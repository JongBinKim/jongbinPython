class Movie : #static class메소드 인스턴스 참조 여부
    '''영화클래스'''
    title = "암살"
    director = "김종빈"
    count = 0 #객체생성될때마다 플러스
    def __init__(self, title, director) : #생성자
        self.title = title
        self.director = director
        #self.count += 1
        Movie.count += 1
        print(self.title + "생성자 호출 ")

    def __del__(self) :
        print(self.title + "소멸자 호출 ")

    def showInfo(self) :
        print(self.title + " " + self.director)

    @staticmethod
    def showCountS() :
        print(Movie.count)

    @classmethod
    def showCountC(cls) :
        print(cls.count)

    
m1 = Movie("a","b")
m2 = Movie("c","d")
m3 = Movie("e","f")
m4 = Movie("a","s")
m5 = Movie("l","r")

Movie.showCountC()
Movie.showCountS()
#movie1 = Movie("베테랑1","류승완1")
#movie2 = Movie("베테랑2","류승완2")
#movie3 = Movie("베테랑3","류승완3")
#movie4 = Movie("베테랑4","류승완4")
#print(type(movie4))
#movie4 = movie3     #모든 변수는 참조형(같은주소 가리킴)
#print(id(movie4))
#print(id(movie3))
#movie4.showInfo()

#==>Movie.__init__(movie1,"aaa","bbb")

#movie1.actor = "mainactor"#멤버변수 추가

#print(movie1.actor)
#print(movie1.__doc__)#클래스 해당정보 출력'''  '''

#print(movie1.title)
#print(movie1.__class__.title)

#print(movie1.title)
##print(movie2.actor)
#movie1.showInfo()
#movie2.showInfo()