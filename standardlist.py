class StandardList():
    def __init__(self):
        self.DataStructure = []
    
    def insertElement(self, x):
        self.DataStructure.append(x)
    
    def searchElement(self, x):
        for item in self.DataStructure:
            if item == x:
                return "Found key " + str(x)
    
    def deleteElement(self, x):
        if x in self.DataStructure:
            self.DataStructure.remove(x)
    
    def accessElement(self, index):
        return self.DataStructure[index]
    
    def displayList(self):
        print("*****Array*****")
        for item in self.DataStructure:
            print(item, end=" ")
        print()