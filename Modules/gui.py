import tkinter as tk
from tkinter import scrolledtext
import subprocess
import threading

# Create the GUI window
root = tk.Tk()
root.title("TopDroid")
root.geometry("600x400")

# Create the buttons
button1 = tk.Button(root, text="Full Process Run", width=20, bg="blue")
button2 = tk.Button(root, text="Astrominer auto.sh Reload", width=20, bg="green")
button3 = tk.Button(root, text="Share Android Screen", width=20, bg="orange")
button4 = tk.Button(root, text="Install New Version of AstroMiner", width=20, bg="red")

# Create the text area
text_area = scrolledtext.ScrolledText(root, width=60, height=20)

# Define the button callbacks
def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    for line in process.stdout:
        text_area.insert(tk.END, line)
    process.wait()

def button1_clicked():
    threading.Thread(target=run_command, args=(["python", "process.py"],)).start()

def button2_clicked():
    threading.Thread(target=run_command, args=(["python", "miner/auto.sh_CONFIG_RUN.py"],)).start()

def button3_clicked():
    threading.Thread(target=run_command, args=(["python", "Open_Android_Screen.py"],)).start()

def button4_clicked():
    threading.Thread(target=run_command, args=(["python", "miner/astrominer.py"],)).start()

# Add the buttons and text area to the window
button1.pack(pady=10)
button2.pack(pady=10)
button3.pack(pady=10)
button4.pack(pady=10)
text_area.pack(pady=10)

# Set the button callbacks
button1.config(command=button1_clicked)
button2.config(command=button2_clicked)
button3.config(command=button3_clicked)
button4.config(command=button4_clicked)

# Start the GUI event loop
root.mainloop()
