#import pickle#########저장 dump()###########읽어오기 load()

#fileName = "friends2.txt"
#fileName2 = "Monica.txt"

#roles = []

#with open(fileName, "r") as myFile, open(fileName2, "wb+") as monica :## pickle바이너리형태라 wb
    #myFile.write("201011248 김종빈\n")
    #myFile.write("201011247 기민주\n")
    #myFile.write("201011246 이철헌\n")
    #myFile.write("201011245 최종윤\n")

 #전체 읽기
 #   content = myFile.read()
 #   print(content)
 ##   myFile.close()#with에선 클로즈 필요없음
    #for문 과 while문 사용으로 한줄씩 읽기
    #while True :
    #    content = myFile.readline()
    #    if not content : break
    #    print(content)
    
    #for line in myFile :
    #    print(line)
    
    #for content in myFile :
    #    (role, etc) = content.strip().split(":",1)
    #    if (role == "Monica") :
    #        monica.write(role +" : "+ etc)
    #        monica.write("\n")
    #    if role[0] == "M" :
    #        print(role +  " :" + etc)
    
    ####리스트에 저장
    #for content in myFile :
    #    (role,etc) = content.strip().split(":",1)
    #    roles.append(role)
    #print(roles)
#     for content in myFile :
#        (role,etc) = content.strip().split(":",1)
#        roles.append(role)
#    pickle.dump(roles, monica)
    
#with open(fileName, "r") as myFile, open(fileName2, "rb") as monica :## pickle바이너리형태라 wb
#    result = pickle.load(monica)
#    print(result)
