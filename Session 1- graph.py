import matplotlib.pylab as plt
#section1
x0=eval(input("please enter x0:"))
v0=eval(input("please enter v0:"))
a=eval(input("please enter a:"))
ti=eval(input("please enter t:"))
time=range(ti+1)

#section2
x=[]
for t in time:
    x1=(0.5*a*(t**2))+(v0*t)+x0
    x.append(x1)

#section 3
v=[]

for t in time:  
    v1=(a*t)+v0
    v.append(v1)
#section 4
a=[a]*(ti+1)

plt.plot(time,x,marker="*",color="r",label="displacement")
plt.show()
plt.plot(time,v, "bs" ,label="velocity")
plt.show()
plt.plot(time,a,label="acceleration")

plt.legend(loc="upper left")

plt.xlabel("time")
plt.ylabel("X,V,A")
plt.title("full plot")
plt.grid()
plt.show()
