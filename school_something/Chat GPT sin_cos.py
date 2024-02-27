import math
import tkinter as tk

class SinCosSimulator(tk.Canvas):
    def __init__(self, parent, width, height, scale=50):
        super().__init__(parent, width=width, height=height)
        self.scale = scale
        self.draw_axes()
        self.draw_wave('sin', 'blue')
        self.draw_wave('cos', 'red')

    def draw_axes(self):
        x0, y0 = self.scale, self.scale
        x1, y1 = self.winfo_width()-self.scale, self.winfo_height()-self.scale
        self.create_line(x0, y0, x1, y0, arrow=tk.LAST)
        self.create_line(x0, y0, x0, y1, arrow=tk.LAST)
        for x in range(x0, x1, self.scale):
            self.create_line(x, y0-5, x, y0+5)
        for y in range(y0, y1, self.scale):
            self.create_line(x0-5, y, x0+5, y)

    def draw_wave(self, func, color):
        x0, y0 = self.scale, self.scale
        x1, y1 = self.winfo_width()-self.scale, self.winfo_height()-self.scale
        points = []
        for x in range(x0, x1+1):
            if func == 'sin':
                y = y0 + self.scale*math.sin((x-x0)/(x1-x0)*2*math.pi)
            elif func == 'cos':
                y = y0 + self.scale*math.cos((x-x0)/(x1-x0)*2*math.pi)
            points.append((x, y))
            self.create_line(points, fill=color)

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Sinus and Cosinus Simulator')
    sim = SinCosSimulator(root, 500, 300)
    sim.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
