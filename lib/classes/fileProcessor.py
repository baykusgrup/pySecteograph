from pathlib import Path


class FileProcessor:
    path = './test'
    permissions = 'w+'
    fileBuffer = None

    def __init__(self, path='./test', permissions='w+'):
        self.path = path
        self.permissions = permissions
        self.getFile()

    def getFile(self):
        todo_file = Path(self.path)
        if todo_file.is_file():
            self.fileBuffer = open(todo_file, 'a+')
        else:
            self.fileBuffer = open(todo_file, self.permissions)

    def closeFile(self):
        self.fileBuffer = self.fileBuffer.close()

    def write(self, data, force=False):
        try:
            with self.fileBuffer as f:
                # To-do ID -- User -- Description -- StartDate -- EndDate -- Status
                f.write(
                    "{0} {1} {2} {3} {4} {5} \n".format(
                        data['ID'],
                        data['user'],
                        data['desc'],
                        data['start'],
                        data['end'],
                        data['status']
                    )
                )
                # f.write("text\n")
        except IOError as identifier:
            pass

    def read(self, line='all', force=False):
        try:
            with self.fileBuffer as f:
                f.seek(0, 0)
                if line == 'all':
                    lines = f.readlines()
                else:
                    lines = f.readlines()[line]
                    lines = lines.split(',')

        except IOError as identifier:
            pass
        return lines
