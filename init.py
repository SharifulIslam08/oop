


class myClass:
    age=""
    def student(self,age):
        self.age=age
    def prints(self):
        print (self.age)

tushar=myClass()
tushar.student(22)
tushar.prints()

         
class varsity:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def output(self):
        print("my name is ",self.name )
        print("my age is ", self.age)
        print("\n next student \n\n")

s1=varsity("morshed",22)
s1.output()
s2=varsity("zahid",23)
s1.output()
        
