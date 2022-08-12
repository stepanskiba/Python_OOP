class PathLines:
    def __init__(self, *args):
        self.lines = list(args)

    def get_path(self):
        return self.lines

    def add_line(self, line):
        self.lines.append(line)

    def get_length(self):
        s = ((self.lines[0].x)**2 + (self.lines[0].y)**2)**0.5
        for i in range(1, len(self.lines)):
            s += ((self.lines[i - 1].x - self.lines[i].x)**2 + (self.lines[i - 1].y - self.lines[i].y)**2)**0.5
        return s


class LineTo:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


