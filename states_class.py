class republic_States:
    def __init__(self):
        self.name = "AP"
        self.area = 52400
        self.latitude = 80
        self.longitude = 90

    def __str__(self):
        return self.name + "\n" + str(self.area)+str(self.latitude)+str(self.longitude)

class reunion_States:
    def __init__(self,name,area,latitude,longitude):
        self.name = name
        self.area = area
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return self.name + "\n" + str(self.area)+str(self.latitude)+str(self.longitude)

s = reunion_States("[Illionis,Washingthon]",4000,80,80)
print(s)
    
