num = 1


class Server:
    dict_of_server = dict()

    def __init__(self, buffer=None):
        if buffer is None:
            buffer = []
        self.buffer = buffer
        global num
        self.ip = num
        Server.dict_of_server[self.ip] = self
        num += 1

    def send_data(self, data):
        Router.buffer.append(data)

    def get_data(self):
        x = self.buffer
        self.buffer = []
        return x

    def get_ip(self):
        return self.ip


class Router:
    buffer = []
    list_of_server = []

    @staticmethod
    def link(server):
        if server not in Router.list_of_server:
            Router.list_of_server.append(server)

    @staticmethod
    def unlink(server):
        if server in Router.list_of_server:
            Router.list_of_server.remove(server)

    @staticmethod
    def send_data():
        for elem in Router.buffer:
            for x in Router.list_of_server:
                if elem.ip == x.ip:
                    Server.dict_of_server[elem.ip].buffer.append(elem)
        Router.buffer = []




class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip

router = Router()
sv_from = Server()
router.link(sv_from)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
print(Router.list_of_server)
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()
#print(msg_lst_to, msg_lst_from)

#assert msg_lst_from[0].data == "Hi" and msg_lst_to[0].data == "Hello", "данные не прошли по сети, классы не функционируют должным образом"