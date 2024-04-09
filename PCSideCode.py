import serial
import time

BAUD_RATE = 2400
EEPROM_SIZE = 1024
TEXT_LENGTH = 1000
TEXT = "Your text goes here..."  # Provide your text here

def measure_speed(start_time, bytes_transferred):
    elapsed_time = time.time() - start_time
    speed = (bytes_transferred * 8) / elapsed_time  # bits per second
    return speed

def send_text_to_mcu(ser, text):
    bytes_sent = 0
    start_time = time.time()
    for c in text:
        ser.write(c.encode())
        bytes_sent += 1
        speed = measure_speed(start_time, bytes_sent)
        print(f"Transmitting... Speed: {speed:.2f} bits/second", end='\r')
    print("\nText sent successfully.")

def receive_text_from_mcu(ser):
    bytes_received = 0
    start_time = time.time()
    received_text = ""
    while bytes_received < TEXT_LENGTH:
        if ser.in_waiting > 0:
            c = ser.read().decode()
            received_text += c
            bytes_received += 1
            speed = measure_speed(start_time, bytes_received)
            print(f"Receiving... Speed: {speed:.2f} bits/second", end='\r')
    print("\nText received successfully:", received_text)

def main():
    with serial.Serial('COMx', BAUD_RATE, timeout=1) as ser:  # Replace 'COMx' with your serial port
        time.sleep(2)  # Allow some time for Arduino to reset after establishing connection
        send_text_to_mcu(ser, TEXT)
        receive_text_from_mcu(ser)

if __name__ == "__main__":
    main()
