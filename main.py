import matplotlib.pyplot as plt
from feynman import Diagram

fig = plt.figure(figsize=(10., 10.))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)

diagram = Diagram(ax)
diagram.text(.5, 0.9, r'$\beta\ plus\ decay$', fontsize=40)

## 图的左半部分
in1 = diagram.vertex(xy=(.1, .75), marker='')
in2 = diagram.vertex(xy=(.1, .25), marker='')
v1 = diagram.vertex(xy=(.35, .5))
v2 = diagram.vertex(xy=(.65, .5))
in1a = diagram.vertex(xy=(.07, .75), marker='')
in2a = diagram.vertex(xy=(.07, .25), marker='')
in1b = diagram.vertex(xy=(.04, .75), marker='')
in2b = diagram.vertex(xy=(.04, .25), marker='')
v1a = diagram.vertex(xy=(.32, .5), marker='')
v1b = diagram.vertex(xy=(.29, .5), marker='')
#####################################################################
higgsout = diagram.vertex(xy=(.9, .75), marker='')
out1 = diagram.vertex(xy=(.9, .25), marker='')

## in1 是图左上角的顶点，v1是中间曲线的左边点
q1 = diagram.line(v1, in1)
q1a = diagram.line(v1a, in1a)
q1b = diagram.line(v1b, in1b)
## in2 是图右下角的顶点，v1是中间曲线的左边点
q2 = diagram.line(in2, v1)
q2a = diagram.line(in2a, v1a)
q2b = diagram.line(in2b, v1b)
#####################################################################
## 中间的线
wz1 = diagram.line(v1, v2, style='wiggly')
#####################################################################
## 右下角的线
wz2 = diagram.line(v2, out1)
#####################################################################
higgs = diagram.line(higgsout, v2)

# q1.text("q", fontsize=30)
# q2.text(r"$\bar{\mathrm{q}}$", fontsize=30)
# 右边的
diagram.text(.1, .77, "d")
diagram.text(.1, .23, "u")
# 中间的
diagram.text(.07, .77, "u")
diagram.text(.07, .23, "u")
# 左边的
diagram.text(.04, .77, "d")
diagram.text(.04, .23, "d")

# diagram.text(0.5, 0.55, "$Z/W^\pm$", fontsize=30)
# diagram.text(0.69, 0.35, "$Z/W^\pm$", fontsize=30)
diagram.text(.9, .77, '$e^{+}$')
diagram.text(.9, .23, r'$\upsilon_{e}$')
# higgs.text("H", fontsize=30)

diagram.plot()
# plt.show()
plt.savefig('betaPdecay.jpg')
