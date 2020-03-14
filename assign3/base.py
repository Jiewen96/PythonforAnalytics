import os
import glob


def hello():
    print('Hello World!')
class salad():
    def __init__(self):
        self.path = ''
        
        
    def read(self, path, salad, n_items):
        self.path = path
        assert len(salad) == len(n_items), 'Not cool!'
        for k in range(len(salad)):
            for j in range(n_items[k]):
                file_name = salad[k] + "0" + str(j) +'.salad'
                f = open(os.path.join(self.path, file_name), 'w+')
                f.close()

    def write(self, path):
        files = glob.glob(os.path.join(path, '*.salad'))
        ret = {}
        for file in files:
            file_name = file.split('/')[-1]
            strip_ext = file_name.split('.')[0]
            ingredient = ''.join([i for i in strip_ext if not i.isdigit()])
            if ingredient not in ret:
                ret[ingredient] = 1
            else:
                ret[ingredient] += 1
        return ret


