#類別class、物件object
class phone:
    def __init__(self,os,number,is_waterproof):
        self.os = os
        self.number = number
        self.is_waterproof = is_waterproof
    def is_ios(self):
        if self.os == "ios" :
            return  True
        else:
            return False

phone1 = phone("ios",88675755116,True)
print (phone1.is_ios())

