from linkedlist import TuplesLinkedList

class HashTable:
    def __init__(self,):
        self.internal_list = [None for i in range(127)]

    def hash(self, key):
        totalhash = 0
        for i in range(len(key)):
            for char in key:
                totalhash += ord(char) * (31 ** i)
            return totalhash

    def put(self, key, value):
        bucket_index = hash(key) % 127
        index = bucket_index
        stop = False
        while not stop:
            if self.internal_list[index] is None:
                self.internal_list[index] = (key, value)
                stop = True
            else:
                index += bucket_index % 17




    def get(self, key):
        counter = hash(key) % 127
        while self.internal_list[counter][0] != key:
            hash2 = counter % 17
        return self.internal_list[counter][1]




