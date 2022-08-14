"""This module provides the class BlueBot to control a TTS BlueBot."""
import socket


class BlueBot:
    """This class allows controlling a TTS BlueBot via Bluetooth with the following commands:
       forward, back, left, right, soft_left, soft_right, hard_left, hard_right.
       Commands are not executed immediately,
       but only when the `when` block is left or when `start` is called.
    """

    def __init__(self, mac):
        """Initialize with the BlueBot's MAC address."""
        self.mac = mac
        self.channel = 6
        self.moves = b''

    def forward(self):
        """Move BlueBot one field forward."""
        self.moves += b'\x04'

    def back(self):
        """Move BlueBot one field backwards."""
        self.moves += b'\x05'

    def left(self):
        """Turn BlueBot left by 90 degrees."""
        self.moves += b'\x06'

    def right(self):
        """Turn BlueBot right by 90 degrees."""
        self.moves += b'\x07'

    def soft_left(self):
        """Turn BlueBot left by 45 degrees."""
        self.moves += b'\x08'

    def soft_right(self):
        """Turn BlueBot right by 45 degrees."""
        self.moves += b'\x09'

    def hard_left(self):
        """Turn BlueBot left by 135 degrees."""
        self.moves += b'\x0a'

    def hard_right(self):
        """Turn BlueBot right by 135 degrees."""
        self.moves += b'\x0b'

    def start(self):
        """Execute prepared commands."""
        command = b'\x82\x11' + self.moves + b'\x01'
        length = bytes([len(command)])
        command = length + command

        checksum = 0
        for byte in command:
            checksum += byte
        checksum = -(checksum & 0xFF)
        checksum = bytes([checksum & 0xFF])

        message = b'\xaa' + command + checksum

        bluetooth_socket = socket.socket(socket.AF_BLUETOOTH,
                                         socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        bluetooth_socket.connect((self.mac, self.channel))
        bluetooth_socket.send(message)
        bluetooth_socket.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.start()
