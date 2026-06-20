---
title: "How do I program this dialer to add a 2 second pause after the auto dial number and then dial another number?"
sidebar_position: 3
format: md
---

Using #2 in register 01 adds .5 seconds.  So, added 4 times to add a delay of 2 seconds, as shown in the example below:  
  
For example, program it to auto dial 3055585577 pause (2 seconds) then dial 1:

Step 1) Enter **# 0 \***(you should hear a 'Beep' sound) -- entering the programming mode 

Step 2) Enter **01** (you should hear a 'Beep' sound) -- entering function code to restrict numbers 

Step 3) Enter **3055585577 #2#2#2#2 1**

Step 4) Hang-up or press **##** -- exit
