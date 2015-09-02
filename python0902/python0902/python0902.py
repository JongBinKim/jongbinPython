print("i gads %d" % 6)
print("%d %d %d %d"%(1,2,3,4))
#asdfasdfasd
#print("Here are the numbers!" + \ "%d %d"%(6,7))

'''
salary = input("please enter your salary : ")#input은 기본 자료형이 string
bonus = input("please enter your bonus : ")
payCheck = salary + bonus
payCheck = float(salary) + float(bonus)
print(payCheck)
'''

#ctr + k + c / ctr + k + u
#salary = float(input("please enter your salary : "))#file->고급 설정 -> utf-8(한글 사용가능)
#bonus = float(input("please enter your bonus : "))
#payCheck = salary + bonus
#print(round(payCheck,2))#소수점 2자리까지 출력
#print(payCheck)
##ㅁㅇㄴㄻㅇㄴㄹ
#print(type(payCheck))#type check

print("="*10)#문자열 10번 반복

#index 0 시작 index -1 끝
name = "jongbin1"
print(name[0])
print(name[-4])
print(name[0:3]) #0번 인덱스부터 2이하 인덱스까지(3자리출력)

info = "201011248jongbin"
sid = info[:9]#처음부터 9번째까지(지정된범위까지)
sname = info[9:]#지정된곳부터 ㄱ끝까지
print(sid + " " + sname)
#문자열 상수 수정 안됨

#a = "i eat %s aaa." %"five"
#print(a)

#a = "i eat %10s aaa." %"five"
#print(a)

#a = "i eat %-10s aaa." %"five"
#print(a)

#a = "error is %d%%."%34
#print(a)

quit = input("exit? ").upper()
print(quit)
