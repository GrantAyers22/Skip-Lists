class HashTable():
    def __init__(self):
        self.DataStructure = dict()
        self.index = 0
    
    def insertElement(self, x):
        self.DataStructure[self.index] = x
        self.index += 1
    
    def deleteElement(self, x):
        for key, value in dict(self.DataStructure).items():
            if value == x:
                del self.DataStructure[key]
    
    def searchElement(self, x):
        for key, value in dict(self.DataStructure).items():
            if value == x:
                return "Found key " + str(x)
    
    def accessElement(self, index):
        return self.DataStructure[str(index)]
    
    def displayList(self):
        print("*****Hash Table******")
        for key, value in dict(self.DataStructure).items():
            print(str(key) + ": " + str(value), end=" | ")
        print()


