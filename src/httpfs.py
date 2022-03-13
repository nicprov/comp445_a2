from src.lib.http import Http
from src.lib.http_status import HttpStatus


def main():
    Http("localhost", 8080).start()

if __name__ == "__main__":
    main()