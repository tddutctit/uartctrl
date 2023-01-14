import threading
import serial

port = "/dev/ttyUSB1"
cmd_string = "xvsr 44a30004\r"  # fpga rev reg


def open_uart_port(uart_port=port, baudrate=115200):
    try:
        ser = serial.Serial(uart_port, baudrate)
        return ser
    except serial.SerialException as e:
        print(e)
        return None


ser = open_uart_port()
if ser is None:
    print("Error: UART port not available")
else:
    print("UART port open successfully")

# Reading


def read_from_uart(port):
    try:
        ser = serial.Serial(port, 115200, timeout=1)
        while True:
            data = ser.readline().decode()
            if data:
                print("RxData: ")
                print(data)
    except serial.serialutil.SerialException:
        print("Error: Unable to open port {}".format(port))


def start_reading_thread():
    # port = "/dev/ttyUSB1"
    thread = threading.Thread(target=read_from_uart, args=(port,))
    thread.start()

# Sending
import serial
import threading
import time

def send_string_to_uart(port, string):
    try:
        ser = serial.Serial(port, 115200, timeout=1)
        while True:
            ser.write(string.encode())
            print("Data sent: {}".format(string))
            time.sleep(3)
    except serial.serialutil.SerialException:
        print("Error: Unable to open port {}".format(port))

def send_to_uart(ser, string):
    if ser is None:
        print("Error: UART port not open")
    else:
        ser.write(string.encode())


ser = open_uart_port()
if ser is None:
    print("Error: UART port not available")
else:
    send_to_uart(ser, "read 10000\a")
    ser.close()


def main():
    ser = open_uart_port()
    if ser is None:
        print("Error: UART port not available")
    else:
        print("UART port open successfully")
        port = "/dev/ttyUSB1"
    thread = threading.Thread(target=read_from_uart, args=(port,))
    thread.start()
    print("Send read rev cmd: ", cmd_string)
    send_to_uart(ser, cmd_string)
    print("Done");

    thread = threading.Thread(target=send_string_to_uart, args=(port, cmd_string))
    thread.start()
    # sleep(5)
    # ser.close()


if __name__ == "__main__":
    main()
