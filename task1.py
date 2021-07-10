class Bottle:
    def __init__(self, capacity, water_amount):
        self.capacity = capacity
        self.water_amount = water_amount
    def fillIn(self, capacity1):
        if capacity1 > self.capacity:
            self.water_amount = self.capacity
        else:
            if water_amount != 0:
                if self.water_amount + capacity1 < self.capacity:
                    self.water_amount += capacity1
                else:
                    self.water_amount = self.capacity
            else:
                if self.capacity > capacity1:
                    self.water_amount = capacity1
                else:
                    self.water_amount = self.capacity
        return self.water_amount
    def empty(self, capacity1):
        if capacity1 > self.water_amount:
            self.water_amount = 0
        else:
            self.water_amount -= capacity1
        return self.water_amount
    def maxCapacity(self):
        return self.capacity
