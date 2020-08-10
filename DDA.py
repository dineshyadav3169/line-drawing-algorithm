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
dx = x1 - x0
dy = y1 - y0

if abs(dx)>=abs(dy):
    step = abs(dx)
else:
    step = abs(dy)

print('step = ',step)

dx = dx/step
dy = dy/step

print('dx = ',dx)
print('dy = ',dy)

x = x0 + 0.5 
y = y0 + 0.5
print('x = ',x)
print('y = ',y)
print("\n\n")
#display list
x_list = []
y_list = []
x_ = []
y_ = []

i=1
while i<=step:
    x_.append(x)
    y_.append(y)
    
    x_list.append(int(x))
    y_list.append(int(y))
    x = x + dx
    y = y + dy
    i+=1

print(pd.DataFrame({"X":x_list, "Y":y_list, "X point":x_,"Y point":y_}))

plt.scatter(x_list, y_list, color='red')
plt.plot(x_list, y_list)
plt.show()
