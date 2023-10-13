class ClassDictionary():

    def __init__(self):
        fileClassi = open("classi.txt","r")
        i = 0
        self.classes = {}

        while True:
            riga  = fileClassi.readline()
            if riga == "":
                break
            self.classes[i] = riga.split('\n')[0]
            i +=1
            
    
        fileClassi.close()

    def get(self):
        return self.classes
    
    def IndexList(self):
        return list(self.classes.keys())
    
    def LabelList(self):
        return list(self.classes.values())