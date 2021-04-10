import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, CheckButtons
from method import Method


def calculate_x_data_y_data(n):
    m = Method(n)
    x_data = np.linspace(0, 1, n)
    y_data_method_euler = [0.1]
    y_data_method_cauchy = [0.1]
    y_data_method_trapezium = [0.1]

    for x in x_data[1:]:
        y_data_method_euler.append(m.method_euler(x, y_data_method_euler[-1]))
        y_data_method_cauchy.append(m.method_cauchy(x, y_data_method_cauchy[-1]))
        y_data_method_trapezium.append(m.method_trapezium(x, y_data_method_trapezium[-1]))
    return x_data, y_data_method_euler, y_data_method_cauchy, y_data_method_trapezium


def add_solution_plot_to_axes():

    def y_data_solution(x):
        return np.exp(10 * (x * x * x) - 13.5 * x * x + 4.2 * x) * 0.1
    x_data_solution = np.linspace(0, 1, 200)
    y_data_solution = y_data_solution(x_data_solution)
    ax.plot(x_data_solution, y_data_solution, label=r'$y(x)=0.1 \cdot e^{10x^3-13.5x^2+4.2x}$')


def add_start_plot_to_axes():
    global g1, g2, g3
    x_arguments, y_method_euler, y_method_cauchy, y_method_trapezium = calculate_x_data_y_data(5)
    g1, = ax.plot(x_arguments, y_method_euler, label='метод Эйлера')
    g2, = ax.plot(x_arguments, y_method_cauchy, label='метод Коши')
    g3, = ax.plot(x_arguments, y_method_trapezium, label='метод трапеций')


fig, ax = plt.subplots()
add_solution_plot_to_axes()
add_start_plot_to_axes()
ax.grid()
ax.legend(loc='lower left')
fig.subplots_adjust(bottom=0.2)


def submit(text):
    if text.isdigit():
        n = int(text)
        if n > 0:
            x_arguments, y_method_euler, y_method_cauchy, y_method_trapezium = calculate_x_data_y_data(n)
            g1.set_xdata(x_arguments)
            g1.set_ydata(y_method_euler)
            g2.set_xdata(x_arguments)
            g2.set_ydata(y_method_cauchy)
            g3.set_xdata(x_arguments)
            g3.set_ydata(y_method_trapezium)
            plt.draw()


axes_box = fig.add_axes([0.125, 0.05, 0.3, 0.075]) #plt.axes([0.125, 0.05, 0.775, 0.075])
initial_text = '5'
text_box = TextBox(axes_box, 'N', initial=initial_text)
text_box.on_submit(submit)

check_axes = fig.add_axes([0.525, 0.05, 0.1, 0.075])
check_box = CheckButtons(check_axes, ['Сетка'], [True])
check_grid = True


def on_check_clicked(label):
    global check_grid
    if label == 'Сетка':
        check_grid = not check_grid
    ax.grid(check_grid)
    plt.draw()


check_box.on_clicked(on_check_clicked)
plt.gcf().canvas.set_window_title('Лабораторная работа №5')
plt.show()
