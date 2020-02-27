import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


plt.subplots_adjust(left=0.15, bottom=0.15)


x=np.arange(0,100,0.1)
y_l=[]

for i in x:
    fun1=15*i+0
    y_l.append(fun1)



l,=plt.plot(x,y_l)
plt.xlim(0,100)
plt.ylim(-1000,1000)
plt.text(2,1010,'Y=X(Slope) + (Y-Intercept)')


am = plt.axes([0.15, 0.01, 0.75, 0.03])
ac = plt.axes([0.15, 0.05, 0.75, 0.03])
m = Slider(am, 'Slope', -100, 100.0, valinit=15)
c = Slider(ac, 'Y Intercept', -1000, 1000.0, valinit=0)




def update(val):
    slope = m.val
    center = c.val
    l.set_ydata(slope*x+center)

m.on_changed(update)
c.on_changed(update)

plt.show()