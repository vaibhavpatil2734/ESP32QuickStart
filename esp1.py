import serial
import time

# Update with the correct COM port (check Device Manager)
SERIAL_PORT = "COM9"  # Example: COM5 (Windows) or /dev/rfcomm0 (Linux)
BAUD_RATE = 9600  # Must match ESP32 Serial.begin() baud rate

try:
    # Open Bluetooth Serial Connection
    esp = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    time.sleep(2)  # Wait for connection

    print(f"Connected to ESP32 on {SERIAL_PORT}")

    while True:
        command = input("Enter 1 to turn ON LED, 0 to turn OFF, q to quit: ").strip()

        if command == "q":
            print("Exiting...")
            break
        elif command in ["1", "0"]:
            esp.write(command.encode())  # Send command to ESP32
            print(f"Sent: {command}")
        else:
            print("Invalid input. Enter 1 or 0.")

    esp.close()  # Close the serial connection

except serial.SerialException as e:
    print(f"Could not open port {SERIAL_PORT}. Error: {e}")
