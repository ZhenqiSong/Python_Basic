class CardHolder(object):
    acctlen = 8
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr
    
    def getName(self):
        return self.__name
    
    def setName(self, value):
        value = value.lower().replace(' ', '_')
        self.__name = value 
    name = property(getName, setName)


    def getAge(self):
        return self.__age

    def setAge(self, value):
        if value < 0 or value >150:
            raise ValueError('invalid age')
        else:
            self.__age = value 
    age = property(getAge, setAge)

    def getAcct(self):
        return self.__acct[:3] + '***'
    
    def setAcct(self, value):
        value = value.replace('-', '')
        if len(value) != self.acctlen:
            raise TypeError('invald acct number')
        else:
            self.__acct = value

    def remainGet(self):
        return self.retireage - self.age
    remain = property(remainGet)

def printholder(who):
    print(who.acct, who.name, who.age, who.remain, who.addr, sep=' / ')

if __name__ == '__main__':
    bob = CardHolder('1234-5678', 'Bob Smith', 40, '123 main st')
    printholder(bob)

    bob.name = 'Bob Q. Smith'
    bob.age = 50
    bob.acct = '23-45-67-89'
    printholder(bob)