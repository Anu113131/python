from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\ASUS\PycharmProjects\pythonProject\Aatdevel\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

#window.geometry("550x340")
window.configure(bg = "#FFFFFF")
width_of_window = 550
height_of_window = 340
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
window.geometry("%dx%d+%d+%d" %(width_of_window, height_of_window, x_coordinate, y_coordinate))
window.overrideredirect(True)
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 340,
    width = 550,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    393.0,
    170.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("Logo.png"))
image_2 = canvas.create_image(
    101.0,
    146.0,
    image=image_image_2
)

canvas.create_text(
    41.0,
    145.0,
    anchor="nw",
    text="Make",
    fill="#000000",
    font=("Inter ExtraBold", 70 * -1)
)

canvas.create_text(
    45.0,
    213.0,
    anchor="nw",
    text="your design",
    fill="#000000",
    font=("Inter Regular", 14 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    209.0,
    174.0,
    image=image_image_3
)
"""
canvas.create_text(
    335.0,
    134.0,
    anchor="nw",
    text="@ Copy Rights\n This Application fully developed for college\n project purpose",
    fill="#A6A6A6",
    font=("Inter Bold", 10 * -1)
)
"""

canvas.create_text(
    335.0,
    134.0,
    anchor="nw",
    text="@ Copy Rights",
    fill="#A6A6A6",
    font=("Inter Bold", 10 * -1)
)
canvas.create_text(
    335.0,
    151.0,
    anchor="nw",
    text="This Application fully developed for college ",
    fill="#A6A6A6",
    font=("Inter Regular", 9 * -1)
)

canvas.create_text(
    333.0,
    163.0,
    anchor="nw",
    text=" project purpose",
    fill="#A6A6A6",
    font=("Inter Regular", 9 * -1)
)
def mainWin():
    window.destroy()
    import index

window.after(3000, mainWin)
window.resizable(False, False)
window.mainloop()
