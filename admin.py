def init():
   global admin,conn,addr
   import socket
   admin=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   admin.bind(("127.0.0.1",5555))
   admin.listen(3)
   print("Waiting For Connection...")
   conn,addr=admin.accept()
   print("new connection")
init()
while True:
   try:
      conn.send(str.encode(input("$ ")))
      m=conn.recv(4096).decode("ascii").replace('\\\n',"\n")
      if len(m)!=0:
         print(m)
      else:
         print("empty")
   except:
      for x in [conn,admin]:
          x.close()
      init()
      print("initialized!")
