import os
from .http_response import HttpResponse
from .http_status import HttpStatus
from .content_type import ContentType


class FileManager:
    def __init__(self, data_dir):
        self.__data_dir = data_dir

    def get_list_of_files(self):
        try:
            files = self.__list_of_files()
            return HttpResponse(HttpStatus.OK, ContentType.PLAIN, str(files)).build()
        except Exception:
            return HttpResponse(HttpStatus.INTERNAL_SERVER_ERROR, ContentType.PLAIN).build()

    def get_file(self, path):
        try:
            print()
            if len(path.split("/")) > 2:
                return HttpResponse(HttpStatus.FORBIDDEN, ContentType.PLAIN).build()
            filename = path.split("/")[1]
            if filename not in self.__list_of_files():
                return HttpResponse(HttpStatus.NOT_FOUND, ContentType.PLAIN).build()
            with open(self.__data_dir + "/" + filename, "r") as file:
                return HttpResponse(HttpStatus.OK, ContentType.PLAIN, file.read()).build()
        except Exception as e:
            return HttpResponse(HttpStatus.INTERNAL_SERVER_ERROR, ContentType.PLAIN).build()

    def create_file(self, path, body):
        try:
            if len(path.split("/")) > 2:
                return HttpResponse(HttpStatus.FORBIDDEN, ContentType.PLAIN).build()
            filename = path.split("/")[1]
            with open(self.__data_dir + "/" + filename, "w") as file:
                file.write(body)
                if filename not in self.__list_of_files():
                    return HttpResponse(HttpStatus.CREATED, ContentType.PLAIN).build()
                else:
                    return HttpResponse(HttpStatus.OK, ContentType.PLAIN).build()
        except Exception as e:
            return HttpResponse(HttpStatus.INTERNAL_SERVER_ERROR, ContentType.PLAIN).build()

    def __list_of_files(self):
        return [file for file in os.listdir(self.__data_dir) if os.path.isfile(os.path.join(self.__data_dir, file))]


