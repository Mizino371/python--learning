import tkinter as tk

def hide_text():
    canvas.itemconfig(text_item, state='hidden')

def show_text():
    canvas.itemconfig(text_item, state='normal')

# Create the main window
root = tk.Tk()
root.title("Canvas Text Example")

# Create a canvas
canvas = tk.Canvas(root, width=200, height=100)
canvas.pack()

# Create text
text_item = canvas.create_text(100, 50, text="This text will disappear in 5 seconds")

# Schedule the text to be hidden after 5 seconds
root.after(5000, hide_text)

# Optional: Show the text again after 10 seconds
# root.after(10000, show_text)

# Start the event loop
root.mainloop()
