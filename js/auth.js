(function() {
  const API_TOKEN    = 'https://gwaio-0fb226784267.herokuapp.com/api/v1/session/token';
  const STORAGE_KEY  = 'mkdocs_auth_token';
  const TIME_KEY     = 'mkdocs_auth_time';
  const REDIRECT_KEY = 'mkdocs_auth_target';
  const SESSION_TTL  = 60 * 60 * 1000;

  function ensureTrailingSlash(path) {
    return path.endsWith('/') ? path : `${path}/`;
  }

  function getSiteRootUrl() {
    if (window.__md_scope && typeof window.__md_scope.href === 'string') {
      return new URL('./', window.__md_scope);
    }

    const authScript = document.currentScript || Array.from(document.scripts).find(script => {
      if (!script.src) return false;
      try {
        return new URL(script.src, window.location.href).pathname.endsWith('/js/auth.js');
      } catch (error) {
        return false;
      }
    });

    if (authScript && authScript.src) {
      return new URL('../', new URL(authScript.src, window.location.href));
    }

    if (window.location.pathname.endsWith('/login/')) {
      return new URL('../', window.location.href);
    }

    return new URL('/', window.location.href);
  }

  const SITE_ROOT_URL = getSiteRootUrl();
  const SITE_ROOT     = ensureTrailingSlash(SITE_ROOT_URL.pathname);
  const LOGIN_URL     = new URL('login/', SITE_ROOT_URL);
  const LOGIN_PATH    = ensureTrailingSlash(LOGIN_URL.pathname);

  function isSessionValid() {
    const token = localStorage.getItem(STORAGE_KEY);
    const ts    = parseInt(localStorage.getItem(TIME_KEY), 10);
    return token && !isNaN(ts) && ((Date.now() - ts) < SESSION_TTL);
  }

  function startSession(token) {
    localStorage.setItem(STORAGE_KEY, token);
    localStorage.setItem(TIME_KEY, Date.now().toString());
  }

  function clearSession() {
    localStorage.removeItem(STORAGE_KEY);
    localStorage.removeItem(TIME_KEY);
  }

  function handleLoginForm() {
    const form = document.getElementById('login-form');
    if (!form) return;

    form.action = '.';

    const loginButton = document.getElementById('login-button');
    const spinner = document.getElementById('btn-spinner');

    form.addEventListener('submit', async e => {
      e.preventDefault();

      if (loginButton && spinner) {
        loginButton.classList.add('loading');
        loginButton.disabled = true;
        spinner.classList.remove('sr-only');
      }

      const user = form.user.value;
      const pass = form.pass.value;
      const machineId = 'browser-' + navigator.userAgent;

      const basic = btoa(`${user}:${pass}`);

      try {
        const resp = await fetch(API_TOKEN, {
          method: 'POST',
          headers: {
            'Authorization': `Basic ${basic}`,
            'Content-Type':  'application/json',
            'Accept':        '*/*'
          },
          body: JSON.stringify({ machine_id: machineId })
        });

        if (!resp.ok) {
          throw new Error(`Error ${resp.status}: ${resp.statusText}`);
        }
        const data = await resp.json();
        const token = data.access_token;
        if (!token) {
          throw new Error('No se recibió access_token');
        }

        startSession(token);
        const target = sessionStorage.getItem(REDIRECT_KEY) || SITE_ROOT;
        sessionStorage.removeItem(REDIRECT_KEY);
        window.location.replace(target);

      } catch (err) {
        console.error('Login failed:', err);
        const errorDiv = document.getElementById('error');
        if (errorDiv) {
            errorDiv.textContent = 'Incorrect username or password.';
            errorDiv.style.display = 'block';
        }
      } finally {
        if (loginButton && spinner) {
          loginButton.classList.remove('loading');
          loginButton.disabled = false;
          spinner.classList.add('sr-only');
        }
      }
    });
  }

  async function requireLogin() {
    const path = ensureTrailingSlash(window.location.pathname);
    if (path === LOGIN_PATH) {
      document.documentElement.style.visibility = '';
      handleLoginForm();
      return;
    }

    if (!isSessionValid()) {
      clearSession();
      sessionStorage.setItem(
        REDIRECT_KEY,
        window.location.pathname + window.location.search + window.location.hash
      );
      window.location.replace(LOGIN_URL.href);
    } else {
      startSession(localStorage.getItem(STORAGE_KEY));
      document.documentElement.style.visibility = '';
    }
  }

  requireLogin();
})();
