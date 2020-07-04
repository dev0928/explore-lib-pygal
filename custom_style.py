import pygal
from pygal.style import TurquoiseStyle

chart = pygal.StackedLine(fill=True, interpolate='cubic', style=TurquoiseStyle, explicit_size=20)
chart.add('A', [1, 3,  5, 16, 13, 3,  7])
chart.add('B', [5, 2,  3,  2,  5, 7, 17])
chart.add('C', [6, 10, 9,  7,  3, 1,  0])
chart.add('D', [2,  3, 5,  9, 12, 9,  5])
chart.add('E', [7,  4, 2,  1,  2, 10, 0])
chart.render_in_browser()