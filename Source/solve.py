import socket
from hashlib import sha256
from Crypto.Cipher import DES

BS = DES.block_size


def recv_until(s, st):
    tmp = ''
    while st not in tmp:
        tmp += s.recv(1)
    return tmp


def unpad(s):
    l = len(s)
    return s[:l - ord(s[-1])]


while 1:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("52.55.92.145", 22995))
    # s.connect(("127.0.0.1", 22990))
    data = recv_until(s, "???\n")
    # print data
    xx = data[data.index(": ") + 2:data.index("\nSo,")].decode("hex")
    # print xx
    iv = xx[:16].decode("hex")
    ci = xx[16:].decode("hex")
    # ddd=hex(i).lstrip("0x").rjust(4,"0")
    key = sha256(sha256("6461").hexdigest()).hexdigest()[:BS * 2]
    des = DES.new(key.decode("hex"), DES.MODE_CBC, iv)
    challenge = unpad(des.decrypt(ci))
    # print "==>",challenge.encode("hex")
    flag = sha256(challenge).hexdigest()
    s.send(flag + "\n")
    tmp = s.recv(1024)
    if "flag" in tmp:
        print(tmp)
        break
    s.close()
