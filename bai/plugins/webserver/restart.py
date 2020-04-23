import os
from os import path


if __name__ == '__main__':
    os.system('sh ' + path.join(path.dirname(path.dirname(path.dirname(path.dirname(__file__)))), 'update.sh'))