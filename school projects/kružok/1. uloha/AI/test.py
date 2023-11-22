import tkinter as tk
root = tk.Tk()
# def on_button_click():
    
c=tk.Canvas(root, width=1500,height=1000)
c.pack()

but_rozne = tk.Button(c,text="rôzne")
but_rozne_okno = c.create_window(150,150,anchor=tk.CENTER,window=but_rozne)

but_rovn = tk.Button(c,text="rôzne")
but_rovn_okno = c.create_window(150,300,anchor=tk.CENTER,window=but_rovn,)
c.mainloop()

