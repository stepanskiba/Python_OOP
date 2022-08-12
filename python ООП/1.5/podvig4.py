from random import random, choices

class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


ch = ['Line', 'Rect', 'Ellipse']
elements = []
for _ in range(217):
    cur = choices(ch)
    a, b, c, d = random(), random(), random(), random()
    #print(cur)
    if cur == ['Line']:
        elements.append(Line(a, b, c ,d))
    elif cur == ['Rect']:
        elements.append(Rect(a, b, c, d))
    elif cur == ['Ellipse']:
        elements.append(Ellipse(a, b, c, d))

for elem in elements:
    if isinstance(elem, Line):
        elem.sp = (0, 0)
        elem.ep = (0, 0)

