import asyncio
import ipaddress

from dynamite.message import Message, MessageParser


class TCPDNSProtocol(asyncio.Protocol):

    def __init__(self):
        self.parser = MessageParser()

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        message = self.parser.parse(data)
        response = Message()
        self.transport.write(response.to_bytes())


class UDPDNSProtocol(asyncio.DatagramProtocol):
    pass


def main(host, port):
    local_addr = (ipaddress.ip_address(host).exploded, port)

    loop = asyncio.get_event_loop()
    endpoint = loop.create_datagram_endpoint(UDPDNSProtocol, local_addr=local_addr)
    transport, _ = loop.run_until_complete(endpoint)
    server = loop.run_until_complete(loop.create_server(TCPDNSProtocol, *local_addr))

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    transport.close()
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()
