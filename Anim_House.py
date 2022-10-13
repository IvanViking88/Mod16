class Cat:
    def __init__(self, name, breed, gender, age, reg_num, status):
        self.name = name
        self.breed = breed
        self.gender = gender
        self.age = age
        self.reg_num = reg_num
        self.status = status

    def getName(self):
        return self.name
    def getBreed(self):
        return self.breed
    def getAge(self):
        return self.age
    def getGender(self):
        return self.gender
    def getReg_num(self):
        return self.reg_num
    def getStatus(self):
        return self.status
    def Display(self):
        print('Name: ', self.name, '\nGender: ', self.gender, '\nAge:', self.age, '\nBreed: ', self.breed, '\nRegistration Number: ',  self.reg_num, '\nStatus: ', self.status)
