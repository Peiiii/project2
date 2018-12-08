import socket
import threading

def test1():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('207.148.94.195',80))
    s.listen(5)
    print('Waiting for connection...')
    i=0
    while True:
        sock,addr=s.accept()
        t=threading.Thread(target=tcplink,args=(sock,addr))
        t.start()
        i+=1


def tcplink(sock,addr):
    print('Accept new connection from %s:%s...'%addr)
    while True:
        data=sock.recv(1024)
        if data.decode('utf-8')=='exit':
            break
        print('Recieving a new message [%s]'%data.decode('utf-8'))
        response='HTTP/1.1 200 0K\r\n\r\n<h1>Hi</h1>'
        sock.send(response.encode('utf-8'))
        sock.send(('Hello! %s'%data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.'%addr)

if __name__=="__main__":
    test1()