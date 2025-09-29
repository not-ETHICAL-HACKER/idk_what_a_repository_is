import time,sys,matplotlib
class game:
    def __init__(self,x=0):
        self.x = x
    def dance(self,x=0):
        frames = ["|","/","-","\\"]
        for i in range(240):
            for f in frames:
                sys.stdout.write("\r"+(f*20))
                sys.stdout.flush()
                time.sleep(x)
    def star(self):
        for i in range(10):
            time.sleep(0.1)
            print(" "*(10-i)+"*"*(i*2+1))
        for i in range(8,-1,-1):
            time.sleep(0.1)
            print(" "*(10-i)+"*"*(i*2+1))
game().star()