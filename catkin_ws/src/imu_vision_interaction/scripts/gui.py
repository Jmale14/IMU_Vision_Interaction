#!/usr/bin/env python3

import tkinter as Tk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
import time
from PIL import Image, ImageTk

class StateEst:
    def __init__(self):
        self._final = np.array([[6, 6], [6, 6], [6, 6]])
        self._im = np.array([[5, 5], [5, 5], [5, 5]])
        self._imu = np.array([[7, 7], [7, 7], [7, 7]])


CATEGORIES = ['AllenKeyIn', 'AllenKeyOut', 'ScrewingIn', 'ScrewingOut', 'Null']
pos = np.arange(len(CATEGORIES))
imu_state_hist = np.array([4, 4, 4], dtype=np.int)
im_screw_hist = np.zeros((1, 3), dtype=np.int)
imu_pred = np.zeros(5)
state_est = StateEst()

root = Tk.Tk()
root.wm_title("Embedding in Tk")
root.resizable(True, True)

plt.ion()

fig = Figure()#(figsize=(5, 4), dpi=100)
axs = fig.subplots(2, 2)
k = 0


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


def _next_part():
    pass


def update_counter():
    pass


def update_message():
    pass


def update_plot():
    global k
    k = k + 1
    global state_est
    global CATEGORIES
    legend = ['Image', 'IMU', 'Final']
    Titles = ['Total No. Screws', 'Total No. Bolts']
    global axs
    for i in range(0, 2):
        ax = axs[0, i]
        ax.cla()
        ax.plot(state_est._im[:, i] * k)
        ax.plot(state_est._imu[:, i])
        ax.plot(state_est._final[:, i])
        ax.set_ylabel('Estimated Number')
        ax.set_title(Titles[i])
        ax.legend(legend)
        ax.set_ylim(bottom=0)

    ax = axs[1, 0]
    ax.cla()
    ax.bar(pos, imu_pred, align='center', alpha=0.5)
    ax.set_xticks(pos)
    ax.set_xticklabels(CATEGORIES)
    ax.set_ylabel('Confidence')
    ax.set_ylim([0, 1])
    ax.set_title('Current IMU Prediction')

    ax = axs[1, 1]
    ax.cla()
    ax.bar([1, 2], [im_screw_hist[-1, 1], im_screw_hist[-1, 2]], align='center', alpha=0.5)
    ax.set_xticks([1, 2])
    ax.set_xticklabels(['Screws', 'Bolts'])
    ax.set_ylabel('Confidence')
    ax.set_ylim([0, 4])
    ax.set_title('Current image Prediction')

    plt.pause(0.0001)


def update_gui():
    update_plot()
    update_counter()
    update_message()


def setup_gui():
    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    update_gui()
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=0, rowspan=3, columnspan=2, sticky=Tk.W+Tk.E+Tk.N+Tk.S)

    #toolbar = NavigationToolbar2Tk(canvas, root)
    #toolbar.update()
    #canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

    #canvas.mpl_connect("key_press_event", on_key_press(canvas, toolbar))

    message_text = 'Starting...'
    message_obj = Tk.Text(master=root, width=20, height=1, padx=50, pady=20, bg="black")
    message_obj.insert(Tk.INSERT, message_text)
    message_obj.grid(row=3, column=0, columnspan=2, sticky=Tk.W + Tk.E)

    load = Image.open("logo.jpg")
    resized = load.resize((100, 100), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(resized)
    img = Tk.Label(root, image=render, width=200)
    img.image = render
    img.grid(row=0, column=2, sticky=Tk.W+Tk.E+Tk.N+Tk.S)

    counter_text = f"Screws: 0 \n Bolts: 0"
    counter_obj = Tk.Text(master=root, width=20, height=2)
    counter_obj.insert(Tk.INSERT, counter_text)
    counter_obj.grid(row=1, column=2, sticky=Tk.W+Tk.E+Tk.N+Tk.S)

    next_button = Tk.Button(master=root, text="Next Part", command=_next_part, bg="green", padx=50, pady=20)
    next_button.grid(row=2, column=2, sticky=Tk.W+Tk.E+Tk.N+Tk.S)

    quit_button = Tk.Button(master=root, text="Quit", command=_quit, bg="red", padx=50, pady=20)
    quit_button.grid(row=3, column=2, sticky=Tk.W+Tk.E+Tk.N+Tk.S)

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=0)
    root.grid_rowconfigure(0, weight=4)
    root.grid_rowconfigure(1, weight=2)
    root.grid_rowconfigure(2, weight=2)
    root.grid_rowconfigure(3, weight=1)

    while True:
        time.sleep(0.5)
        update_gui()
        canvas.draw()
        root.update_idletasks()
        root.update()


# def on_key_press(event, canvas, toolbar):
#     print("you pressed {}".format(event.key))
#     key_press_handler(event, canvas, toolbar)


setup_gui()
