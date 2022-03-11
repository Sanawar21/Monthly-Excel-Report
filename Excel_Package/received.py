class Received:

    def __calculate_weight(self):
        return self.bags * self.__weight_per_bag

    def __init__(self, date, name, bags, weight_per_bag = 25, serial = 0):
        self.name = name
        self.date = date
        self.bags = bags
        self.__weight_per_bag = weight_per_bag
        self.weight = self.__calculate_weight()
        self.day = self.extract_day()
        self.serial = serial
        self.folio = '-'
        self.issued = None
        self.balance = 0

    def extract_day(self):
        date = self.date
        lists = date.split('/')
        return float(lists[0])

    def as_list(self):
        return [self.serial,self.date,self.name,self.bags,self.folio,self.weight,'']

    def __str__(self):
        return f"{self.serial},{self.date},{self.name},{self.bags},{self.folio},{self.weight},"

    def __eq__(self, other):
        return self.name == other.name and self.date == other.date and self.bags == other.bags

    def __repr__(self):
        return repr((self.date,self.name,self.bags))

    # def __repr__(self):
    #     return repr([self.serial,self.date,self.name,self.bags,self.folio,self.weight,''])