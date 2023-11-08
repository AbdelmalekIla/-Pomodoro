from tkinter import *
import math

# CONSTANTS

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
time_r = None


# TIMER RESET
def reset_timer():
    window.after_cancel(time_r)
    title_label.config(text='TIME', fg=GREEN)
    canvas.itemconfig(timer, text='00:00')
    check_marks.config(text='')
    global reps
    reps = 0


# TIMER MECHANISM
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text='LONG BREAK', fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label['text'] = 'SHORT BREAK'
        title_label['fg'] = f'{PINK}'
    else:
        count_down(work_sec)
        title_label['text'] = 'WORK TIME'


# COUNTDOWN MECHANISM


def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer, text=f'{count_min}:{count_sec}')
    if count > 0:
        global time_r
        time_r = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ''
        session = math.floor(reps / 2)
        for i in range(session):
            marks += "✔"
        check_marks.config(text=marks)


# UI SETUP
window = Tk()
window.title('pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
my_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=my_img)
timer = canvas.create_text(103, 130, text='00:00', font=(FONT_NAME, 35, "bold"), fill='white')
canvas.grid(column=1, row=1)

title_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, 'bold'))
title_label.grid(column=1, row=0)

start_button = Button(text='Start', command=start_timer)
start_button.grid(column=0, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

reset_button = Button(text='Reset', command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
