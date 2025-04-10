import serial
import time

SERIAL_PORT = "COM9"  
BAUD_RATE = 115200  # Must match ESP32 Serial.begin()

try:
    # 🔹 Open Bluetooth Serial Connection
    esp = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    time.sleep(2)  # Wait for connection

    print(f"✅ Connected to ESP32 on {SERIAL_PORT}")

    while True:
        # 🔹 Read data from ESP32
        if esp.in_waiting > 0:
            esp_data = esp.readline().decode("utf-8").strip()
            if esp_data == "HAND DETECTED":  # Only print if the message is received
                print(f"📡 ESP32 says: {esp_data}")  # Display detected message

        # 🔹 Exit option
        command = input("Press 'q' to quit: ").strip()
        if command == "q":
            print("❌ Exiting...")
            break

    # 🔹 Close the serial connection
    esp.close()

except serial.SerialException as e:
    print(f"❌ Could not open port {SERIAL_PORT}. Error: {e}")
