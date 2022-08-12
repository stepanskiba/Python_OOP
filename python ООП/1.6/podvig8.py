TYPE_OS = 1   # 1 - Windows; 2 - Linux


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:
    def __new__(cls, name, *args, **kwargs):
        if TYPE_OS == 1:
            ans = super().__new__(DialogWindows)
        else:
            ans = super().__new__(DialogLinux)
        ans.name = name
        return ans
