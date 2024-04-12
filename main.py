import socket


SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8080

server_socket = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server_socket.setblocking(True)

server_socket.bind((SERVER_HOST, SERVER_PORT))

server_socket.listen(10)

print(f"Listening on port {SERVER_PORT} ...")

while True:
    client_socket, client_address = server_socket.accept()
    request = client_socket.recv(1500).decode()
    print(request)
    headers = request.split('\n')
    first_header_componets = headers[0].split()
    http_method = first_header_componets[0]
    path = first_header_componets[1]    

    # RESPONSE SHOULD HAVE THIS TO SEND RESPONSE
    # STATUS LINE -
    # HEADERS 
    # MESSAGE-BODY 
    if http_method == 'GET':
        if path == '/':
            fin = open('index.html')
        elif path == '/book':
            fin  = open('Book.json')
            
        content = fin.read()
        fin.close   
        response = 'HTTP/1.1 200 OK \n\n' + content


    else:
        response = 'HTTP/1.1 405 method not allowed \n\n'
    client_socket.sendall(response.encode())
    client_socket.close()