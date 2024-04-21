import serial
import time

SERIAL_PORT = '/dev/ttyUSB0'  # Use your sensor's actual serial port
BAUD_RATE = 9600
OUTPUT_FILE = '/home/biqu/sds011_data.txt'  # Specify the path to the output file

def process_frame(frame):
    if frame[0] == int('AA', 16) and frame[-1] == int('AB', 16):
        pm_2_5 = (frame[3] * 256 + frame[2]) / 10.0
        pm_10 = (frame[5] * 256 + frame[4]) / 10.0
        return pm_2_5, pm_10
    else:
        return None

def write_to_file(pm_2_5, pm_10):
    with open(OUTPUT_FILE, 'w') as file:
        file.write(f"PM2.5={pm_2_5} PM10={pm_10}")

def read_from_sensor():
    with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
        data = ser.read(10)
        if len(data) == 10:
            pm_values = process_frame(data)
            if pm_values:
                write_to_file(*pm_values)

if __name__ == '__main__':
    while True:
        read_from_sensor()
        time.sleep(2)  # Adjust the sleep time as needed

