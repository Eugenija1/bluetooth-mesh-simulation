import numpy as np



class FileManager:
    @staticmethod
    def to_matrix():
        with open('file.txt', 'r') as f:


            l = np.array([ line.split() for line in f])
            print (l)


FileManager.to_matrix()