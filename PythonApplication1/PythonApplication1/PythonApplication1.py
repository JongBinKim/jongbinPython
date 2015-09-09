import turtle
##dictionary

#dic1 = {}
#dic2 = dict()
#dic = {'name':'pey','phone':'0101111','birth':'1111'}
#a = {1:'hi'}
#b = {'a':[1,2,3]}
#print(dic['name'],dic['phone'])
#c = dic.keys()
#print(c)

##키값들을 리스트로 받기

#c=list(dic.keys())

#d = dic.items()
#print(d)

##별점주기

#dic3 = {'Hong':{'Veterang':'5.0','ArmSal':'4.5'},
#         'Cheol':{'GoGil':'3.0', 'Jong':'10.0'}}
#print(dic3['Hong'],dic3['Cheol'])
#print(dic3['Hong'].get('ArmSal'))
#print(dic3['Hong']['ArmSal'])

##제어문

#answer = input("Would you like express shipping?").lower()

#if answer == "yes" :
#    print("That will be an extra $10")
#else :
#    print("no charge")

#for 문
a = [(1,2),(3,4),(5,6)]
for(first, last) in a :
    print(first + last)

#구구단
for i in range(2,10) :
    for j in range(1,10) :
        print("%d * %d = %d" %(i,j,i*j), end="")
    print(" ")

#turtle 그리기 라이브러리
#nSides = 12
#for steps in range(nSides) :
#    turtle.forward(100)
#    turtle.right(360/nSides)
#    for step2 in range(nSides) :
#        turtle.forward(50)
#        turtle.right(360/nSides)

#While문 메뉴 만들기 예제

prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: """

number = 0
while number != 4 :
    print(prompt, end="")
    number = int(input())