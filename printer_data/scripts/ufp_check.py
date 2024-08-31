import serial
import time

SERIAL_PORT = '/dev/ttyUSB0'  # Adjust this to your sensor's serial port
BAUD_RATE = 9600

def process_frame(frame):
    # Check start and end bytes
    if frame[0] == int('AA', 16) and frame[-1] == int('AB', 16):
        # Combine the bytes for PM2.5 and PM10 using little-endian format
        pm_2_5 = (frame[3] * 256 + frame[2]) / 10.0
        pm_10 = (frame[5] * 256 + frame[4]) / 10.0
        return pm_2_5, pm_10
    else:
        return None

def read_from_sensor():
    with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
        while True:
            data = ser.read(10)
            if len(data) == 10:
                pm_values = process_frame(data)
                if pm_values:
                    pm_2_5, pm_10 = pm_values
                    print(f"PM 2.5: {pm_2_5:.1f} μg/m³, PM 10: {pm_10:.1f} μg/m³")
                else:
                    print("Invalid frame received")
            else:
                print("Incomplete packet received")
            time.sleep(1)

if __name__ == '__main__':
    read_from_sensor()

