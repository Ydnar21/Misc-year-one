import threading
import time
import sys
import subprocess
#from StringIO import StringIO

philosophers_num = 5
go = True


class Philosopher(threading.Thread):
    def __init__(self, threadID, Llock, Rlock):
        threading.Thread.__init__(self)
        self.id = threadID
        self.Llock = Llock
        self.Rlock = Rlock

    def run(self):
        #both forks must be available at the same time
        global go
        while go:
            #use acquire and lock
            done = False
            print(f"philosopher {self.id} is thinking...")
            while not done:
                    self.Llock.acquire()
                    print(f"philosopher {self.id} picks up left fork")
                    acquired = self.Rlock.acquire(False)
                    if acquired:
                        print(f"philosopher {self.id} picks up right fork")
                        break
                    else:
                        self.Llock.release()
                        print(f"philosopher {self.id} puts down left fork.")
                    time.sleep(.2)

            print(f"philosopher {self.id} is eating...")
            print(f"philosopher {self.id} puts down left fork.")
            self.Llock.release()
            print(f"philosopher {self.id} puts down right fork.")
            self.Rlock.release()





def main():
    global philosophers_num
    global go
    philosophers_num =int(sys.argv[1])
    threads = []
    locks = [threading.Lock() for _ in range(philosophers_num)]
    for i in range(philosophers_num):
        thread = Philosopher(i, locks[i], locks[(i+1)%philosophers_num])
        threads.append(thread)
    for i in range(philosophers_num):
        threads[i].start()

    time.sleep(2)
    go = False


main()