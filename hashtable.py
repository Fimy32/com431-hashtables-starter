from linkedlist import TuplesLinkedList

class HashTable:
    def __init__(self,):
        self.buckets = [TuplesLinkedList() for i in range(127)]

    def hash(self, key):
        totalhash = ""
        for i in range(len(key)):
            for char in key:
                totalhash += (ord(char) * 31) ^ i
            return totalhash

    # def unhash(self, hash):
    #     totalunhash = ""
    #     for i in range(len(hash)):
    #         for char in hash:
    #             totalunhash += (ord(char) * 31) ^ i



    def put(self, key, value):
        self.buckets[hash(key) % 127].add(key, value)

    def get(self, key):
        for i in range(self.buckets[hash(key) % 127].size):
            total = ""
            for g in range(len(key)):
                total += self.buckets[hash(key) % 127].get(i)[g]
        return total


    # def get(self, key):
    #     for i in range(self.buckets[hash(key) % 127].size):
    #         total = ""
    #         total += self.buckets[hash(key) % 127].get(i)
    #     return total
    #
    # def get(self, key):
    #     self.buckets[hash(key) % 127].find(key)

