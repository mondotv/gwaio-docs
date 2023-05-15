# Recap on the development of the Teaser
Last revision: 2023/05/11  
Author: Juan Moraga Martín

## Table of contents
- [Recap on the development of the Teaser](#recap-on-the-development-of-the-teaser)
  - [Table of contents](#table-of-contents)
  - [Summary](#summary)
  - [Artists availability](#artists-availability)
    - [Problems](#problems)
    - [Proposed solution](#proposed-solution)
    - [Relevance: High](#relevance-high)
  - [VPN being slow](#vpn-being-slow)
    - [Problems](#problems-1)
    - [Proposed solution (mostly implemented already)](#proposed-solution-mostly-implemented-already)
    - [Relevance: Medium](#relevance-medium)
  - [Overlapping departments](#overlapping-departments)
    - [Problems](#problems-2)
    - [Proposed solution¿?](#proposed-solution-1)
    - [Relevance: High](#relevance-high-1)
  - [Tools to be improved/not ready](#tools-to-be-improvednot-ready)
    - [Problem](#problem)
    - [Proposed solution](#proposed-solution-2)
    - [Relevance: Medium](#relevance-medium-1)
  - [The files in the server seem messy](#the-files-in-the-server-seem-messy)
    - [Problems](#problems-3)
    - [Proposed solution](#proposed-solution-3)
    - [Relevance: High](#relevance-high-2)
  - [Many people is new to Shotgrid](#many-people-is-new-to-shotgrid)
    - [Problems](#problems-4)
    - [Proposed solutions](#proposed-solutions)
    - [Relevance: High](#relevance-high-3)
  - [Artists are not used to the tools](#artists-are-not-used-to-the-tools)
    - [Problems](#problems-5)
    - [Proposed solution](#proposed-solution-4)
    - [Relevance: Medium](#relevance-medium-2)

<br /><br />
<br />


## Summary
This is an recap on the development of the teaser, regarding what worked, what did not work and possible solutions.
I haven't assigned any order to this list of issues as I think all off them should be addressed regardless its relevance, frequency or difficulty.

## Artists availability
In some cases, artists were either working on other projects, working for just a week or working at very unual times (fron 5pm onwards, for instance), working overtime or with tight schedules. 
### Problems
This of course is far from ideal because:
1. artists need a period for adapting to workflows
2. artists need to overlap their working hours with other team members to find solutions to problems
3. things may not go as expected so artists need a bit of buffer time to be able to react to this issues.
4. technical departments need to be switching licenses constantly and in a rush which is not ideal.
### Proposed solution
This is a tricky problem as there is a lack of talent available in the island, this was worsen by the specs of the teaser (very short time period/tight deadline). I know that the best was done by HR given the circumstances, so I have nothing to add/suggest here, but I still wanted to metion this, so that maybe in the future we can give more room to departments and artists.
### Relevance: High

## VPN being slow
Any VPN is a limited resource, but with a low budget it is the best we can do, as we can not have 1 PC per artist at Tomavision. That's why we use artist's own machines for remote users.
### Problems
File transfer in general is slow and may hold an artist from working. This is OK for small files, but for big files such as those used in Substance Painter and ZBrush, this is not bearable.
### Proposed solution (mostly implemented already)
1. Prevent using the VPN for these files: as this became an issue with the shading department during the teaser we came up with the solution of using SG as an intermediary (cloud storage) when a transfer of big files happens.
2. Collecting all dependencies in a zip file with a script and transfer them to the artists to prevent having them download all the dependencies through the VPN.
3. Optimize source files so that they are not as heavy:
    - Substance Painter has an option for reducing file size
    - Exporting compressed EXR with DWAB compresion (45 is almost loseless) or using other lighter image format such as PNG.
    - Improve the tool for synchronizing through the VPN so it is easier to get the files we need.
4. Having machines at the studio so that departments that have a lot of data I/O such as compositing can use them. So far the only department where this has been a must was both Editing and Compositing.
### Relevance: Medium

## Overlapping departments
Because we spent many months cycling through concepts, fur issues and without render farm, very little time was left to make the actual teaser, this meant that many departments were overlapping at the same time, having many people working in parallel.
### Problems
Having people working in parallel makes things very messy, it creates a bottle necks because departments don't have their input ready when they are supposed to start simply because the previous department is not done, so they start working with unfinished assets and in sub-optimal conditions.
This becomes obvious when we look at the rough dates:
- 2023/03/31 - Layout starts
- 2023/04/04 - both Bruno and Jau start
- 2023/04/17 - 010_020 is approved in layout
- 2023/04/14 - first successful connection to Deadline from remote
- 2023/04/18 - 010_020 is approved in refine
- 2023/04/20 - Lighting starts
- 2023/04/21 - Shading is finishing.
- 2023/04/23 - Dani starts
### Proposed solution¿?
Having a maximum number of retakes so that deparments can close tasks? This is tricky as most of this is client-dependent. But keep moving the production as if certain tasks were approved may at least help the dependant departments have an idea of the workload, so basically what we did in the Teaser, but with more time so that dependent departments are not in such a tight schedule.
### Relevance: High

## Tools to be improved/not ready
As a result of the department overlap, some department-specific tools were not polished as they hadn't been used before, so when a new department was opened in a hurry some tools were not tested before hand by the department artists to provide feedback.
### Problem
Departments were opened without a testing period, this was more relevant for both animation and lighting.
### Proposed solution
Idealy if we keep moving the production through the pipeline, tools can be tested and created so that when they become critical, they work perfectly.  Nonetheless most of the tools key problems that appeared during the teaser are either solved or in the process to be solved, but it is a good idea to keep animating and lighting shots and constantly asking artists for their opinion on how to improve their workflow.
### Relevance: Medium

## The files in the server seem messy
The compositing department was complaining because the renders were saved all over the place
### Problems
The lighting department was working in a rush for about 2 weeks, they didn't have the time to look at the documentation/understand the tools/pipeline and they were not being consistent about where to put the output of their renders. Also there was no standarization on rendering processes.
### Proposed solution
In the Pipeline document was stated that a task called render would be assigned to the person who was creating the final renders. This task has its own filesystem, that holds the render output. This task was never assigned through Shotgrid, so assigning it and having the rendering people understand this will solve the problem.  
Reach a consensus and ask lighters how can we help them understand better the processes and also talk to the compositing department about how they prefer to configure this settings.
### Relevance: High

## Many people is new to Shotgrid
It is my perception that most of the team has little experience with Shotgrid, this leads to several problems.
### Problems
People who actually know shotgrid has to constantly supervise and help people who doesn't know shotgrid.  
People doesn't understand correctly their assignments or how to properly review content in SG.  
People have a wrong idea about what SG is and raise errors/problems that are not really errors/problems.
### Proposed solutions
Having Shotgrid as a requirement for the interviews when possible.  
Having people complete the online SG tutorials.  
Giving people enough time to get used to SG, or having a dedicated SG expert to help with that.
### Relevance: High

## Artists are not used to the tools
Many times people misunderstand/misuse the tools.  
Tools are presented to the artists in 4 ways:
1. Introductory meeting where I show them around.
2. PDF file that they can always reach out to.
3. Long pipeline docuement that holds descriptions for their tasks
4. Video file explaining how tools work.
### Problems
1. Technical people has to explain 100 times the same things.
2. People don't follow (or may not even know) the workflows/guidelines.
### Proposed solution
Make tools more accesible to artists.  
Making tutorials and documentation more accesible. 
Asking artists to write down notes as things are being explained to them.  
Giving artists more time to get used to the tools and let them learn at their own pace.  
Fixing bugs that the tools may have.  
Having production check on these things and looking at when someone may not be following processes.  
Having automations to check whether people are not following the processes?
### Relevance: Medium
