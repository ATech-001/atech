import tkinter as tk

def create_round_rect(canvas, x1, y1, x2, y2, r, **kwargs):
    points = (
        x1+r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y2-r, x2, y2, x2-r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y1+r, x1, y1
    )
    return canvas.create_polygon(points, smooth=True, **kwargs)

root = tk.Tk()
c = tk.Canvas(root, width=200, height=200, bg="#000")
c.pack()

# shadow
create_round_rect(c, 20, 25, 180, 185, 40, fill="#111")
# main
create_round_rect(c, 20, 20, 180, 180, 40, fill="#333")
# highlight top
create_round_rect(c, 30, 25, 170, 70, 20, fill="#555")

root.after(2000, root.destroy)
root.mainloop()
