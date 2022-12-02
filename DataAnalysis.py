import random
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import ticker
from scipy.stats import f_oneway


def main():
    odf_df = pd.read_csv("ODF_Test-sessions.csv")
    odf_df_notnull = odf_df.fillna(20)
    task_df = odf_df_notnull[['Task 1', 'Task 2', 'Task 3', 'Task 4']]
    odf_arr = []
    odf_arr.append(task_df['Task 1'].to_numpy(dtype=float))
    odf_arr.append(task_df['Task 2'].to_numpy(dtype=float))
    odf_arr.append(task_df['Task 3'].to_numpy(dtype=float))
    odf_arr.append(task_df['Task 4'].to_numpy(dtype=float))
    m1 = task_df.mean(axis=0)
    st1 = task_df.std(axis=0)
    fig, ax = plt.subplots()
    bp = ax.boxplot(odf_arr, showmeans=True, patch_artist=True)

    for i, line in enumerate(bp['medians']):
        x, y = line.get_xydata()[1]
        text = ' μ={:.2f}\n σ={:.2f}'.format(m1[i], st1[i])
        ax.annotate(text, xy=(x, y))

    plt.ylabel('Time (sec)')
    plt.title('Box plot of average time per task')
    plt.savefig("./boxplot.png")
    user1 = task_df.iloc[0]
    user2 = task_df.iloc[1]
    user3 = task_df.iloc[2]
    user4 = task_df.iloc[3]
    user5 = task_df.iloc[4]
    print(f_oneway(user1, user2, user3, user4, user5))
    print(f_oneway(odf_arr[0], odf_arr[1], odf_arr[2], odf_arr[3]))


main()
