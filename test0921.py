#class Service :
#    secret = "aaaaaaaaaaaaaaaaa" #클래스 변수
#    def _init_(self, name, value=0) : #초기화하면서 멤버변수 생성가능(인스턴스 객체를 통해서만 엑세스)
#        self.name = name        #인스턴스 변수
#        self.value = value
#        self.secret = name
#    def sum(self, a, b) : #self 가 구분자로 꼭 들어가야함
#        result = a + b
#        print("%s + %s  = %s "%(a,b,result))

#Service.age = 0 #새로운 클래스 변수
#S1.age2 = 20     #S1인스턴스에서만 사용할수 있는 멤버

#pey = Service()
#print(pey.secret)

##동일한 형태의 함수 호출#
#pey.sum(1,1) # 바운드가 된후에는 명시적으로 self 불필요
#Service.sum(pey,1,1)

