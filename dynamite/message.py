import enum


class OPCODE(enum.IntEnum):
    QUERY = 0
    IQUERY = 1
    STATUS = 2


class RCODE(enum.IntEnum):
    NO_ERROR = 0
    FORMAT_ERROR = 1
    SERVER_ERROR = 2
    NAME_ERROR = 3
    NOT_IMPLEMENTED = 4
    REFUSED = 5


class CLASS(enum.IntEnum):
    IN = 1
    CS = 2
    CH = 3
    HS = 4


class QCLASS(enum.IntEnum):  # + CLASS
    ANY = 255


class TYPE(enum.IntEnum):
    A = 1
    NS = 2
    MD = 3
    MF = 4
    CNAME = 5
    SOA = 6
    MB = 7
    MG = 8
    MR = 9
    NULL = 10
    WKS = 11
    PTR = 12
    HINFO = 13
    MINFO = 14
    MX = 15
    TXT = 16


class QTYPE(enum.IntEnum):  # + TYPE
    AXFR = 252
    MAILB = 253
    MAILA = 254
    ANY = 255


class Message:

    @classmethod
    def parse(cls, data):
        return None

    def to_bytes(self):
        return b''

