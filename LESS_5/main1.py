class Thing(object):
    def eat(self):
        print('eating')
    def breathe(self):
        print('breathe')
    def multyply(self):
        print('myltiply')
    def exude(self):
        print('exude')
    def __init__(self,cell):
        self.cell=cell
    def _show_info(self):
        print(self.cell)
class Human(Thing):
    def __init__(self,cell, brain):
        self.brain = brain
        super().__init__(cell)
    def learn_python(self):
        print('learn_python')
    def show_info(self):
        print(self.cell,self.brain)
ameba= Thing('H12hh2')
person= Human('Sasha','sdsd')
print(ameba.cell, person.cell, person.brain)
    