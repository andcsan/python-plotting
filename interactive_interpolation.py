from matplotlib import pyplot as plt
import numpy

class LineBuilder:
    def __init__(self, line, points):
        self.line = line
        self.points = points
        self.p = []
        self.cid = line.figure.canvas.mpl_connect('button_press_event', self.mouse_click)

    def mouse_click(self, event):
        print(event)

        if event.inaxes != self.line.axes \
        or not event.dblclick:
            return

        self.p.append([event.xdata, event.ydata])
        self.p.sort()

        pontos = numpy.asarray(self.p)

        self.domain = numpy.arange(-100, 100, 0.1)

        self.points.set_data(pontos[:, 0], pontos[:, 1])
        self.line.set_data(self.domain, [self.interpolacao(i, pontos) for i in self.domain])

        self.line.figure.canvas.draw()
        self.points.figure.canvas.draw()

    def interpolacao(self, x, pontos):
        soma, produto = 0, 1

        if not pontos.any():
            return

        for i in range(len(pontos)):
            produto =1
            for j in range(len(pontos)):
                if j != i:
                    produto = produto * (x - pontos[j, 0])/(pontos[i, 0] - pontos[j, 0])
            soma = soma + pontos[i, 1] * produto

        return soma

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('Clique para criar pontos da curva')
ax.axis([-20, 20, -20, 20])
ax.grid(True)
line, = ax.plot([], 'r-')
points, = ax.plot([], 'ro')
linebuilder = LineBuilder(line, points)
plt.show()
