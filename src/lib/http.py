import socket
from .response import Response
from .http_status import HttpStatus
from .content_type import ContentType
from urllib.parse import urlparse
from .http_method import HttpMethod

BUFFER_SIZE = 1024


class Http:
    def __init__(self, host, port):
        self.__host = host
        self.__port = port

    def start(self):
        # Starts listening
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.bind((self.__host, self.__port))
        except socket.error as e:
            print("Unable to bind to: {0}:{1}".format(self.__host, self.__port))
            exit(1)
        s.listen(1)
        print("Listening on port {0}".format(self.__port))
        try:
            while(True):
                conn, address = s.accept()
                data = conn.recv(BUFFER_SIZE)
                if data is None:
                    break
                conn.sendall(Response(HttpStatus.OK, ContentType.PLAIN, "Empty").build())
                conn.close()
                # print(conn)
                # print(address)
                # print(data)
        except KeyboardInterrupt as e:
            print("Gracefully exiting...")
            s.detach()
            exit(0)
