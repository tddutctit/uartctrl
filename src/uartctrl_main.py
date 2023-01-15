import yaml
import serial


def read_commands_from_yaml_v1(file_path):
    with open(file_path, 'r') as file:
        # commands = yaml.load(file, Loader=yaml.SafeLoader)
        commands = yaml.safe_load(file_path)
        for command in commands:
            print("Command:", command)
        subline_cmd = commands[command]
        for subline in subline_cmd:
            print("  Subline:", subline)
    return commands


def read_commands_from_yaml(file_path):
    # Read commands from YAML file
    with open(file_path, 'r') as file:
        commands = yaml.safe_load(file)

    # Iterate through commands
    for command, subline_cmd in commands.items():
        print("Command: {}".format(command))
        # Iterate through subline_cmd of command
        for subline in subline_cmd:
            print("  Subline: {}".format(subline))
    return commands

import time
def send_and_receive_from_uart(port, commands):
    try:
        ser = serial.Serial(port, 115200, timeout=1)
        # for top, command in commands:
        for command, subline_cmd in commands.items():
            print("Command: {}".format(command))
            # Iterate through subline_cmd of command
            for subline in subline_cmd:
                print("DBG, subline_cmd: ", subline)
                ser.write(subline.encode())
                time.sleep(0.5)
                response = ser.readline().decode()
                print("Command sent: {}".format(subline))
                print("Response received: {}".format(response))
        return response
    except serial.serialutil.SerialException:
        print("Error: Unable to open port {}".format(port))


if __name__ == "__main__":
    file_path = "../dbfiles/uart_commands.yml"
    commands = read_commands_from_yaml(file_path)
    port = "/dev/ttyUSB1"
    result = send_and_receive_from_uart(port, commands)
    print(result)
