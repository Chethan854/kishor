import time
import matplotlib.pyplot as plt
start=time.time()
def bubblesort(a):
    n=len(a)
    for i in range(n-1):
        for j in range(n-1-i):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
x=[10,58,67,94,34,58,42,14]
print("beforesorting",x)
bubblesort(x)
print("aftersorting",x)
x=list(range(1,10000))
plt.plot(x,[y*y for y in x])
plt.title("bubblesort time complextity")
plt.xlabel("input")
plt.ylabel("time")
plt.show()

