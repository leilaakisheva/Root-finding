

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline

#function mach represents the formula of spherically symmetric flow of an ideal gas onto black hole
def mach(M,r):
  return 2*np.power(r,4)*np.power(M,2)*np.power(((2+6*r)/(r*(M**2+6))),7)-1

#defining a function for bisecting method
def bsec(x1, x2, r, p, imax):
  x_r=x2
  x=np.zeros(imax); e=np.zeros(imax); it=np.zeros(imax)
  for i in range(imax):
    x_rold=x_r
    x_r=(x1+x2)/2
    if (x_r!=0.0):
      ea=abs((x_r-x_rold)/x_r)*100
    it[i]=i; x[i]=x_r; e[i]=ea
    test=mach(x1, r)*mach(x_r, r)
    if (test<0.0):
      x2=x_r
    elif (test>0.0):
      x1=x_r
    else:
      ea=0.0
    if (ea<p):
      break
  return it,x_r, e

"""### **Part A**
I used values of mach(M,r) function near 0 to estimate value of variable M there. So, it could be seen in what range it lays and could be possible to choose first guess of boundary values.
"""

M=np.arange(0, 7, 0.001) #arranging values for M
y=np.zeros(7000)
for i in range(7000):
  y[i]=mach(M[i], 0.025) #filling array with the values from mach function
  if mach(M[i],0.025)<0.0 and mach(M[i], 0.025)>-1e-2:
#checking if the function is near 0.
#If it is, then values of M there should be close to the actual value of M
#it was done in order to find a lower boundary guess and an upper boundary guess
    print('Value of Mach number =', round(M[i], 4), 'at y =', mach(M[i], 0.025))
plt.plot(M,y)
plt.grid()

#checking computed value of M (the actual value)
#as it could be seen that its value lays between 3 and 3.5
i, M, e = bsec(3, 3.5, 0.025, 1e-12,50)
print(M)

"""**Plot 1**"""

plt.plot(i,e)
plt.xlabel("Iteration number")
plt.ylabel("Error")
plt.yscale("log")
plt.grid()

"""### **Part B**"""

r=np.linspace(0.025, 0.5, 20) #making a uniformly distributed array of numbers between 0.025 and 0.5
M=np.linspace(0, 5, 20)
y=np.zeros(20)
for i in range(20):
  if r[i]<0.25: #supersonic values
    if mach(M[i],r[i])>=-1 and mach(M[i],r[i])<=1:
      n, m, e = bsec(1, 5, r[i], 1e-12,500) #bisecting between 1 and 5, because supersonic values are >1
      y[i]=m
    print(i+1,') M = ', round(m, 4), ', for r =', round(r[i],3))
  elif (r[i]>0.25): #subsonic values
    if mach(M[i],r[i])>=-1 and mach(M[i],r[i])<=1:
      n, m, e = bsec(0, 1, r[i], 1e-12,500) #bisecting between 0 and 1, because subsonic values are <1
      y[i]=m
    print(i+1,') M =', round(m, 4), ', for r =', round(r[i],3))
  elif(r[i]==0.25): #should be approximately 1
    n, m, e = bsec(0, 1, r[i], 1e-12,500)
    y[i]=m
    print(i+1,') M =', round(m, 4), ', for r =', round(r[i],3))

"""**Plot 2**"""

plt.plot(r,y)
plt.xlabel("Radius (r)")
plt.ylabel("Mach value (M)")
