import socket

#yikes to setting system defaults lile '127..', *users/use-cases
hostname = socket.gethostname()
HOST = socket.gethostbyname(hostname)
PORT = 9000
RESPONSE = b"""\

        """



#TODO Q1: Context Manager. Why/How/When-To?
#By default, socket.socket creates TCP sockets
with socket.socket() as server_sock:

    #Tell the kernel to reuse sockets in TIME_WAIT stage
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

    #And tell the socket what host & port to bind to
    #TODO Q2: Why are 'secrets'/immutable data transferred over the network in Tuples?

    server_sock.bind((HOST, PORT))

    #0 is the num of connections we want the server to have pending before it refuses connections, bcause this will process only one connection at a time & we want to refuse every other connection but ours
    server_sock.listen(0)
    print(f'listening to {HOST} on port {PORT}')

    #without this line, the server listens but doesnt process requests. So the accept() method must be called.
    #Server 'works' at rhis point below.

    client_sock, client_addr = server_sock.accept()
    #TODO Q4:what does server_sock.accept() return?




    

