import tkinter as tk
import time

# Function to update the time
def update_time():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)  # Update the time every second

# Create the main application window
root = tk.Tk()
root.title("Digital Clock")

# Create and configure the clock display
clock_label = tk.Label(root, font=('calibri', 40, 'bold'), background='purple', foreground='white')
clock_label.pack(anchor='center')

# Start the clock
update_time()

# Run the main event loop
root.mainloop()
