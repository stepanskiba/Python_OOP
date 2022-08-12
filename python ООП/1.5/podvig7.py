class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu, *args):
        self.name = name
        self.total_mem_slots = 4
        self.cpu = cpu
        self.mem_slots = list(args)

    def get_config(self):
        conf = []
        conf.append(f'Материнская плата: {self.name}')
        conf.append(f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}')
        conf.append(f'Слотов памяти: {self.total_mem_slots}')
        s = 'Память: '
        for elem in self.mem_slots:
            s = s + str(elem.name) + '-' + str(elem.volume) + ';'
        s = s[:-1:]
        conf.append(s)
        return conf


cp = CPU('проц', 100)
mr1 = Memory('память1', 1024)
mr2 = Memory('память2', 1024)
mb = MotherBoard('материнка', cp, mr1, mr2)
print(mb.get_config())