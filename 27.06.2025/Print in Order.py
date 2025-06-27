class Foo:
    is_first_executed=False
    is_second_executed=False
    def __init__(self):
        pass

    def first(self, printFirst):
        printFirst()
        self.is_first_executed=True

    def second(self, printSecond):
        while not self.is_first_executed: continue     
        printSecond()
        self.is_second_executed=True
                      
    def third(self, printThird):
        while not self.is_second_executed: continue
        printThird()
