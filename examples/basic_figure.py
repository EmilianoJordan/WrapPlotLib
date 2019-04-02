"""
Created: 3/20/2019
Author: Emiliano Jordan,
        https://github.com/EmilianoJordan
        https://www.linkedin.com/in/emilianojordan/,
        Most other things I'm @emilianojordan
"""
import matplotlib.pyplot as plt

from wrapplotlib.figures import BaseFigure

x = [0, 1, 2]
y = [0, 1, 2]

f = BaseFigure()

a = f.add_subplot(1,1,1)
f.title = "test"
a.plot(x,y)
a.set_title("testies")
f.canvas.draw()
plt.show()
