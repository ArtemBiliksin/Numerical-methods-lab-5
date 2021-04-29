import numpy as np
import matplotlib.pyplot as plt

from matplotlib.widgets import TextBox, CheckButtons
from method import Method, SolutionCauchyProblem


def add_plot(name_class_method, plot, n=5):
    method = name_class_method(n)
    plot.set_xdata(method.x_data)
    plot.set_ydata(method.y_data)
    fig.canvas.draw_idle()


def add_plots(name_class_method, plot_dict, n=5):
    method = name_class_method(n)
    x_data = method.x_data
    y_data_dict = method.y_data_dict
    for plot in plot_dict:
        plot_dict[plot].set_xdata(x_data)
        plot_dict[plot].set_ydata(y_data_dict[plot])
    fig.canvas.draw_idle()


def submit(text):
    if text.isdigit():
        n = int(text)
        if n > 0:
            pass
            add_plots(Method, plot_dict, n)


def on_check_clicked(label):
    global visible_grid
    if label == 'Сетка':
        visible_grid = not visible_grid
    ax.grid(visible_grid)
    fig.canvas.draw_idle()


if __name__ == '__main__':
    fig, ax = plt.subplots()
    fig.canvas.set_window_title('Лабораторная работа №5')
    ax.set(xlim=(-0.1, 1.1), ylim=(0, 0.3), xticks=np.arange(0, 1.1, 0.1), yticks=np.arange(0, 0.31, 0.025))
    ax_solution, = ax.plot([], [], label=SolutionCauchyProblem.name_tex_notation())
    add_plot(SolutionCauchyProblem, ax_solution, 200)

    plot_dict = dict(zip(Method.get_name_methods(), [None for _ in range(len(Method.get_name_methods()))]))
    for plot in plot_dict:
        plot_dict[plot], = ax.plot([], [], label=plot)
    add_plots(Method, plot_dict)

    ax.legend(loc='upper left')

    fig.subplots_adjust(bottom=0.2)

    box_axes = fig.add_axes([0.125, 0.05, 0.3, 0.075])
    text_box = TextBox(box_axes, 'N', initial='5')
    text_box.on_submit(submit)

    visible_grid = True
    ax.grid(linestyle='--', visible=visible_grid)
    check_axes = fig.add_axes([0.525, 0.05, 0.1, 0.075])
    check_box = CheckButtons(check_axes, ['Сетка'], [visible_grid])
    check_box.on_clicked(on_check_clicked)

    plt.show()
