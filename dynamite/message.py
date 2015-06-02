import enum
import random
import struct


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

    def __init__(self, id=None, is_response=False, opcode=OPCODE.QUERY,
                 is_authoritative=False, is_truncated=False,
                 is_recursion_desired=False, is_recursion_available=False,
                 response_code=RCODE.NO_ERROR,
                 questions=None, answers=None, authority=None, additional=None):
        if id is None:
            id = random.randint(0, 2 ** 16 + 1)
        self.id = id
        self.is_response = is_response
        self.opcode = opcode
        self.is_authoritative = is_authoritative
        self.is_truncated = is_truncated
        self.is_recursion_desired = is_recursion_desired
        self.is_recursion_available = is_recursion_available
        self.response_code = response_code
        self.questions = questions or []
        self.answers = answers or []
        self.authority = authority or []
        self.additional = additional or []

    @classmethod
    def parse(cls, data):
        return None

    def to_bytes(self):
        try:
            opcode_value = self.opcode.value
        except AttributeError:
            opcode_value = self.opcode
        try:
            response_code_value = self.response_code.value
        except AttributeError:
            response_code_value = self.response_code

        bits = (
            ((0 if self.is_response else 1) << 15) |
            ((opcode_value) << 11) |
            ((1 if self.is_authoritative else 0) << 10) |
            ((1 if self.is_truncated else 0) << 9) |
            ((1 if self.is_recursion_desired else 0) << 8) |
            ((1 if self.is_recursion_available else 0) << 7) |
            response_code_value
        )
        return struct.pack(
            '!6H', self.id, bits,
            len(self.questions), len(self.answers),
            len(self.authority), len(self.additional),
        )


class Question:

    def __init__(self, name=None, type=None, class_=None):
        self.name = name
        self.type = type
        self.class_ = class_


class ResourceRecord:

    def __init__(self, name=None, type=None, class_=None, ttl=None, data=None):
        self.name = name
        self.type = type
        self.class_ = class_
        self.ttl = ttl
        self.data = data
