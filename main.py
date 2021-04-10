import numpy as np
import matplotlib.pyplot as plt

from matplotlib.widgets import TextBox, CheckButtons
from method import Method


def calculate_x_data_y_data(n):

    method = Method(n)
    x_data = np.linspace(0, 1, n)
    dict_methods = method.dict_methods
    y_data_dict = dict(zip(dict_methods.keys(), [[0.1] for _ in range(3)]))
    for x in x_data[1:]:
        for method_name in dict_methods:
            y_data_dict[method_name].append(dict_methods[method_name](x, y_data_dict[method_name][-1]))

    return x_data, y_data_dict


def add_solution_plot_to_axes(ax):
    x = np.linspace(0, 1, 200)
    y = np.exp(10 * (x * x * x) - 13.5 * x * x + 4.2 * x) * 0.1
    ax.plot(x, y, label=r'$y(x)=0.1 \cdot e^{10x^3-13.5x^2+4.2x}$')


def add_start_plot_to_axes(ax):

    x_data, y_data_dict = calculate_x_data_y_data(5)
    method_names = y_data_dict.keys()
    g = dict(zip(method_names,[None for _ in range(3)]))
    for method_name in method_names:
        g[method_name], = ax.plot(x_data, y_data_dict[method_name], label=method_name)

    return tuple(g.values())


def submit(text):

    if text.isdigit():
        n = int(text)
        if n > 0:
            x_data, y_data_dict = calculate_x_data_y_data(n)
            y_data = list(y_data_dict.values())
            g = [g1, g2, g3]
            for i in range(3):
                g[i].set_xdata(x_data)
                g[i].set_ydata(y_data[i])
            fig.canvas.draw_idle()


def on_check_clicked(label):
    global check_grid

    if label == 'Сетка':
        check_grid = not check_grid
    ax.grid(check_grid)
    fig.canvas.draw_idle()


fig, ax = plt.subplots()
fig.canvas.set_window_title('Лабораторная работа №5')
add_solution_plot_to_axes(ax)
g1, g2, g3 = add_start_plot_to_axes(ax)
ax.legend(loc='lower left')
fig.subplots_adjust(bottom=0.2)

box_axes = fig.add_axes([0.125, 0.05, 0.3, 0.075])
text_box = TextBox(box_axes, 'N', initial='5')
text_box.on_submit(submit)

check_axes = fig.add_axes([0.525, 0.05, 0.1, 0.075])
check_grid = False
check_box = CheckButtons(check_axes, ['Сетка'], [check_grid])
check_box.on_clicked(on_check_clicked)

plt.show()
