import tkinter

canvas = tkinter.Canvas(width=1500, height=900)
canvas.pack()

canvas.create_rectangle(10, 10, 500, 500)

canvas.mainloop()
