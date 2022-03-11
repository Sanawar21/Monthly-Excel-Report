class Issued:

    def __init__(self, date, name, folio, issued, serial = 0):
        self.date = date
        self.name = name
        self.folio = folio
        self.weight = 0
        self.issued = issued
        self.day = self.extract_day()+0.1
        self.serial = serial
        self.bags = 0
        self.balance = 0

    def as_list(self):
        return [self.serial,self.date,self.name,'',self.folio,'',self.issued]

    def extract_day(self):
        date = self.date
        lists = date.split('/')
        return float(lists[0])

    def __str__(self):
        return f"{self.serial},{self.date},{self.name},,{self.folio},,{self.issued}"

    def __eq__(self, other):
        return self.date == other.date and self.name == other.name and self.folio == other.folio and\
               self.issued == other.issued

    def __repr__(self):
        return repr((self.date,self.name,self.folio,self.issued))

    # def __repr__(self):
    #     return repr([self.serial,self.date,self.name,'',self.folio,'',self.issued])

if __name__ == '__main__':
    o1 = Issued('1/1/2001','Sanawar',21,100, 1)
    o2 = Issued('2/1/2001','Sanawar S',22,200, 2)

    x = [o1,o2]


    print(type((o1)))