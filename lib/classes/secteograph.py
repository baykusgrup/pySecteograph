from .fileProcessor import FileProcessor


class Secteograph:
    x = 'deneme'

    def __init__(self):
        self.isim = self.x

    def writeInFile(self):
        print(self.x)

    @staticmethod
    def addTodo(start, end, desc, user):
        data = {"ID": "1", "user": user, "desc": desc,
                "start": start, "end": end, "status": "OPEN"}
        fp = FileProcessor()
        fp.write(data)
        # print('Start: %s End: %s Desc: %s User: %s' %
        #       (start, end, desc, user))

    @staticmethod
    def deleteTodo(user, start, end, desc):
        print('Start: %s End: %s Desc: %s User: %s' %
              (start, end, desc, user))

    @staticmethod
    def getTodo(user, start, end, desc):
        fp = FileProcessor()
        fp.read()
        print('Start: %s End: %s Desc: %s User: %s' %
              (start, end, desc, user))

    def readInFile(self):
        print('Read:' + self.x)
