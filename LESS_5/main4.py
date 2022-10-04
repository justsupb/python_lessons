class Phone():
    def __init__(self,display,camera,corpus,battery,CPU):
        self.display=display
        self.camera=camera
        self.corpus=corpus
        self.battery=battery
        self.CPU=CPU
    def __del__(self): 
        print('object was deleted')
    def call(self):
        print('phone is calling')
    def show_info(self):
        print(self.display,self.camera,self.corpus,self.battery,self.CPU,sep="|")
Iphone14 = Phone('Retina','sony 64 mp','glass', '5000mah','A15 bionic')
# Iphone14.call()
# del Iphone14
# print(Iphone14.camera)
Redmi = Phone('good display','4 in a raw','nice','6000mah','Queen')
Redmi.show_info()
arr=[Redmi,Iphone14]
print(arr[1].camera)