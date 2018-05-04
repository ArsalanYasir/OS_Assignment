def read(n,process):
    n = int(input("Enter the total no of processes: "))
    for i in range(0,n):
        process.append([])
        process[i].append(input('Enter p_name: '))  #process name
        process[i].append(int(input('Enter p_arrival: ')))  #arrival time
        process[i].append(int(input('Enter p_bust: ')))     #burst time
        process[i].append(0)    #start time
        process[i].append(0)    #final time
        print (' ')
    return n,process

def add_process_in_running(process,running,lastProcessEnding):
    n = len(process)
    if(process[0][1] <= lastProcessEnding):
        running.append(process[0])
        del(process[0])
    else:    #no process arrived at the ending of last process
        lastProcessEnding += -lastProcessEnding+process[0][1]
        running.append(process[0])
        del(process[0])
    return  lastProcessEnding

def execute(process,running,complete):
    i=0;     #i is for complete queue, and j is for running queue
    n = len(process)    #getting total no of proesses
    lastProcessEnding = 0 
    while i < n:
        lastProcessEnding = add_process_in_running(process,running,lastProcessEnding)
        running[0][3] = lastProcessEnding   #start time is when last process ends
        running[0][4] = running[0][3]+running[0][2]  #and final time is its final time is starting time + burst time
        lastProcessEnding = running[0][4]  #and its the last process executed
        i+=1    #and one process is complete so put it in complete queue
        complete.append(running[0])
        del(running[0])

def cal_time(n,complete):
    w_time = 0; t_time=0
    for i in range(n):
        w_time += complete[i][3]-complete[i][1]
        t_time += complete[i][4]-complete[i][1]
    return w_time,t_time


def display(n,process):
    print ('ProcessName\tArrivalTime\tBurstTime\tStartTime\tFinalTime')
    for i in range(n):
        print (process[i][0],' ',process[i][1],' ',process[i][2],' ',process[i][3],' ',process[i][4])
    print(' ')

if __name__ == "__main__":
    running = []
    process = []
    complete = []
    total_waitTime = 0
    total_turnAroundTime = 0
    n = 0
    n ,process = read(n, process)    
    process.sort(key = lambda process:process[2]) #first sort by burst time
    process.sort(key = lambda process:process[1]) #then sort by arrival time, as it is inplace so the shortest job with best arrival time is here
    execute(process,running,complete)
    display(n,complete)
    total_waitTime,total_turnAroundTime = cal_time(n,complete)    
    print ('Total waiting time: ',total_waitTime)
    print ('Average waiting time: ',(total_waitTime/n) )
    print ('Total turn around time: ',total_turnAroundTime)
    print ('Average turn around time: ',(total_turnAroundTime/n) )

    input("<Press Enter>")
