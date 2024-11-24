# Python Keylogger

This is a simple Python keylogger that sends the captured keystrokes to a remote server. The script listens for keypress events and sends the captured data over a socket connection to the specified remote host and port.

## Requirements

- Python 3.x
- `pynput` library (for capturing keyboard events)

### Install Dependencies

You can install the necessary dependency with pip:

```bash
pip install pynput



How to Use
1. Attacker Machine (Server)
On the attacker's machine (where you are listening for the keystrokes), you need to use Netcat to listen on the specified port and capture the incoming keystrokes.

Run the following command on the attacker machine:

bash
Copy code
nc -lvnp 4444 > keylogs.txt
This will open a listener on port 4444 and save the captured keystrokes to keylogs.txt.

2. Victim Machine (Client)
Run the keylogger script on the victim's machine. It will automatically attempt to establish a connection to the attacker's machine at the specified IP address (REMOTE_HOST) and port (REMOTE_PORT).

bash
Copy code
python keylogger.py
Once the script is running, it will capture keystrokes and send them to the attacker's machine.

Keylogger Behavior
The keylogger captures both regular and special keys (e.g., Enter, Space, Esc).
It continues running in the background, sending keystrokes to the attacker machine until the Esc key is pressed.
Pressing Esc will stop the keylogger and close the socket connection.
Security Warning
This script is intended for educational and ethical hacking purposes only. Do not use it for malicious activities. Always obtain explicit permission before testing or deploying keyloggers or similar software on any system.

Disclaimer
The author is not responsible for any misuse of this software. Use it at your own risk.


```
