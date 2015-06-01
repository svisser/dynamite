import enum


class Opcode(enum.IntEnum):
    QUERY = 0
    IQUERY = 1
    STATUS = 2


class ResponseCode(enum.IntEnum):
    NO_ERROR = 0
    FORMAT_ERROR = 1
    SERVER_ERROR = 2
    NAME_ERROR = 3
    NOT_IMPLEMENTED = 4
    REFUSED = 5


class Message:

    def to_bytes():
        return b''


class MessageParser:

    def parse(self, data):
        return Message()
