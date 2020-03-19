import numpy as np
import self as self


class FileManager:
    def to_matrix(self):
        f = open ( 'file.txt' , 'r')
        l = []
        l = np.array([ line.split() for line in f])
        print (l)

FileManager.to_matrix(self)


