import unittest
import mock
from unittest.mock import patch

class TestSerialFunctions(unittest.TestCase):
    def test_send_string_to_uart(self):
        # mock the serial library
        with mock.patch('serial.Serial') as mock_serial:
            mock_serial.return_value.write.return_value = None
            send_string_to_uart("/dev/ttyUSB1", "test_string")
            mock_serial.assert_called_once_with("/dev/ttyUSB1", 9600, timeout=1)
            mock_serial.return_value.write.assert_called_once_with(b'test_string')

    def test_read_from_uart(self):
        # mock the serial library
        with mock.patch('serial.Serial') as mock_serial:
            mock_serial.return_value.readline.return_value = b'test_string\r\n'
            read_from_uart("/dev/ttyUSB1")
            mock_serial.assert_called_once_with("/dev/ttyUSB1", 9600, timeout=1)
            mock_serial.return_value.readline.assert_called()

if __name__ == '__main__':
    unittest.main()