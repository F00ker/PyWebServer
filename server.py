import socket
import os

class http_listener:

    def __init__(self):
        self.request_buffer = ""
        self.serversocket = None
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serversocket.bind(("localhost",8080))

    def get_request_path(self,request_buffer):
        self.request_buffer = request_buffer
        if "GET" in self.request_buffer:
            GET_request = self.request_buffer.split("\n", 1)
            request_PATH = GET_request[0].split(" ", 2)
            return request_PATH

        if "HEAD" in self.request_buffer:
            return [0,"/curious"]


    def listen(self):
        self.serversocket.listen(5)
        while True:
            connection, address = self.serversocket.accept()
            request_buffer = connection.recv(4096)
            if len(request_buffer) > 0:
                try:
                    print request_buffer
                    connection.sendall(get_content(self.get_request_path(request_buffer)))
                    connection.close()
                except Exception as e:
                    connection.send('HTTP/1.0 500 Internal Server Error\r\n')
                    connection.close()
            else:
                break

    def send_reply(self,reply):
        pass


if __name__ == '__main__':

    def get_content(request_PATH):
        try:
            response_buffer = ""
            print os.getcwd()+request_PATH[1]
            with open(os.getcwd()+request_PATH[1], 'r') as requested_file:
                for line in requested_file:
                    print line
                    response_buffer += line
                return response_buffer
        except IOError as e:
            return "404 File Not Found"
        except Exception as e:
            raise

    web_listener = http_listener()
    web_listener.listen()
