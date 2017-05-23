import socket

s = socket.socket()
host = socket.gethostname()
port = 8888
print host

la = [1, 2, 3]
lb = ["q", "e", "f"]
lc = ["9", 10]
ta = (1, 2, 3)
tb = ("asd", "ASda")
t = zip(la, lb, lc)
print t

print zip(ta, tb)

print zip(la, ta)
a,b,c = zip(la, ta)
print a,b,c