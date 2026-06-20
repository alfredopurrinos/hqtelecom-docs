---
title: "Can I add a delay when auto dialing a number?"
sidebar_position: 1
format: md
---

Yes, you can! Register 12 allows you to add an Off hook dial delay in milliseconds  
  
This register comes into play when using the Hotline dial feature or the speed dial numbers. This register

determines the delay from when the phone goes off hook to when it dials the hotline number. When a

speed dial trigger is detected the dialer has to hang up the line to get dial tone back, the dialer delays

this amount of time after getting dial tone back then dials the speed dial number. Scenario: You want

the dialer to delay 2000 milliseconds (2 seconds) before dialing hotline number. How to:

Step 1) Enter **# 0 \***-- wait for beep  
Step 2) **12** -- wait for beep  
Step 3) **2000** -- wait for beep  
Step 4)**##** -- wait for 2 beeps

Hangup

You can also add delays to the digits as they are being dialed out by programming registers 14 & 15  
  
Register 14 Dtmf ON time in milliseconds  
This sets the duration of the dtmf tone of each digit the dialer dials.  
Scenario: You want the dtmf tone on time to be 50 milliseconds. How to:

Step 1) Enter **# 0 \*** -- wait for beep

Step 2) **14** -- wait for beep  
Step 3) **50** -- wait for beep  
Step 4) **##** -- waid for 2 beeps

Hangup  
  
Register 15 Dtmf OFF time in milliseconds  
This sets the duration of the silence period between each dtmf tone the dialer dials.  
Scenario: You want the dtmf tone off time to be 50 milliseconds. How to:

Step 1) Enter **# 0 \*** -- wait for beep

Step 2) **15** -- wait for beep  
Step 3) **50** -- wait for beep  
Step 4) **##** -- waid for 2 beeps

Hangup

Example:  The programing below adds a 2 second delay before start dialing the toll-free number, and also adds a .5 second delay between each digit dialing.

#0\*   : Enter program mode

01  18003468080 ##  : Number to dial

12   2000 ##               : Set 2000 millisecond delay before dialing

15   500 ##                 : Set 500 millisecond delay between dialed digits

Hang up

Here another example:  
Program your dialer to dial \* # 1234, wait 2 seconds, then dial \* \* \*, wait 2 seconds,, then dial \* \* 2 7 \* \*  
For this case, you can add those delays on the register 01 ...  
#0\* : enter program code  
01 (hear beep)  
\* #1 1234 #2 #2 #2 #2 \* \* \* #2 #2 #2 #2 \* \* 27 \* \* ##   
Hang up  
Note (1):  Please note that you need to use "#1" for this dialer to dial #

Note (2):  #2 adds a .5 second delay, so if you want a 2 second delay, you need to add it 4 times.

If you need any more help, please contact us.

>> [Buy this hot dialer](https://www.hqtelecom.com/hotdialer)  | [View all dialers](https://www.hqtelecom.com/dialers/)
