Hello all,

I would like to share a recap on the development of the teaser, regarding what worked, what did not work and possible solutions.

## Artists availability
### Problem
In some cases, artists were either working on other projects, working for just a week or working at very unual times (fron 5pm onwards, for isntance), working overtime or with tight schedules. This of course is far from ideal because:
1. artists need a period for adapting to workflows
2. artists need to overlap their working hours with other team members
3. things may not go as expected so artists need a bit of buffer
### Solution
This is tricky as there is a lack of talent available in the island, this was worsen by the specs of the teaser (very short time period). I know that the best was done by HR given the circumstances, so I have nothing to add/sugges here, but I still wanted to metion this.
### Relevance
High

## VPN being slow
Any VPN is a limited resource, but with a low budget it is the best we can do, at least that I know of. That's why we use artist's own machines for remote users.
### Problems
File transfer in general is slow and may hold an artist from working. This is OK for small files, but for big files such as those used in Substance Painter and ZBrush, this is not bearable.
### Solution (mostly implemented already)
1. Prevent using the VPN for these files: as this became an issue with the shading department during the teaser we came up with the solution of using SG as an intermediary (cloud storage) when a transfer of big files happens.
2. Collecting all dependencies in a zip file with a script and transfer them to the artists to prevent having them download all the dependencies through the VPN.
3. Optimize source files so that they are not as heavy:
  - Substance Painter has an option for reducing file size
  - Exporting compressed EXR with DWAB compresion (45 is almost loseless) or using other lighter image format such as PNG.
  - Improve the tool for synchronizing through the VPN so it is easier to get the files we need.
### Relevance
Low

## Overlapping departments
Because we spent many months cycling through concepts, fur issues and without render farm, very little time was left to make the actual teaser, this meant that many departments were overlapping at the same time, having many people working in parallel.
### Problems
Having people working in parallel makes things very messy, it creates a bottle neck because departments don't have their input ready simply because the previous department is not done, so they start working with unfinished assets and in sub-optimal conditions.
This becomes obvious when we look at the rough dates:
- 2023/03/31 - Layout starts
- 2023/04/04 (5 weeks ago) - both Bruno and Jau start
- 2023/04/17 - 010_020 is approved in layout
- 2023/04/14 (1 month ago) - first successful connection to Deadline from remote
- 2023/04/18 - 010_020 is approved in refine
- 2023/04/20 - Lighting starts
- 2023/04/21 - Shading is finishing.
- 2023/04/23 - Dani starts
### Solution?
Having a maximum number of retakes so that deparments can close tasks? This is tricky as most of this is client-dependent. But keep moving the production as if certain tasks were approved may at least help the dependant departments have an idea of the workload, so basically what we did in the Teaser, but with more time so that dependent departments are not in a tight schedule.
### Relevance
High

## Tools to be improved/not ready
As a result of the department overlap, some tools were not polished as they hadn't been used before, so when a new department was opened in a hurry some tools were not perfect.
### Problem
Departments were opened without a testing period, this was more relevant for both animation and lighting.
### Solution
Idealy if we keep moving the production through the pipeline, tools can be tested and created so that when they become critical, they work perfectly. Nonetheless most of the key problems are either solved or in the process to be solved, but it is a good idea to keep animating and lighting shots and asking artists for their opinion on how to improve their workflow.
### Relevance
Medium

## The files in the server seem messy
The compositing department was complaining because the renders were all over the place
### Problems
The lighting department was working in a rush for about 2 weeks, they didn't have the time to look at the documentation/understand the tools and they were not being consistent about where to put the output of their renders.
### Solution
In the Pipeline Document was stated that a task called render would be assigned to the person who was creating the final renders. This task has its own filesystem, that holds the render output. This task was never assigned through Shotgrid.
Reach a consensus and ask lighters how can we help them understand better the processes and also talk to the compositing department about how they prefer to configure this settings.
### Relevance
Medium/Low

## Many people is new to Shotgrid
It is my perception that most of the team has little experience with Shotgrid, this leads to several problems.
### Problems
People who actually know shotgrid has to constantly supervise and help people who doesn't know shotgrid
People doesn't understand correctly their assignments or how to properly review content in SG.
### Solutions
Having Shotgrid as a requirement for the interviews when possible
Having people complete the online SG tutorials
Giving people enough time to get used to SG, or having a dedicated SG expert to help with that.
### Relevance
Low

## Team Composition
It is my opinion that the team seems to be segmented, and the team's overall know-how could be improved.
### Problems
If people doesn't know how to use Deadline, the hole production relies on the few people that knows.
Some departments don't have a Supervisor, which renders it components without a clear leadership when tey don't know how to solve a technical problem.
### Solutions
Having the team talk more and learn mor from each other
Having maybe some generalist profiles in the team with experience in Maya, Deadline and Arnold/Redshift?
Having an expert that knows how to handle character fxs such as fur.


## Artists are not used to the tools
Many times people misunderstand/misuse the tools
### Problems
1. Technical people has to explain 100 times the same things
2. People don't follow (or may not even know) the workflows/guidelines
### Solution
Make tools more accesible to artists.
Making tutorials and documentation more accesible
Fixing bugs that the tools may have
Having production check on these things and looking at when someone may not be following processes
Having automations to check whether people are not following the processes.
### Relevance
Medium
