import random
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import ticker

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
    columns = 4
    rows = 5
    odf_df = pd.read_csv("ODF_Test-sessions.csv")
    odf_df_notnull = odf_df.fillna(20)
    task_df = odf_df_notnull[['Task 1','Task 2','Task 3','Task 4']]
    odf_arr = []
    odf_arr.append(task_df['Task 1'].to_numpy(dtype=float))
    odf_arr.append(task_df['Task 2'].to_numpy(dtype=float))
    odf_arr.append(task_df['Task 3'].to_numpy(dtype=float))
    odf_arr.append(task_df['Task 4'].to_numpy(dtype=float))
    print(odf_arr[0])
    m1 = task_df.mean(axis=0)
    st1 = task_df.std(axis=0)
    fig, ax = plt.subplots()
    bp = ax.boxplot(odf_arr, showmeans=True)

    for i, line in enumerate(bp['medians']):
        x, y = line.get_xydata()[1]
        text = ' μ={:.2f}\n σ={:.2f}'.format(m1[i], st1[i])
        ax.annotate(text, xy=(x, y))

    plt.ylabel('Time (sec)')
    plt.title('Box plot of average time per task')
    plt.show()


main()
