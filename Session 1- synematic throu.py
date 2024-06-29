
def BalckManba(v0,theta):
    #section 1
    import math as m
    #degree =rad*(rad/pi)===> rad=degree/(180/pi)
    theta/=(180/m.pi)  
    #R=((v0**2)/g)*(sin(2theta))
    g=9.81
    R=(v0**2)*(m.sin(2*theta)) /g
    print(f"R={R} m")
    #section2
    def y(x):
        return((m.tan(theta))*x)-((g*(x**2))/(2*(v0*m.cos(theta))**2))

    import matplotlib.pylab as plt
    import numpy as np
    x=np.linspace(0,R,1000)
    plt.style.use("ggplot")
    #x=np.arrange(0,R,0.001)
    plt.plot(x,y(x),"b")
    plt.show()
BalckManba(10,60)


