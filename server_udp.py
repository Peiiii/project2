import socket
import threading

def test1():
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind(('127.0.0.1',9999))
    print('Bind to 127.0.0.1:9999...')
    i=0
    while True:
        data,addr=s.recvfrom(1024)
        if data.decode('utf-8')=='exit':
            break
        print(data.decode('utf-8'),addr)
        print('got it!')
        s.sendto(("Hello,%s!"%data.decode('utf-8')).encode('utf-8'),addr)

        #t=threading.Thread(target=udplink,args=(sock,addr))
        #t.start()
        i+=1
    s.close()
    print('Terminated.')


def udplink(sock,addr):
    print('Accept new connection from %s:%s...'%addr)
    sock.sendto(b'Welcome!',addr)
    while True:
        data=sock.recv(1024)
        if data.decode('utf-8')=='exit':
            break
        print('Recieving a new message [%s]'%data.decode('utf-8'))
        sock.sendto(('Hello! %s'%data.decode('utf-8')).encode('utf-8'),addr)
    sock.close()
    print('Connection from %s:%s closed.'%addr)

if __name__=="__main__":
    test1()