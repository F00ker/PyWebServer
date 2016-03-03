import socket
import os

class http_listener:

    def __init__(self):
        self.request_buffer = ""
        self.serversocket = None
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serversocket.bind(("localhost",8080))
        self.connection = None

    def get_request_path(self,request_buffer):
        self.request_buffer = request_buffer
        if "GET" in self.request_buffer:
            GET_request = self.request_buffer.split("\n", 1)
            request_PATH = GET_request[0].split(" ", 2)
            return request_PATH[1]

        if "HEAD" in self.request_buffer:
            return [0,"/curious"]

    def get_content(self,request):
        try:
            self.response_buffer = ""
            with open(os.getcwd()+request, 'r') as requested_file:
                for line in requested_file:
                    print line
                    self.response_buffer += line
                return self.response_buffer
        except IOError as e:
            return "404 File Not Found"
        except Exception as e:
            self.connection.sendall('HTTP/1.0 500 Internal Server Error\r\n')
            self.connection.close()

    def listen(self):
        self.serversocket.listen(5)
        while True:
            self.connection, address = self.serversocket.accept()
            request_buffer = self.connection.recv(4096)
            if len(request_buffer) > 0:
                try:
                    self.connection.sendall(self.get_content(self.get_request_path(request_buffer)))
                    self.connection.close()
                except Exception as e:
                    self.connection.sendall('HTTP/1.0 500 Internal Server Error\r\n')
                    self.connection.close()
            else:
                break


if __name__ == '__main__':

    web_listener = http_listener()
    web_listener.listen()
