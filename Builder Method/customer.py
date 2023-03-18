class InvalidNameException(Exception):
    pass

class InvalidYoeException(Exception):
    pass

class InvalidGradYearException(Exception):
    pass

class Student:
    def __init__(self, builder):
        self.id = builder.id
        self.name = builder.name
        self.yoe = builder.yoe
        self.gradyear = builder.gradyear
        self.psp = builder.psp
        self.batchName = builder.batchName

    @staticmethod
    def builder():
        return Student.Builder()

    def __str__(self):
        return f"Student{{id={self.id}, name='{self.name}', yoe={self.yoe}, gradyear={self.gradyear}, psp={self.psp}, batchName='{self.batchName}'}}"

    class Builder:
        def __init__(self):
            self.id = None
            self.name = None
            self.yoe = None
            self.gradyear = None
            self.psp = None
            self.batchName = None

        def setId(self, id):
            self.id = id
            return self

        def setName(self, name):
            self.name = name
            return self

        def setYoe(self, yoe):
            self.yoe = yoe
            return self

        def setGradyear(self, gradyear):
            self.gradyear = gradyear
            return self

        def setPsp(self, psp):
            self.psp = psp
            return self

        def setBatchName(self, batchName):
            self.batchName = batchName
            return self

        def validate(self):
            if self.name is None:
                raise InvalidNameException("Name is invalid")
            if self.yoe < 1:
                raise InvalidYoeException("Years of experience should be atleast 1")
            if self.gradyear >= 2023:
                raise InvalidGradYearException("Grad year should be 2022 or earlier")

        def build(self):
            self.validate()
            return Student(self)
        

if __name__ == "__main__":
    s= Student.Builder().setId(1).setName("Amit").setGradyear(2022).setYoe(1).build()
    print(s)

