class Farm(object):
    def __init__(self, v):
        self.value = v
    def show(self):
        print(self.value)
    def getValue(self):
        return self.value
    def setValue(self, v):
        self.value = v
f1 = Farm(LED, 10)
print(f1.getValue())
f1.setValue(20)
print(f1.getValue())