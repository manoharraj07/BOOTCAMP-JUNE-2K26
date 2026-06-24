class Student:
    def __init__(self,name,branch,rno):
        self.Sname=name
        self.Sbranch=branch
        self.Srno=rno
    @classmethod
    def hike(cls):
        return "I am class method..."
    @staticmethod
    def result(fname, lname):
        return f"fname+lname"
    def name(self):
        print(self.Sname)   
    def __repr__(self):
        return f"{self.Sname}, {self.Sbranch}, {self.Srno}"
    def __str__(self):
        return f"{self.Sname}, {self.Sbranch}, {self.Srno}"
S1=Student("xyz","abc","123")
print(S1)

S2=Student("xyz","abc","123")
print(S2)
print(S1.hike())