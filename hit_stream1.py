import requests
import serial
with serial.Serial('/dev/tty.usbmodem1421', 9600, timeout=1) as ser:
    count = 0
    aggregate = 0
    while 1:
        aggregate += float(ser.readline().decode("ascii", "ignore").strip())
        if count == 5:
            requests.post('http://127.0.0.1:5000/api/send_event/Bob',
                          data=str(aggregate / 5))
            count = 0
            aggregate = 0
        count += 1
