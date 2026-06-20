---
title: "Can I disallow all outbound calls except a few?"
sidebar_position: 2
format: md
---

Yes, you can ... To disallow all calls, simply add \* to the disallow register 05, as follows:

#0\*  

05    

\*      

##     
99  

hangup

If you wish to alllow dialing of certain numbers, please use register 08, as follows:

#0\* 

05   

\*    

##  

08  

(enter number 1 e.g. 305-558-5577)  

##

08 

(enter number 2 e.g. 786-221-5997)

##   
(you can keep adding numbers to the allow register)

99   
hangup  
  
You should hear a beep after each programming line above.
