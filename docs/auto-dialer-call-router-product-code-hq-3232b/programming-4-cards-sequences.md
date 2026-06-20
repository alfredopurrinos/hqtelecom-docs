---
title: "Programming 4 cards (sequences)"
sidebar_position: 1
format: md
---

Below are the steps to program 4 sequences using HQTelecom's Calling Card Auto Dilaer

Each number set (A-L) can consist of any combination of digits 1-9, #, except asterisk (\*)

Sequence 1, has numbers A, B & C

sequence 2: D, E, F

sequence 3: G, H, I

Sequence 4: J, K, L

Sequence 1 will use 1 as a trigger, after lifting the handset (going off hook)

Sequence 2 will use 2 as a trigger, after lifting the handset (going off hook)

Sequence 3 will use 3 as a trigger, after lifting the handset (going off hook)

Sequence 4 will use 4 as a trigger, after lifting the handset (going off hook)

**Programming:**

**\*\*\*8888**        ; login

**\*00\*\***            ; reset

Sequence 1:

**\*01\*1\*A\*\***     ; enter 1st number (or access number) - any combination of digits 1-9, #, except asterisk (\*)

**\*02\*1\*B\*C\*\*** ; enter 2nd number (or PIN) and 3rd number (or destination number) - any combination 1-9, #

**\*03\*1\*1\*** ; trigger for sequence # 1 (1 - 4)

**\*06\*1\*99\*\***    ; delay between 1st number and 2nd number (99 = 10 seconds)

**\*08\*1\*20\*\***    ; delay between 2nd number and 3rd number (20 = 2 seconds)

**\*11\*1\*0\*\***; disable IVR (voice) detection

**\*10\*1\*1\*\***; enable 2nd number (or PIN)

Sequence 2:

**\*01\*2\*D\*\***

**\*02\*2\*E\*F\*\***

**\*03\*2\*2\***

**\*06\*2\*99\*\***

**\*08\*2\*50\*\***

**\*11\*2\*0\*\***

**\*10\*2\*1\*\***

Sequence 3:

**\*01\*3\*G\*\***

**\*02\*3\*H\*I\*\***

**\*03\*3\*3\***

**\*06\*3\*99\*\***

**\*08\*3\*50\*\***

**\*11\*3\*0\*\***

**\*10\*3\*1\*\***

Sequence 4:

**\*01\*4\*J\*\***

**\*02\*4\*K\*L\*\***

**\*03\*4\*4\***

**\*06\*4\*99\*\***

**\*08\*4\*50\*\***

**\*11\*4\*0\*\***

**\*10\*4\*1\*\***

**\*15\*1234\*\*** ; enable sequence triggers 1-4

Note: this programming will dial the sequences followed by the trigger.

For example, if you go off hook and press 1, the dialer will dial number A, wait 10 seconds, B, wait 2 seconds, then C, then 1

Tip: You may want to end the 3rd number with pound (#) to prevent any issues with the trigger.
  
  
[Product link](https://hqtelecom.com/callingcarddialer)

[Manual](http://hqtelecom.com/callingcarddialer-manual.pdf)
