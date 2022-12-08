import kivy
from kivy.app import App
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.graph import Graph, LinePlot
import numpy as np


class MainApp(App):

    def build(self):
        return MainGrid()


class MainGrid(BoxLayout):

    zoom = NumericProperty(1)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.samples = 512
        self.zoom = 1
        self.graph = Graph(y_ticks_major=0.5,
                           x_ticks_major=0.5*np.pi,
                           border_color=[0, 1, 1, 1],
                           tick_color=[0, 1, 1, 0.7],
                           x_grid=True, y_grid=True,
                           xmin=-2*np.pi, xmax=2*np.pi,
                           ymin=-1.0, ymax=1.0,
                           draw_border=True,
                           x_grid_label=True, y_grid_label=True)

        self.children[0].add_widget(self.graph)
        self.plot_x = np.linspace(-2*np.pi, 2*np.pi, self.samples)
        self.plot_y = np.zeros(self.samples)
        self.plot = LinePlot(color=[1, 1, 0, 1], line_width=1.5)
        self.plot2 = LinePlot(color=[1, 0, 0, 1], line_width=1.5)
        self.graph.add_plot(self.plot)
        self.graph.add_plot(self.plot2)
        
        self.plot_y = np.sin(self.plot_x)
        self.plot_y1 = np.cos(self.plot_x)
        self.plot.points = [(self.plot_x[x], self.plot_y[x]) for x in range(self.samples)]
        self.plot2.points = [(self.plot_x[x], self.plot_y1[x]) for x in range(self.samples)]

if __name__ == '__main__':
    MainApp().run()




    