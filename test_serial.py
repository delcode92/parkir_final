import serial
import time
# /dev/tty.usbserial-1410

ser = serial.Serial('/dev/cu.usbserial-1410', baudrate=9600)
try:
    while True:
        ser.write(b'0')
        print("Trigger GERBANG")
        time.sleep(2)

except KeyboardInterrupt:
    print("\nbunuh")

finally:
    ser.close()