import os
from .http_response import HttpResponse
from .http_status import HttpStatus
from .content_type import ContentType
class FileManager:
    def __init__(self, data_dir):
        self.__data_dir = data_dir

    def get_list_of_files(self):
        try:
            dirs = os.listdir(self.__data_dir)
            return HttpResponse(HttpStatus.OK, ContentType.PLAIN, str(dirs)).build()
        except Exception:
            return HttpResponse(HttpStatus.INTERNAL_SERVER_ERROR, ContentType.PLAIN).build()

    def get_file(self, path):
        try:
            filename = path.split("/")[1]
            with open(self.__data_dir + "/" + filename, "r") as file:
                return HttpResponse(HttpStatus.OK, ContentType.PLAIN, file.read()).build()
        except Exception as e:
            return HttpResponse(HttpStatus.INTERNAL_SERVER_ERROR, ContentType.PLAIN).build()

    def create_file(self, path, body):
        try:
            filename = path.split("/")[1]
            with open(self.__data_dir + "/" + filename, "w") as file:
                file.write(body)
                return HttpResponse(HttpStatus.CREATED, ContentType.PLAIN).build()
        except Exception as e:
            return HttpResponse(HttpStatus.INTERNAL_SERVER_ERROR, ContentType.PLAIN).build()


