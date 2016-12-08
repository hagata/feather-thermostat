# Main entry point for the board. Runs on Boot.
import machine
import time
import network
import socket

print("Hello, Micropython!")

# Network setup.
nic = network.WLAN(network.STA_IF)
nic.active(True)
if nic.isconnected() == False:
    print('Please connect to a WiFi network using the commend nic.connect(\'SSid\', \'password\').')

print(nic.ifconfig())
print('Connected : %s' % nic.isconnected())

# Setup URL to connect with

def http_get(url, port):
    _, _, host, path = url.split('/', 3)
    print(url.split('/', 3))
    addr = socket.getaddrinfo(host, port)[0][-1]
    s = socket.socket()
    print('Address: %s', addr)
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    while True:
        data = s.recv(100)
        if data:
            print(str(data, 'utf8'), end='')
        else:
            break

http_get('http://10.0.0.253/', 4000)