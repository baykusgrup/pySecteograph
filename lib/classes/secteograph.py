class Secteograph:
    x = 'deneme'

    def __init__(self):
        self.isim = self.x

    def writeInFile(self):
        print(self.x)

    @staticmethod
    def addTodo(start, end, desc, user):
        print('Start: %s End: %s Desc: %s User: %s' %
              (start, end, desc, user))

    @staticmethod
    def deleteTodo(user, start, end, desc):
        print('Start: %s End: %s Desc: %s User: %s' %
              (start, end, desc, user))

    @staticmethod
    def getTodo(user, start, end, desc):
        print('Start: %s End: %s Desc: %s User: %s' %
              (start, end, desc, user))

    def readInFile(self):
        print('Read:' + self.x)
