import json
import matplotlib.pyplot as plt
import socket
import threading
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Tk, Canvas

# Create a new socket object
s = socket.socket()

# Connect to the server on the specified port
s.connect(('localhost', 8080))

# Set the initial values for the x- and y-axes
x = 0
y = []

# Create the main window for the GUI
root = Tk()
root.geometry("600x400")
root.title("CPU Usage")

# Create a canvas to display the live graph
canvas = Canvas(root, width=600, height=400)
canvas.pack()

# Create the figure and axes for the graph
fig, ax = plt.subplots()

# Create a FigureCanvasTkAgg object to represent the figure canvas
canvas_agg = FigureCanvasTkAgg(fig, root)
canvas_agg.draw()

# Define a function that will be called to update the GUI
def update_gui():
    global x
    # Receive the JSON data from the server
    json_str = s.recv(1024).decode()

    # Convert the JSON string to a Python data structure
    data = json.loads(json_str)

    # Get the current CPU usage from the data
    cpu_usage = data["cpu"]

    # Update the x- and y-axes with the new data point
    x += 1
    y.append(cpu_usage)

    # Clear the previous graph and plot the updated data
    ax.clear()
    ax.plot(x, y)

    # Update the graph with the new data
    plt.draw()
    plt.pause(0.05)

    # Create a PhotoImage object from the generated graph
    photo = canvas_agg.get_tk_widget().to_photoimage(fig.canvas.get_renderer())

    # Add the PhotoImage object to the canvas
    canvas.create_image(0, 0, image=photo, anchor="nw")

    # Schedule the update_gui() function to be called again after 0.1 seconds
    root.after(100, update_gui)

# Acquire the GIL
threading.RLock().acquire()

# Start the update_gui() function
update_gui()

# Start the event loop
root.mainloop()
