import socket
from .response import Response
from .request import Request
from .http_status import HttpStatus
from .content_type import ContentType

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
                self.__handle_request(conn, data)
                # print(conn)
                # print(address)
                print(data)
        except KeyboardInterrupt as e:
            print("Gracefully exiting...")
            s.close()
            exit(0)

    def __handle_request(self, conn, data):
        request = Request(data)
        print(request.get_formatted_request())
        print(request.get_body())
        print(request.get_http_method())
        print(request.get_path())
        # Check http version

        # Check if valid http method (only GET/POST supported)

        # Check if valid path
        conn.sendall(Response(HttpStatus.OK, ContentType.PLAIN, "Empty").build())
        conn.close()
