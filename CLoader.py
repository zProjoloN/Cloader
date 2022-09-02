

class CLoad:

    def __init__(self, pfad, row, splitpoint):
        self.pfad = str(pfad) 
        self.row = int(row)
        self.splitpoint = str(splitpoint)

    def load(self):
        var1 = [""]
        pfad = self.pfad
        datei = open(pfad, "r")

        for i in range(self.row):
   
            data = datei.readline()
            data = data.split(";")
            dataa = data[1]
            var1.append(dataa)

        return var1
if __name__ == "__main__":
    main = CLoad("Cloader/Files/config/test_config.txt", 6, ";")
    print(main.load())
