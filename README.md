# Root-finding
In this study I investigate Bisection method for the formula of spherically symmetric flow of an ideal gas onto black hole. Given some radius  r , I computed values of Mach number  M . Also, it was defined how number of iterations and error are related using the plot.

First I import all the necessary libraries and define function mach(M,r). Then, I define the function bsec which is used as the method of computing the solution. Variables of the function bsec are x1 - lower boundary, x2 - upper boundary, r - radius, p - error, imax - maximum number of iterations.
I used values of mach(M,r) function near 0 to estimate value of variable M there. So, it could be seen in what range it lays and could be possible to choose first guess of boundary values.

Plot 1
![image](https://github.com/leilaakisheva/Root-finding/assets/128895782/79084b19-937b-4ed3-8000-ab7b4956d4e3)
Value of Mach number = 0.102 at y = -0.0019463699774129317
Value of Mach number = 3.169 at y = -0.0018225091595096554
Value of Mach number = 3.17 at y = -0.003950741360807752
Value of Mach number = 3.171 at y = -0.006074414997626065
Value of Mach number = 3.172 at y = -0.008193539584907539


ERROR PLOT
![image](https://github.com/leilaakisheva/Root-finding/assets/128895782/8c2fa586-8cc5-4d58-a2fa-7cc14373f7d0)

Plot 2
![image](https://github.com/leilaakisheva/Root-finding/assets/128895782/22abf909-75ce-476b-9062-88cd518e0a37)

1 ) M =  3.1681 , for r = 0.025
2 ) M =  2.4043 , for r = 0.05
3 ) M =  2.0026 , for r = 0.075
4 ) M =  1.7369 , for r = 0.1
5 ) M =  1.5418 , for r = 0.125
6 ) M =  1.3897 , for r = 0.15
7 ) M =  1.2663 , for r = 0.175
8 ) M =  1.1634 , for r = 0.2
9 ) M =  1.0758 , for r = 0.225
10 ) M =  1.0 , for r = 0.25
11 ) M = 0.9337 , for r = 0.275
12 ) M = 0.8749 , for r = 0.3
13 ) M = 0.8225 , for r = 0.325
14 ) M = 0.7754 , for r = 0.35
15 ) M = 0.7328 , for r = 0.375
16 ) M = 0.6941 , for r = 0.4
17 ) M = 0.6587 , for r = 0.425
18 ) M = 0.6262 , for r = 0.45
19 ) M = 0.5963 , for r = 0.475
20 ) M = 0.5687 , for r = 0.5

Results
From the plot 1 it can be seen that the number of iterations and error related logarithmically . The graph is in log scale, so there is a logarithmic decay of error as the number of iterations grows. Also, from the plot 2 it is possible to conclude that Mach Number and radius are also logarithmically dependent. From the results of Part A, it can be seen that approximating values from the plot, where the function is near 0 is also a nice method for guessing the boundary conditions. From the Part B it can be seen that bisection method is actually a great techinque of finding a solution to the equation, since all of the values of M match the actual values to a very high extent.

Conclusion
In this paper, I analyzed the bisection approach for the spherically symmetric flow of an ideal gas onto black holes. I calculated the Mach numbers  M  for various radiuses  r . The graphics also demonstrated the relationship between the number of iterations and the error value. Overall, the assesment was succesfull and the method is proved to be reliable.
