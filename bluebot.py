import socket

class BlueBot:
    def __init__(self, mac):
        self.mac = mac
        self.channel = 6
        self.moves = b''

    def forward(self):
        self.moves = self.moves + b'\x04'
    
    def back(self):
        self.moves = self.moves + b'\x05'

    def left(self):
        self.moves = self.moves + b'\x06'

    def right(self):
        self.moves = self.moves + b'\x07'

    def softLeft(self):
        self.moves = self.moves + b'\x08'

    def softRight(self):
        self.moves = self.moves + b'\x09'

    def hardLeft(self):
        self.moves = self.moves + b'\x0a'

    def hardRight(self):
        self.moves = self.moves + b'\x0b'

    def start(self):
        command = b'\x82\x11' + self.moves + b'\x01'
        length = bytes([len(command)])
        command = length + command

        sum = 0
        for c in command:
            sum += c
        sum = -(sum & 0xFF)
        sum = bytes([sum & 0xFF])
        
        message = b'\xaa' + command + sum

        s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        s.connect((self.mac, self.channel))
        s.send(message)
        s.close()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.start()
