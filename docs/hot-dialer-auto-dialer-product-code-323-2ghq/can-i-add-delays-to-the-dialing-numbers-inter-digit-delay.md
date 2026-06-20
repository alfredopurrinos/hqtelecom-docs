---
title: "Can I add delays to the dialing numbers (inter-digit delay)?"
sidebar_position: 5
format: md
---

Yes, use the following command lines to add 1 to 2 second inter-digit delays between the dialing number(s):

1 second delay between digits:   
  
\*\*\*.    (wait for beep)    
\*\*9\*\* (wait for beep)  
\*9\*1\*\*200\*NUMBER\*\* (wait for beep)  
\*\*235\* (enables off-hook dialing) (wait for beep)  
\*\*4\*11\* (inter-digit timer settings) (wait for beep)

\*\*2110\* (wait for beep)  
\*\*2210\* (wait for beep)

1.5 second delay between digits:   
Replace the last 2 commands for these:

\*\*2115\*  
\*\*2215\*

2 second delay between digits:   
Replace the last 2 commands for these:

\*\*2120\*  
\*\*2220\*

If you are programming it remotely (calling it from another line), then you must use the command below to enter the programming mode:   
\*#1234 (wait for beep)
