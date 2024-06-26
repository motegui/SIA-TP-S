import numpy as np
import matplotlib.pyplot as plt


def level_methods_bar_graph(data, miny, maxY, groupLabels, barLabels, barColors, xLabel, yLabel, title):
    fig, ax = plt.subplots()
    bar_width = 0.175
    bar_positions = np.arange(len(data))

    for bar_list, (label, color) in enumerate(zip(barLabels, barColors)):
        success_data = [sublist[bar_list] for sublist in data]
        ax.bar(
            bar_positions + bar_list * bar_width,
            success_data,
            width=bar_width,
            label=label,
            color=color
        )
    ax.set_xlabel(xLabel)
    ax.set_ylabel(yLabel)
    ax.set_title(title)
    ax.set_xticks([pos + bar_width * 1.5 for pos in bar_positions])
    ax.set_xticklabels(groupLabels)
    handles = []
    for c in barColors: handles.append(plt.Rectangle((0, 0), 1, 1, color=c))
    ax.legend(handles, barLabels)

    plt.ylim(miny, maxY)
    plt.show()


def average_and_variance_graph(means, variances, labels, title, yLabel):
    x = np.arange(len(labels))
    width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(x, means, width, yerr=variances, capsize=5)

    ax.set_ylabel(yLabel)
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    plt.show()
