class myclass:
    name=""
    age=""
    gender=""
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def output(self):
        print(self.name,"  ",self.age,"  ",self.gender,"\n")

class childclass(myclass):
    def __init__(self, name, age, gender):
        myclass.__init__(self,name, age, gender)

s1=childclass("tushar",22,"male")
s1.output()