
#section1
g=9.81
h=eval(input("hight of tower (m):"))
t=eval(input("time (s):"))

#section 2
#y-y0=(-1/2 gt**2)+(v0t)
y=(0.5*g*(t**2))
#print(f"masafat:{y}m")
#print(f"fasele:{h-y}m")

if y>h:
    print("ball touched the ground")
else:
    print(f"ball didnt touche the ground\n\tfasele:{h-y} m")

