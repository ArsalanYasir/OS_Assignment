def read(n,p,timequantum):
    n = int(input("Enter the total no of processes: "))
    timequantum = int(input("Enter the time quantum: "))
    for i in range(0,n):
        p.append([])
        p[i].append(input('Enter process_name: '))  
        p[i].append(int(input('Enter process_arrivalTime: ')))  
        p[i].append(int(input('Enter process_burstTime: ')))  
        p[i].append(0)  
        p[i].append(0)   
        p[i].append(p[i][2])    
        p[i].append(0)   
        print (' ')
    return n,p,timequantum
def execute(p,running,complete,executing,timequantum):
    p.sort(key = lambda p:p[1]) #sort by arrival time
    i=0
    lastProcessEnding = 0
    n = len(p)
    while i<n:
        add_process_in_running(p,running,lastProcessEnding)
        
        if not running:
            k = 0   
        else:
            if running[0][2] == running[0][5]:
                running[0][3] = lastProcessEnding
            if running[0][2] <= timequantum:
               
                lastProcessEnding += timequantum
				running[0][2] = 0
                running[0][4] = lastProcessEnding
                complete.append(running[0])
                i+=1
                del(running[0])
            else:
                running[0][2] -= timequantum
                lastProcessEnding += timequantum
                add_process_in_running(p,running,lastProcessEnding)
                running.append(running[0])
                del(running[0])
  
def add_process_in_running(p,running,lastProcessEnding):
    n = len(p)
    added =0
    for i in range(n):
        if  p[i][6] == 0 and p[i][1] <= lastProcessEnding:  
            running.append(p[i])
            p[i][6] = 1   
            added += 1
    if added == 0 and n>0:
        lastProcessEnding += p[0][1]-lastProcessEnding
    return lastProcessEnding


def cal_time(n,complete):
    w_time = 0; t_time=0
    for i in range(n):
        w_time += complete[i][4]-complete[i][1]-complete[i][5]
        t_time += complete[i][4]-complete[i][1]
    return w_time,t_time

def display(n,p):
    print ('ProcessName\tArrivalTime\tBurstTime\tStartTime\tFinalTime')
    for i in range(n):
        print (p[i][0],' ',p[i][1],' ',p[i][5],' ',p[i][3],' ',p[i][4])
    print(' ')

if __name__ == "__main__":
    running = []
    p = []
    complete = []
    executing = []
    total_waitingTime = 0
    total_turnAroundTime = 0
    n = 0; timequantum = 0
    n ,p, timequantum = read(n, p, timequantum)
	execute(p,running,complete,executing, timequantum)
    display(n,complete)
	total_waitingTime,total_turnAroundTime = cal_time(n,complete)    
    print ('Total waiting time: ',total_waitingTime)
    print ('Average waiting time: ',(total_waitingTime/n) )
	print ('Total turn around time: ',total_turnAroundTime)
    print ('Average turn around time: ',(total_turnAroundTime/n) )


    input("<Press Enter>")

