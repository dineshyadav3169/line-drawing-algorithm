import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

def sign(a):
    if a>0:
        ret = 1
    elif a<0:
        ret = -1
    else:
        ret = 0
    return ret

x0 = int(input("Enter x1 :")) 
y0 = int(input("Enter y1 :")) 
x1 = int(input("Enter x2 :")) 
y1 = int(input("Enter y2 :")) 
print("\n#############")

x = x0
y = y0
dx = abs(x1-x)
dy = abs(y1-y)
s1 = sign(x1-x0)
s2 = sign(y1-y0)

if dy>dx:
    dx, dy = dy, dx
    interchange = 1
else:
    interchange = 0

print("dx : ",dx,"\ndy : ",dy)
e = 2*dy - dx
print("e : ",e)
print("interchange :", interchange,"\n")
#display list
x_list = []
y_list = []
x_ = []
y_ = []
e_ = []

for i in range(dx):
        x_list.append(x)
        y_list.append(y)
        while(e>=0):
            if interchange==1:
                x = x +s1
                
            else:
                y = y + s2
                
            e = e - 2*dx
        if interchange==1:
            y = y + s2
            
        else:
            x = x + s1
            

        e = e + 2*dy
        e_.append(e)

print(pd.DataFrame({"X":x_list, "Y":y_list,"e":e_}))

plt.scatter(x_list, y_list, color='red')
plt.plot(x_list, y_list)
plt.show()
