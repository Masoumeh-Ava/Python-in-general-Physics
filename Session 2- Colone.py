#f=k*((q1*q2)/r^2)

k=8.98e9
q1=eval(input("enter q1:"))
q2=eval(input("enter q2:"))
r=eval(input("enter r:"))

def forc(q1,q2,r):
    f=k*((q1*q2)/(r**2))
    return(f)
    


print(f"total force is {forc(q1,q2,r)}c")

    