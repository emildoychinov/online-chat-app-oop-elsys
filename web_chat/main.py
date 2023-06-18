from .server import * 

def run():
    srv = SocketServer()
    srv.run()
    #srv2 = SocketServer()
    #print(srv is srv2)
