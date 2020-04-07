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
import rospy
from imu_vision_interaction.msg import gui_msg
from std_msgs.msg import Int8


# class StateEst:
#     def __init__(self):
#         self._final = np.array([[6, 6], [6, 6], [6, 6]])
#         self._im = np.array([[5, 5], [5, 5], [5, 5]])
#         self._imu = np.array([[7, 7], [7, 7], [7, 7]])


CATEGORIES = ['AllenKeyIn', 'AllenKeyOut', 'ScrewingIn', 'ScrewingOut', 'Null']
pos = np.arange(len(CATEGORIES))
#imu_state_hist = np.array([4, 4, 4], dtype=np.int)
#im_screw_hist = np.zeros((1, 3), dtype=np.int)

plt.ion()

fig = Figure()
axs = fig.subplots(2, 2)
k = 0
QUIT = False


class GUI:
    def __init__(self):
        self._no_completed = 0
        self._state = 0
        self._msg_timer = time.time()
        self._prt_done = False
        #self._state_est = None
        self._timer_flag = False
        self._sys_stat = 2
        self._state_est_final = np.zeros((1, 2))
        self._state_est_im = np.zeros((1, 2))
        self._state_est_imu = np.zeros((1, 2))
        self._imu_stat = [2, 2, 2, 2]
        self._im_stat = 2
        self._pub = rospy.Publisher('completed_parts', Int8, queue_size=10)
        self._imu_pred = np.zeros(5)
        self._im_pred = np.zeros(2)

        self.root = Tk.Tk()
        self.root.wm_title("IMU and Vision Interaction System")
        self.root.resizable(True, True)
        self.canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=0, rowspan=4, columnspan=2, sticky=Tk.W + Tk.E + Tk.N + Tk.S)

        # toolbar = NavigationToolbar2Tk(canvas, root)
        # toolbar.update()
        # canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

        # canvas.mpl_connect("key_press_event", on_key_press(canvas, toolbar))

        self.message_obj = Tk.Text(master=self.root, width=50, height=2, pady=20)
        self.message_obj.grid(row=4, column=0, columnspan=2)

        load = Image.open("logo.jpg")
        resized = load.resize((100, 100), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(resized)
        self.img = Tk.Label(self.root, image=render, width=200)
        self.img.image = render
        self.img.grid(row=0, column=2, sticky=Tk.W + Tk.E + Tk.N + Tk.S)

        right_width = 25

        self.status_obj = Tk.Text(master=self.root, width=right_width)
        self.status_obj.grid(row=1, column=2)

        self.counter_obj = Tk.Text(master=self.root, width=right_width, height=5)
        self.counter_obj.grid(row=2, column=2)

        self.next_button = Tk.Button(master=self.root, text="Next Part", command=self._next_part, bg="green", padx=50, pady=20)
        self.next_button.grid(row=3, column=2, sticky=Tk.W + Tk.E + Tk.N + Tk.S)

        self.quit_button = Tk.Button(master=self.root, text="Quit", command=self._quit, bg="red", padx=50, pady=20)
        self.quit_button.grid(row=4, column=2, sticky=Tk.W + Tk.E + Tk.N + Tk.S)

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=0)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=3)
        self.root.grid_rowconfigure(2, weight=2)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_rowconfigure(4, weight=1)

    def _quit(self):
        global QUIT
        QUIT = True
        self._state = 11
        rospy.signal_shutdown('Quit Button')
        self.root.quit()     # stops mainloop
        self.root.destroy()  # this is necessary on Windows to prevent
                        # Fatal Python Error: PyEval_RestoreThread: NULL tstate

    def _next_part(self):
        if 2 <= self._state <= 5:
            self._state = 7
            if self._state_est._final[-1, 1] == 0:
                self._state = 8

            if self._state_est._final[-1, 0] == 0:
                self._state = 9
            self._timer_flag = True
            self._msg_timer = time.time()

        elif self._state == 6 | self._timer_flag:
            self._state = 2
            self._no_completed = self._no_completed + 1
            self._timer_flag = False
            self._msg_timer = time.time()
        pass

    def update_counter(self):
        counter_text = f"Screws: 0 \n Bolts: 0 \n \n Completed: {self._no_completed}"
        self.counter_obj.delete("1.0", Tk.END)
        self.counter_obj.insert(Tk.INSERT, counter_text)
        pass

    def update_message(self):
        state_msgs = [f'Starting',  # 0
                      f'Initialising Sensors',  # 1
                      f'Ready to begin part {self._no_completed+1}',  # 2
                      f'Part {self._no_completed+1} still requires {self._state_est_final[-1, 0]} screws and {self._state_est_final[-1, 1]} bolts',  # 3
                      f'Part {self._no_completed+1} still requires {self._state_est_final[-1, 0]} screws',  # 4
                      f'Part {self._no_completed+1} still requires {self._state_est_final[-1, 1]} bolts',  # 5
                      f'This part seems done, press next part or quit button',  # 6
                      f'Part still missing {self._state_est_final[-1, 0]} screws and {self._state_est_final[-1, 1]} bolts \n'
                      f'Press Next Part button again if you''re sure',  # 7
                      f'Part still missing {self._state_est_final[-1, 0]} screws \n'
                      f'Press Next Part button again if you''re sure',  # 8
                      f'Part still missing {self._state_est_final[-1, 1]} bolts \n'
                      f'Press Next Part button again if you''re sure',  # 9
                      f'Sensor error, see status dialogue',  # 10
                      f'Quitting ',  # 11
                      f'Message Error']  # 12

        if (self._state == 0) & ((time.time() - self._msg_timer) > 3):
            self._state = 1

        if (self._state == 2) & ((time.time() - self._msg_timer) > 3):
            self._state = 3

        if 3 <= self._state <= 9:
            if (7 <= self._state <= 9) & (time.time() - self._msg_timer > 2) & self._timer_flag:
                self._state = 3
                self._timer_flag = False

            if 3 <= self._state <= 6:

                if (self._state_est_final[-1, 1] == 0) & (self._state_est_final[-1, 0] == 0):
                    self._state = 6

                if self._state_est_final[-1, 1] == 0:
                    self._state = 4

                if self._state_est_final[-1, 0] == 0:
                    self._state = 5



        self.message_obj.delete("1.0", Tk.END)
        if self._state > len(state_msgs) - 1:
            self._state = len(state_msgs) - 1
        self.message_obj.insert(Tk.INSERT, state_msgs[self._state])
        pass

    def update_status(self):
        IMU_MSGS = ['ERROR', 'Ready', 'Unknown', 'Shutdown', 'Starting', 'Connecting', 'Initialising']
        KINECT_MSGS = ['ERROR', 'Ready', 'Unknown', 'Initialising']
        SYSTEM_MSGS = ['ERROR', 'Ready', 'Setting Up']
        IMU_SYS_MSGS = ['ERROR', 'Ready', 'Setting Up']

        if any((i == 0) for i in self._imu_stat) | (self._im_stat == 0):
            self._sys_stat = 0
            self._state = 10
        elif all((i == 1) for i in self._imu_stat) & (self._im_stat == 1):
            if self._sys_stat != 1:
                self._sys_stat = 1
                self._state = 2
                self._msg_timer = time.time()

        status_text = f"System Status: {SYSTEM_MSGS[self._sys_stat]} \n " \
                      f" \n " \
                      f"Vision System: {KINECT_MSGS[self._im_stat]} \n " \
                      f" \n " \
                      f"IMU System: {IMU_SYS_MSGS[self._imu_stat[3]]} \n " \
                      f"  1: {IMU_MSGS[self._imu_stat[0]]} \n " \
                      f"  2: {IMU_MSGS[self._imu_stat[1]]} \n " \
                      f"  3: {IMU_MSGS[self._imu_stat[2]]} \n "
        self.status_obj.delete("1.0", Tk.END)
        self.status_obj.insert(Tk.INSERT, status_text)
        pass

    def update_plot(self):
        global CATEGORIES
        legend = ['Image', 'IMU', 'Final']
        Titles = ['Total No. Screws', 'Total No. Bolts']
        global axs
        for i in range(0, 2):
            ax = axs[0, i]
            ax.cla()
            ax.plot(self._state_est_im[:, i])
            ax.plot(self._state_est_imu[:, i])
            ax.plot(self._state_est_final[:, i])
            ax.set_ylabel('Estimated Number')
            ax.set_title(Titles[i])
            ax.legend(legend)
            ax.set_ylim(bottom=0)

        ax = axs[1, 0]
        ax.cla()
        ax.bar(pos, self._imu_pred, align='center', alpha=0.5)
        ax.set_xticks(pos)
        ax.set_xticklabels(CATEGORIES)
        ax.set_ylabel('Confidence')
        ax.set_ylim([0, 1])
        ax.set_title('Current IMU Prediction')

        ax = axs[1, 1]
        ax.cla()
        ax.bar([1, 2], self._im_pred, align='center', alpha=0.5)
        ax.set_xticks([1, 2])
        ax.set_xticklabels(['Screws', 'Bolts'])
        ax.set_ylabel('Number')
        ax.set_ylim([0, 4])
        ax.set_title('Current image Prediction')

        plt.pause(0.0001)

    def update_gui(self):
        self.update_plot()
        self.update_counter()
        self.update_status()
        self.update_message()
        self.canvas.draw()
        self.root.update_idletasks()
        self.root.update()

        self._pub.publish(self._no_completed)

    def update_data(self, data):
        self._state_est_final = np.vstack((self._state_est_final, [4 - data.state_est_final[0], 1 - data.state_est_final[1]]))
        self._state_est_im = np.vstack((self._state_est_im, [4 - data.state_est_im[0], 1 - data.state_est_im[1]]))
        self._state_est_imu = np.vstack((self._state_est_imu, [4 - data.state_est_imu[0], 1 - data.state_est_imu[1]]))
        self._imu_stat = data.imu_stat
        self._im_stat = data.kin_stat
        self._imu_pred = data.imu_pred
        self._im_pred = data.im_pred


def listener():
    gui = GUI()
    rospy.init_node('gui_listener', anonymous=True)
    rospy.Subscriber('gui_Data', gui_msg, gui.update_data)
    #rospy.spin()
    while not rospy.is_shutdown():
        gui.update_gui()


if __name__ == '__main__':
    #completed = 0
    listener()
# while not QUIT:
#     time.sleep(0.5)
#     imu_stat = [1, 0, 1, 1]
#     kin_stat = [1]
#     completed = gui.update_gui(imu_stat, kin_stat, state_est)
    #gui._state = gui._state + 1

# def on_key_press(event, canvas, toolbar):
#     print("you pressed {}".format(event.key))
#     key_press_handler(event, canvas, toolbar)
