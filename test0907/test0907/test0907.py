##################List
#data = ['a','b','c',['abcd','efc']]
#print(data[0])
#print(data[-1])
#print(data[-2])
#print(data)
#print(data[3][1])

#guests[]
#score[]

#guests['a','b','c','d']
#score[10,20,30,40]#score[0]==score[-4]// score[-1]==score[3]

#b = [1,2,3]
#c = ['Life','is','too','short']
#print(b+c)
#print(b*3)
#b[0]='jongbin'#배열안의 값을 바꿀때
#b[1]=['aaa','bbb']
#b[1:2]=['aaa','bbb']#b[1:2]는 1보다크거나같고 2보다작은 값 == b[1]
#print(b)
#b.insert(2,'e')
#b.append('jongbin2')
#print(b[-1])
##b.remove('c')
#b[1:2] = []
#del b[0]
#print(b.index('aaaa'))

#id = ['jongbin1','jongbin2','jongbin3']
#id.insert(1,111)#덮어씌여지지 않음
#id.insert(3,222)
#id.insert(5,333)
#id.insert(2,['김종빈','0101111'])
#id.insert(4,['김종빈1','0102222'])
#id.insert(6,['김종빈2','0103333'])
#print(id)


##############################for문
#guests=['a','b','c','d']
#for steps in range(4) :
#    print(guests[steps])#파이썬에선 들여쓰기가 굉장히 중요(스페이스나 텝으로)

#nEntries = len(guests)
#for steps in range(nEntries) :
#    print(guests[steps])

#for guest in guests :
#    print(guest)

#for abc in guests :
#    print(abc)
###################sort
score=[90,40,30,80,100,12,33]
print(score)
score.sort()
print(score)
score.reverse()
print(score)
top3 = score[0:3]
print(top3)




