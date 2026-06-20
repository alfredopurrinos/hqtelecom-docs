---
title: "Can I program this device to re-route 911 calls to another number?"
sidebar_position: 2
format: md
---

Yes!  Below are the steps to program this auto dialer to re-route 911 calls to any other number (NNNNNNNNNN).

\*\*\*8888 (hear 1 beep)

\*01\*1\*NNNNNNNNNN\*\* (hear 1 beep)

\*03\*1\*911\*\* (hear 1 beep)

\*15\*911\*\* (hear 1 beep)  
\*18\*1234567890\*\* (hear 1 beep)  
hangup  
  
You can also program this auto dialer to re-route calls from number A to number B, as shown below:

\*\*\*8888 (hear 1 beep)

\*01\*1\*B\*\* (hear 1 beep)

\*03\*1\*A\*\* (hear 1 beep)

\*15\*A\*\* (hear 1 beep)  
\*18\*1234567890\*\* (hear 1 beep)  
hangup  
  
What if you also want to reroute other numbers e.g. 0911, 1911, etc?  
Simply add the other numbers to the registers 03 and 15, as follows:

\*\*\*8888 (hear 1 beep)

\*01\*1\*B\*\* (hear 1 beep)

\*03\*1\*A1\*A2\*A3\*A4\*A5 .... \*AN\*\* (hear 1 beep)  
\*10\*1\*\*  (enables the dialing of the second number or PIN) 

\*15\*A1\*A2\*A3\*A4\*A5 .... \*AN\*\* (hear 1 beep)  
\*18\*1234567890\*\* (hear 1 beep)  
hangup

What if you need to re-route your 911 calls to a carrier that requires 2 sets of numbers (e.g. set 1: a toll-free number, set 2: an access number or pin code)?  
You can use register 02 to add that second string of numbers.  You can also add a delay between the first set of numbers (toll-free number) and the second set of numbers using register 06 as follows (10=1 second, 20=2 seconds, 30=3 seconds, 40=4 seconds, 50=5 seconds, etc):

\*\*\*8888 (hear 1 beep)

\*01\*1\*B\*\* (hear 1 beep)

\*02\*1\*2\*C\*\*  
\*03\*1\*A1\*A2\*A3\*A4\*A5 .... \*AN\*\* (hear 1 beep)

\*06\*1\*50\*\*  
\*10\*1\*\*  
\*15\*A1\*A2\*A3\*A4\*A5 .... \*AN\*\* (hear 1 beep)  
\*17\*1\*00\*3\*\*  
\*18\*1234567890\*\* (hear 1 beep)  
hangup

Where  
A (also A1, A2, A3 ...AN) = the numbers dialed by the users that you want to re-route  
B = the first set of numbers required by your carrier (access number)  
C = the second set of numbers required by your carrier (access code)  
A,B & C are any string of numbers (0-9), up to 16 digits long, including #..

If you need any more help, please contact us.
