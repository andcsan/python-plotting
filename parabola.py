import math
import numpy
from matplotlib import pyplot as plt

class Parabola(object):
    def __init__(self, x, y):
        global g

        self.v0x = x
        self.v0y = y
        self.v0 = math.sqrt(pow(self.v0x, 2) + pow(self.v0y, 2))

        self.time = self.v0y / g * 2

        self.interval = numpy.linspace(0, self.time, 100)
        self.interval = list(self.interval)

        self.domain = [self.v0x * i for i in self.interval]
        self.image  = [self.v0y * i + (-g) * i**2 / 2 for i in self.interval]

class Uservel(object):
    def __init__(self):
        self.figure = plt.figure()

        self.ax = self.figure.add_subplot(111)
        self.ax.set_title('pressione para criar a parabola')
        self.ax.grid(True)
        self.ax.set_xlim([-100, 100])
        self.ax.set_ylim([-100, 100])

        self.x = 0
        self.y = 0

        self.line,  = self.ax.plot(0, 0, 'ro-')
        self.vline, = self.ax.plot(0, 0, 'go-')
        self.xline, = self.ax.plot(0, 0, 'bo-')
        self.yline, = self.ax.plot(0, 0, 'bo-')
        self.pline, = self.ax.plot(0, 0, 'k-')

        self.figure.canvas.mpl_connect('button_press_event', self.update_location)
        self.figure.canvas.mpl_connect('button_release_event', self.update_location)
        self.figure.canvas.mpl_connect('motion_notify_event', self.update_location)

    def update_location(self, event):
        if event.button == 1 and event.inaxes != None:
            self.x = event.xdata
            self.y = event.ydata

            self.parabola = Parabola(self.x, self.y)

            self.line.set_data([self.x, 0], [self.y, 0])
            self.vline.set_data([0, -self.x], [0, -self.y])
            self.xline.set_data([-self.x, 0], [0, 0])
            self.yline.set_data([0, 0], [-self.y, 0])
            self.pline.set_data(self.parabola.domain, self.parabola.image)
        else:
            self.x = 0
            self.y = 0

            self.line.set_data(0, 0)
            self.vline.set_data(0, 0)
            self.xline.set_data(0, 0)
            self.yline.set_data(0, 0)
            self.pline.set_data(0, 0)

        self.line.figure.canvas.draw()

g = 9.80665
run = Uservel()
plt.show()
