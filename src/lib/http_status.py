from enum import Enum


class HttpStatus(Enum):
    OK = ("OK", 200)
    CREATED = ("Created", 201)
    ACCEPTED = ("Accepted", 202)
    NO_CONTENT = ("No Content", 204)
    MOVED_PERMANENTLY = ("Moved Permanently", 301)
    MOVED_TEMPORARILY = ("Moved Temporarily", 302)
    NOT_MODIFIED = ("Not Modified", 304)
    BAD_REQUEST = ("Bad Request", 400)
    UNAUTHORIZED = ("Unauthorized", 401)
    FORBIDDEN = ("Forbidden", 403)
    NOT_FOUND = ("Not Found", 404)
    UNSUPPORTED_MEDIA_TYPE = ("Unsupported Media Type", 415)
    I_AM_A_TEAPOT = ("I'm a teapot", 418)
    INTERNAL_SERVER_ERROR = ("Internal Server Error", 500)
    NOT_IMPLEMENTED = ("Not Implemented", 501)
    HTTP_VERSION_NOT_SUPPORTED = ("HTTP Version Not Supported", 505)

    def __str__(self):
        return self.value[0]

    def __int__(self):
        return self.value[1]


