#from abc import ABCMeta, abstractmethod

#class Terran(metaclass = ABCMeta) :  #추상화, 은닉화, 캡슐화, 다형성
#    #다형성 : 명령하나로 다양하게 움직이도록, 인자설계
#    def __init__(self, name) :
#        self.name = name
#    @abstractmethod
#    def attack(self) :
#        pass

#class Tank(Terran) :
#    def __init__(self, name, damage) :
#        super().__init__(name)
#        self.demage = damage
#    def attack(self) :
#        print("빵야")

#class Marine(Terran) :
#    def __init__(self, name, hp) :
#        super().__init__(name)
#        self.hp = hp
#    def attack(self) :
#        print("마린쏨")

#def Attack(terran) :
#    terran.attack()

#t1 = Tank("tank", 0)
#t2 = Marine("marine", 10)

#tlist = [Tank("tank1", 0),Tank("tank2", 0), Marine("marine1", 10)]
#for item in tlist :
#    Attack(item)

#Attack(t1)
#Attack(t2)

class MyList(list) :
    name = ""
    def __init__(self, name) :
        super().__init__([])
        self.name = name
    def __str__(self) :
        return self.name+":"+super().__str__()

list1 = MyList("jongbin")
list1.append(10)
list1.append(30)
list1.append(50)
list1.append(70)
list1.append(90)
print(list1)
#print(dir(list1))