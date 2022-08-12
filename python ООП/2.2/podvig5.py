class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    @staticmethod
    def check_size(x):
        return type(x) is int and 0 <= x <= 10_000

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if self.check_size(width):
            self.__width = width
            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if self.check_size(height):
            self.__height = height
            self.show()

    def show(self):
        print(f"{self.__title}: {self.width}, {self.height}")


wnd = WindowDlg('Диалог 1', 100, 50)
wnd.show()
print(wnd.width)
wnd.width = 20
print(wnd.width)