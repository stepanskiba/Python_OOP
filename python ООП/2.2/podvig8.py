class TreeObj:
    def __init__(self, indx, value=None):
        self.indx = indx
        self.value = value
        self.__left = None
        self.__right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, l):
        self.__left = l

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, r):
        self.__right = r

class DecisionTree:
    @classmethod
    def predict(cls, root, x):
        pass

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        if node:
            if left:
                node.left = obj
            else:
                node.right = obj
        return obj

    @classmethod
    def predict(cls, root, x):
        obj = root
        while obj:
            obj_next = cls.get_next(obj, x)
            if obj_next is None:
                break
            obj = obj_next

        return obj.value

    @classmethod
    def get_next(cls, obj, x):
        if x[obj.indx] == 1:
            return obj.left
        return obj.right



root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(3, "будет программистом"), v_11)
DecisionTree.add_obj(TreeObj(4, "будет кодером"), v_11, False)
DecisionTree.add_obj(TreeObj(5, "не все потеряно"), v_12)
DecisionTree.add_obj(TreeObj(6, "безнадежен"), v_12, False)

x = [1, 1, 0]
res = DecisionTree.predict(root, x) # будет программистом