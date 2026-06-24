class Students:
    def __init__(self, name, branch, rno):
        self.sname = name
        self.sbranch = branch
        self.srno = rno
    @property
    def from_branch(self):
        return self.sbranch
    @from_branch.setter
    def from_branch(self, branch):
        self.sbranch = branch
    @from_branch.deleter
    def from_branch(self):
        self.branch = None

s1 = Students("Alice", "CSO", 101)
print(s1.sbranch)
s1.from_branch = "CSEIOT"
print(s1.branch)
del s1.from_branch
print(s1.branch)