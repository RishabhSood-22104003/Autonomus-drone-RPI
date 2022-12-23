import itertools
e_prev = list(itertools.repeat(0,100))
total=0
for ele in range(0,len(e_prev)):
    total = total + e_prev[ele]

def PID(Kp, Ki, Kd, Distance=0):
    e = Distance
    e_prev.insert(0,e)
    del e_prev[100]
    P = Kp*e
    I = Ki*sum(e_prev) # summ of elements of e
    D = Kd*(e_prev[0]-e_prev[1]) # previous error - current error

    Distance_new =  P + I + D
    print(Distance_new)
PID(100,100,5 ,5 )
PID(100,100,5 ,4 )
PID(100,100,5 ,3 )
PID(100,100,5 ,2 )
PID(100,100,5 ,1 )
PID(100,100,5 ,0 )
PID(100,100,5 ,-1)
PID(100,100,5 ,-2 )


