from matplotlib import pyplot as plt
import numpy

class LineBuilder:
    def __init__(self, line):
        self.line = line
        self.xs = list()
        self.ys = list()
        self.domain = numpy.arange(-50, 50, 0.1)
        self.cid = line.figure.canvas.mpl_connect('button_press_event', self.but_press)

    def but_press(self, event):
        print(event)

        if event.inaxes!=self.line.axes \
        or not event.dblclick:
            return

        self.xs.append(event.xdata)
        self.ys.append(event.ydata)
        self.line.set_data(self.xs, self.ys)
        self.line.figure.canvas.draw()

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('Clique para criar pontos das retas')
ax.grid(True)
line, = ax.plot([], 'ro-')
linebuilder = LineBuilder(line)

plt.show()
