import numpy as np
import matplotlib.pyplot as plt


def get_xy(hand_data, player_data):
    beta, alpha = np.polyfit(np.log10(player_data), np.log10(hand_data), 1)
    return beta, alpha


def get_main_points(hand_data, player_data):
    alist, blist = [], []
    for i in hand_data:
        b, a = get_xy(i, player_data)

        alist.append(a)
        blist.append(b)
        i.append(a)
        i.append(b)

    return alist, blist


def get_main_plot(alpha, beta):
    plt.scatter(alpha, beta, color="black")


def get_line(xlist, color):
    x = np.array([i[9] for i in xlist])
    y = np.array([i[10] for i in xlist])

    a, b = np.polyfit(x, y, 1)
    plt.plot(x, a*x+b, color=color)


def graph_list(cards, color, label):
    n = 0
    for i in cards:
        if n == 0:
            plt.scatter(i[9], i[10], color=color, label=label)
            n = 1

        else:
            plt.scatter(i[9], i[10], color=color)

    get_line(cards, color=color)


def get_graph(title):
    plt.title(title)
    plt.xlabel("log(α) (Normalized [0-Player] Equity)")
    plt.ylabel("β (Equity Retention)")
    plt.legend()
    plt.show()


def get_axs(ax, plist, title):
    ax.imshow(plist)
    ax.set_title(title)
    ax.xaxis.set_tick_params(labelbottom=False)
    ax.yaxis.set_tick_params(labelleft=False)
    ax.set_xticks([])
    ax.set_yticks([])


def get_data(cards):
    with open("data.txt", "w") as f:
        for i in cards:
            f.write(f"{i[9]}, {i[10]}\n")
