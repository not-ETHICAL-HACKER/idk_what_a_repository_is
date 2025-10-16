import matplotlib.pyplot as plt
import sys,time,math
def golden_ratio (limit:int=10,cooldown:float=0.1,animate:bool=False,graph:bool=False):
    a,b=1,1
    g_r_list=[]
    for _ in range(limit):
        def test(x=str):
            sys.stdout.write("\r"+x)
            sys.stdout.flush()
            time.sleep(cooldown)
        if animate:
            test(str(a))
        else:
            print(a)
            time.sleep(0.1)
        g_r=b/a
        a,b=b,b+a
        g_r_list.append(g_r)
    print(f"\nthe golden ratio(approx)is:{g_r}")
    if not graph:
        return g_r
    else:        
        # Plot the approximations
        plt.plot(g_r_list, label="Approximations",color="gold")

        # Plot a horizontal line at the true golden ratio
        plt.axhline(y=golden_rati, color='red', linestyle='--', label="True φ")

        plt.xlabel("Iteration")
        plt.ylabel("Approximation of φ")
        plt.title("Convergence to the Golden Ratio")
        plt.legend()
        plt.show()
        return g_r_list
golden_rati = (1 + math.sqrt(5)) / 2
a=int(input("enter a limit for the calculations:"))
c=golden_ratio(a,cooldown=0.5,animate=True,graph=True)
