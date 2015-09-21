class Service :
    secret = "aaaaaaaaaaaaaaaaa"
    def sum(self, a, b) : #self 가 구분자로 꼭 들어가야함
        result = a + b
        print("%s + %s  = %s "%(a,b,result))

pey = Service()
print(pey.secret)

pey.sum(1,1) # 바운드가 된후에는 명시적으로 self 불필요
Service.sum(pey,1,1)
