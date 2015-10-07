list1 = [1,2,3,4,5]
print(dir(list1))

data = list(enumerate(list1))
print(data)

print(eval("1+2"))
print(eval("divmod(4,3)"))

def evenNum(a) :
    return a%2 == 0


print(list(filter(lambda x : x%2 == 0,[1,2,3,4,5,6])))

b=3
print(id(3))
print(id(b))

list2 = [lambda a,b : a+b, lambda a,b:a*b]
print(list2[0](3,4))
print(list2[1](2,3))

list3 = ("greenjoa")
list4 = ((1,2,3))
a = [1,2,3]
b = list(a)
c = a

print(id(a))
print(id(b))
print(id(c))

def two_times(x) : 
    return x*2
print(list(map(two_times,[1,2,3])))

print(list(map(lambda a: a*2, [1,3,5])))

print(eval(repr("hi".upper())))#'HI'   eval('HI')  eval(HI)

########################################sorting######################################
#list = [5,2,10,3,1,7]
#print(sorted(list))
#print(sorted("zero"))
#list.sort()
#print(list) #print(list.sort()) 안됨

data = {"홍길동" : [80,70,60,92],
       "김길동" : [20,50,80,12],
       "고길동" : [81,50,90,99]}
##[key,value]
print(type(data))        

data["홍길동"]#키값으로 value값 얻어옴
for list1 in data.values() :
    list1.sort()
keys = list(data.keys())
keys.sort()    

for i in keys:
    print(i,data[i])

#for list in data.keys() :
#    list.sort()

#print(data)    
