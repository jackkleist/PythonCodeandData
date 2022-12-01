from matplotlib import pyplot as plt
import numpy as np
import csv
import random
from matplotlib import ticker
import pandas as pd

color_num = 5
color = ["#" + ''.join([random.choice('0123456789ABCDEF') for i in range(6)])
         for j in range(color_num)]


class DataLooker:
    def __init__(self, row_storage):
        self.y_max = 0.0
        self.row_storage = row_storage
        self.id_storage = self.make_id()
        self.times_list = self.make_times()
        self.task_list = ["Task 1", "Task 2", "Task 3", "Task 4"]
        self.fig = plt.figure()

    def make_id(self):
        id_store = []
        for row in self.row_storage:
            id_store.append(row.pop(0))
        return id_store

    def make_times(self):
        times = []

        for row in self.row_storage:
            temp_arr = []
            for i in range(2, 14, 3):
                j = row.pop(i)
                if j != "":
                    j = float(j)
                    if j > self.y_max:
                        self.y_max = j
                    temp_arr.append(j)
                else:
                    temp_arr.append(0.0)
            times.append(temp_arr)

        return times

    def print_times(self):
        for row in self.row_storage:
            print(row)

    def time_plot(self):
        j = 0
        ax1 = self.fig.add_subplot(111)
        temp_list = self.times_list.copy()
        for i in self.id_storage:
            ax1.plot(self.task_list, temp_list.pop(0), color=color[j], label=i)
            j += 1
        yticks = ticker.MaxNLocator(17)
        ax1.yaxis.set_major_locator(yticks)
        ax1.set(ylabel="Time (seconds)")
        ax1.set_title("User Time to Complete Each Task")
        plt.legend()
        plt.show()


def main():
    odf_df = pd.read_csv("ODF_Test-sessions.csv")
    print(odf_df)
    #file_obj.close()
    #row_storage.pop(0)
    #plot_maker = DataLooker(row_storage)
    #plot_maker.time_plot()


main()
