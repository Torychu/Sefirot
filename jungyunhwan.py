
# for 문의 유형
#     range
#     in
# a = '갑옷'
# # a = [0,1,2,3,4,5,6,7,8,9]
# char = ['방패','칼','갑옷','장화','활','총','헬멧']

# 배열변수 리스트변수
# 인덱스를 가지고 있으며 인덱스로 접근이 가능하다,...
#
# for apple in range(9,0,-2) :
#     print (apple)
#
# a = [(1,2),(3,4),(5,6)]
#
# # print(a[0])
# # print(a[1])
# # print(a[2])
#
# for (first, last) in a:
#     print (first + last)
#
#  합격 불합격 판단 로직
# marks = [90,25,67,45,80]
# number = 0
# for mark in marks:
#     number = number +1
#     if mark < 60:
#         continue
#     print ("%d번 학생은 합격입니다." %number )
# for mark in marks:
#     number = number +1
#     if mark >= 60:
#         print ("%d번 학생은 합격입니다." %number )

# 터틀 라이브러리 또는 모듈
# 터틀로 오륜기 그리기
# import turtle as t
#
# tu = t.Turtle()
# s =t.Screen()
#
# tu.shape('turtle')
#
# tu.circle(100)
# tu.penup()
# tu.goto(100,-100)
# tu.pendown()
# tu.circle(100)
# tu.penup()
# tu.goto(200,0)
# tu.pendown()
# tu.circle(100)
# tu.penup()
# tu.goto(300,-100)
# tu.pendown()
# tu.circle(100)
# tu.penup()
# tu.goto(400,0)
# tu.pendown()
# tu.circle(100)
#
# s.mainloop()
# 별찍기 노가다와 비교
# for i in range (1):
#     print('*' * 1)
#     print('*' * 2)
#     print('*' * 3)
#     print('*' * 4)
#     print('*' * 5)
#     print('*' * 6)
# for i in range(6):
#     print('*' * i)
#marks = [70,65,55,75,95,90,80,85,100]
# 더한값을 저장해놓을 변수 추가
# sum = 0
# for mark in marks:
#     if mark < 60:
#         continue
#     sum = sum + mark
# print(sum/9)

# 딕셔너리 자료형
# a = { 'a': [1,2,3]}
# print(a['a'])

# 터틀 반복
# import turtle
#
# s = turtle.Screen()
# t = turtle.Turtle()
#
# s.screensize(400,400)
# t.penup()
# t.setposition(-200,200)
# t.pendown()
# t.forward(40)
# for i in range(10) :
#     t.right(90)
#     t.forward(400)
#     t.left(90)
#     t.forward(40)
#     t.left(90)
#     t.forward(400)
#     t.right(90)
#     t.forward(40)
#
# s.mainloop()

# 터틀 붓으로 감옥 철창 모양 만들기
# import turtle
#
# s = turtle.Screen()
# t = turtle.Turtle()
#
# s.screensize(400,400)
# t.penup()
# t.setposition(-200,200)
# t.pendown()
#
# for i in range(4):
#     t.forward(400)
#     t.right(90)
#
#
# t.penup()
# t.setposition(-200,200)
# t.pendown()
# t.setheading(270)

# for i in range(10):
#     t.penup()
#     t.setposition(t.xcor() +40,200)
#     t.pendown()
#     t.forward(400)
# s.mainloop()

# xcor 문법을 몰랐을 경우
# for i in range(-200,200,40):
#     t.penup()
#     t.setposition(i +40,200)
#     t.pendown()
#     t.forward(400)
# s.mainloop()

# 가로줄 추가
# import turtle
#
# s = turtle.Screen()
# t = turtle.Turtle()
#
# s.screensize(400,400)
# t.penup()
# t.setposition(-200,200)
# t.pendown()
# t.speed(8)
# for i in range(4):
#     t.forward(400)
#     t.right(90)
#
#
# t.penup()
# t.setposition(-200,200)
# t.pendown()
# t.setheading(270)
#
# for i in range(10):
#     t.penup()
#     t.setposition(t.xcor() +40,200)
#     t.pendown()
#     t.forward(400)
#
# t.penup()
# t.setposition(-200,200)
# t.pendown()
# t.setheading(0)
#
# for i in range(10):
#     t.forward(400)
#     t.penup()
#     t.setposition(-200, t.ycor() - 40)
#     t.pendown()
#
#
# s.mainloop()

# 체스판 만들기
# import turtle
#
# s = turtle.Screen()
# t = turtle.Turtle()
#
# s.screensize(400,400)
# t.penup()
# t.setposition(-200,200)
# t.pendown()
# t.speed(8)
#
# for i in range(4):
#     for i in range(4):
#         t.begin_fill()
#         t.color("black")
#         for i in range(4):
#             t.forward(40)
#             t.right(90)
#         t.end_fill()
#         t.forward(40)
#         for i in range(4):
#             t.forward(40)
#             t.right(90)
#         t.forward(40)
#
#     t.penup()
#     t.setposition(-200,t.ycor()-40)
#     t.pendown()
#
#     for i in range(4):
#         for i in range(4):
#             t.forward(40)
#             t.right(90)
#         t.begin_fill()
#         t.color("black")
#         t.forward(40)
#         for i in range(4):
#             t.forward(40)
#             t.right(90)
#         t.end_fill()
#         t.forward(40)
#     t.penup()
#     t.setposition(-200,t.ycor()-40)
#     t.pendown()
# s.mainloop()

# 터틀봇 복습
#
# import turtle
#
# s = turtle.Screen()
# t = turtle.Turtle()
#
# s.screensize(400,400)
# t.penup()
# t.setposition(-200,200)
# t.pendown()
# t.speed(8)
#
# for i in range(4):
#     t.forward(400)
#     t.right(90)
#
# t.setposition(-200,200)
# t.setheading(315)
# t.forward(565)
# t.penup()
# t.setposition(200,200)
# t.setheading(225)
# t.pendown()
# t.forward(565)
# t.penup()
# t.setposition(0,0)
# t.setheading(45)
# t.pendown()
# t.begin_fill()
# t.color("black")
# t.forward(283)
# t.setheading(180)
# t.forward(400)
# t.setheading(315)
# t.forward(565)
# t.setheading(180)
# t.forward(400)
# t.setheading(45)
# t.forward(283)
# t.end_fill()
#
# s.mainloop()

#딕셔너리 value값 출력하기
# gamelist = { '마크' : 30000 , '롤' : 0 , '아크' : 50000 }
# game = list(gamelist.keys())
# print(game)
#
# gamelist = { '마크' : 30000 , '롤' : 0 , '아크' : 50000 }
# game = list(gamelist.values())
# print(game)

#딕셔너리 value와 key값 출력하기
#
# a= {"김철수": 100, "장동건" : 90, "김나영" : 95, "송중기" : 80}
#
# for keys, value in a.items():
#     if value >= 90:
#        print(keys)
#
# for keys, value in a.items():
#     print(keys)
#     print(value)

# 좋아하는 과일(리스트)
# fruit = ["사과", "포도","홍시"]
# user = input("좋아하는 과일은?")
# if user in fruit:
#     print("정답입니다.")
# else:
#     print("오답입니다")

#좋아하는 과일(딕셔너리)
# fruit= {"봄" : "딸기" , "여름" : "수박", "가을" : "배" , "겨울" : "귤"}
# user = input("좋아하는 과일은?")
# if user in fruit.values():
#     print("정답입니다.")
# else:
#     print("오답입니다.")

#bmi 지수를 구하는 함수/인자값(파라미터)이 있는 함수
# def bmi_func(a,b):
#     return b/(a*a)
#
# a = int(input("몸무게를 입력하세요"))
# b = int(input("키를 입력하세요"))
# print(bmi_func(a,b))
#
#인자값이 없는 함수
# def p(a):
#     if a == 1:
#        print("hello")
#     else:
#         print("fuck")
# p(0)
#

# 더하기 함수
# def plus(a,b):
#     return a+b
#
# a = int(input("첫번째 값을 입력하세요"))
# b = int(input("두번째 값을 입력하세요"))
# print(plus(a,b))
#
# Tultle과 함수를 이용해 입력한 값만큼의 n각형 만들기
#
# import turtle
#
# s = turtle.Screen()
# t = turtle.Turtle()
#
# t.speed(8)
#
#
# def a():
#     for i in range(user):
#         t.forward(100)
#         t.left(360/user)
#
# user = int(input("숫자를 입력하세요")
#
# a()
#
# s.mainloop()
#
# 전역 변수/지역 변수 알아보기 1
# a = 0
# def vartest(a):
#     a = a+1
#     return a
# vartest(3)
#
# print(vartest(a))
#
# 전역 변수/지역 변수 알아보기 2
# a = 1
# def vartest(a):
#     a = a+1
#     return a
#
# a = vartest(a)
# print (a)
#
# 전역 변수/지역 변수 알아보기 3
# a = 1
# def vartest():
#     global a
#     a = a+1
#
#
# vartest()
# print(a)

#  점수를 입력 받아서 합격 불합격 판정해주는 함수
# 합수가 입력 받을 값은 학생의 이름, 과목, 점수
# 각 과목별 점수가 80점 이상이 사람만 합격
# 출력은 다음과 같이 한다
# 아무개 학생의 수학 점수는 90점 입니다
# 수학 합격 입니다
#
# 함수를 활용한 합격 불합격 판단하기
# score = int(input("점수를 입력하세요"))
# name = input("이름을 입력하세요")
# sub = input("과목을 입력하세요")
# result = 0
#
# def t(point):
#     # global result (global 활용)
#     if point >= 80:
#         result = 1
#     else:
#         result = 2
#     return  result
#
# result = t(score)
#
# if result == 1:
#     print(name,"학생의",sub,"점수는",score,"입니다")
#     print("합격")
# else:
#     print(name,"학생의",sub,"점수는",score,"입니다")
#     print("불합격")
#
# 소문자를 사용자에게 입력 받고 합수로 보내면 대문자로 바꾸어서 보내주는 함수
# 대문자로 바꾸는거는 파이썬 내장 함수에 있어
#
# 함수를 통해 소문자를 대문자로 변환하기
# user = input("알파벳을 입력하세요")
#
# def u():
#     print(user.upper())
#
# u()
#
#터틀 런 게임 만들어보기
# import turtle
# import random
# import threading

# s = turtle.Screen()
# t = turtle.Turtle()
# t1 = turtle.Turtle()
#
# t.speed(8)
#
# move = ["f","b","l","r"]
#
# r = random.randint(0,100)
# r1 = random.choice(move)
#
# print(r)
# print(r1)
# t.shape("turtle")
# t1.shape("turtle")

# for i in range(100):
#     r = random.randint(0,50)
#     angle = random.randint(1, 360)
#     t.forward(r)
#     r1 = random.choice(move)
#     if r1 == "l":
#         t.left(angle)
#     elif r1 == "r":
#         t.right(angle)
# t.penup()
# t1.penup()
# t.setposition(-450,400)
# t.towards()


# def e_move():
#     for i in range(10):
#         r = random.randint(0,560)
#         r1 = random.randint(0,50)
#         t.forward(r)
#         t.right(90)
#         t.forward(r1)
#         t.right(90)
#         t.forward(r)
#         t.left(90)
#         t.forward(r1)
#         t.left(90)
#
# th = threading.Thread(target=e_move)
# th.start()


# for i in range(20):
#     r = random.randint(0,560)
#     r1 = random.randint(0,50)
#     t.forward(r)
#     t.right(90)
#     t.forward(r1)
#     t.right(90)
#     t.forward(r)
#     t.left(90)
#     t.forward(r1)
#     t.left(90)

# head =0
#
# def right():
#     global head
#     head = head -90
#     t1.setheading(head)
# def left():
#     global head
#     head = head +90
#     t1.setheading(head)
# def forward():
#     t1.forward(10)
# def backward():
#     t1.backward(10)
#
# s.onkeypress(right,"Right")
# s.onkeypress(left,"Left")
# s.onkeypress(forward,"Up")
# s.onkeypress(backward,"Down")
# s.listen()
#
# s.mainloop()
#
#1과 20사이의 숫자 중 하나를 무작위로 뽑아 더하기 문제를 출제하고,정답률/맞은 갯수/틀린 갯수를 구해보자
#
# import random
#
# sum = 0
#
# for i in range(5):
#     num1 = random.randint(1, 20)
#     num2 = random.randint(1, 20)
#     print(num1, "+", num2, "=")
#     while True:
#         a = input("답을 입력하세요")
#         if a.isdigit() == False:
#             print("숫자만 입력 가능합니다!")
#             continue
#         else:
#             break
#     if num1+num2 == int(a):
#        print("정답입니다!")
#        sum = sum + 1
#     else:
#        print("틀렸습니다!")
#        print("정답은",num1+num2,"입니다!")
#
# print("문제가 종료되었습니다.")
# print("정답률은",sum*20,"% 입니다!")
# print("맞은 갯수는",sum,"개이고,틀린 갯수는",5-sum,"입니다!")
# print("수고하셨습니다.")

# 1과 20사이의 숫자 중 하나를 무작위로 뽑고,사칙 연산도 랜덤하게 뽑아 문제를 출제하고,정답률/맞은 갯수/틀린 갯수를 구해보자
# import random
#
# print("!주의사항!")
# print("나눗셈의 경우 소수점 둘째자리에서 반올림해야 하며,답이 1일 경우 1.0이라고 적어야 합니다.")
# print("그럼 시작하겠습니다.")
# sum = 0
# px = ["+","-","*","/"]
# correct = 0
# def plus(num1,num2):
#     return num1+num2
#
# def m(num1,num2):
#     return num1-num2
#
# def x(num1,num2):
#     return num1*num2
#
# def s(num1,num2):
#     return num1/num2
# def is_digit(str):
#     try:
#         tmp = float(str)
#         return True
#     except ValueError:
#         return False
#
# for i in range(5):
#     num1 = random.randint(1, 20)
#     num2 = random.randint(1, 20)
#     pm = random.choice(px)
#     print(num1, pm, num2, "=")
#     while True:
#         a = input("답을 입력하세요")
#         if is_digit(a) == False:
#             print("숫자만 입력 가능합니다!")
#             continue
#         else:
#             if pm == "+":
#                 correct = plus(num1,num2)
#                 if correct == int(a):
#                     print("정답입니다.")
#                     sum = sum + 1
#                     break
#             elif pm == "-":
#                 correct = m(num1,num2)
#                 if correct < 0:
#                     if str(correct) == str(a):
#                         print("정답입니다.")
#                         sum = sum + 1
#                         break
#                     else:
#                         print("틀렸습니다!")
#                         print("정답은",correct,"입니다!")
#                         continue
#                 elif correct == int(a):
#                     print("정답입니다.")
#                     sum = sum + 1
#                     break
#                 else:
#                     print("틀렸습니다!")
#                     print("정답은",correct, "입니다!")
#                     break
#             elif pm == "*":
#                 correct = x(num1,num2)
#                 if correct == int(a):
#                     print("정답입니다.")
#                     sum = sum + 1
#                     break
#             elif pm == "/":
#                 if num1%num2 ==0:
#                     correct = s(num1, num2)
#                     if str(correct) == str(a):
#                         print("정답입니다.")
#                         sum = sum + 1
#                         break
#                     else:
#                         print("오답입니다.")
#                         print("정답은", correct, "입니다!")
#                         break
#                 else:
#                     correct = s(num1, num2)
#                     if str(round(correct,2)) == str(a):
#                         print("정답입니다.")
#                         sum = sum + 1
#                         break
#                     else:
#                         print("오답입니다.")
#                         print("정답은",round(correct,2), "입니다!")
#                         break
# print("문제가 종료되었습니다.")
# print("정답률은",sum*20,"% 입니다!")
# print("맞은 갯수는",sum,"개이고,틀린 갯수는",5-sum,"입니다!")
# print("수고하셨습니다.")

# import random
#
# sum = 0
#
# for i in range(5):
#     num1 = random.randint(1, 20)
#     num2 = random.randint(1, 20)
#     print(num1, "+", num2, "=")
#     while True:
#         a = input("답을 입력하세요")
#         if a.isdigit() == False:
#             print("숫자만 입력 가능합니다!")
#             continue
#         else:
#             break
#     if num1+num2 == int(a):
#        print("정답입니다!")
#        sum = sum + 1
#     else:
#        print("틀렸습니다!")
#        print("정답은",num1+num2,"입니다!")
#
# print("문제가 종료되었습니다.")
# print("정답률은",sum*20,"% 입니다!")
# print("맞은 갯수는",sum,"개이고,틀린 갯수는",5-sum,"입니다!")
# print("수고하셨습니다.")

# 위의 2번째 문제에서 계속 진행하는 것과 함께 yes와 no로 답변을 받고 진행하는 것과 총 통계를 내보자
# import random
#
# print("!주의사항!")
# print("나눗셈의 경우 소수점 둘째자리에서 반올림해야 하며,답이 1일 경우 1.0이라고 적어야 합니다.")
# print("그럼 시작하겠습니다.")
# sum = 0
# px = ["+","-","*","/"]
# correct = 0
# c = 0
# sc = [0]
# score = []
#
# def plus(num1,num2):
#     return num1+num2
#
# def m(num1,num2):
#     return num1-num2
#
# def x(num1,num2):
#     return num1*num2
#
# def s(num1,num2):
#     return num1/num2
#
# def is_digit(str):
#     try:
#         tmp = float(str)
#         return True
#     except ValueError:
#         return False
#
# while True:
#     for i in range(5):
#         c = c + 1
#         num1 = random.randint(1, 20)
#         num2 = random.randint(1, 20)
#         pm = random.choice(px)
#         print(num1, pm, num2, "=")
#
#         a = input("답을 입력하세요")
#         if is_digit(a) == False:
#             print("숫자만 입력 가능합니다!")
#             continue
#         if pm == "+":
#             correct = plus(num1,num2)
#             if str(correct) == str(a):
#                 sum = sum + 1
#                 sc = sc + 1
#                 print("정답입니다!")
#             else:
#                 print("틀렸습니다!")
#                 print("정답은", correct, "입니다!")
#         elif pm == "-":
#             correct = m(num1,num2)
#             if str(correct) == str(a):
#                 sum = sum + 1
#                 sc = sc + 1
#                 print("정답입니다!")
#             else:
#                 print("틀렸습니다!")
#                 print("정답은", correct, "입니다!")
#         elif pm == "*":
#             correct = x(num1,num2)
#             if str(correct) == str(a):
#                 sum = sum + 1
#                 sc = sc + 1
#                 print("정답입니다!")
#             else:
#                 print("틀렸습니다!")
#                 print("정답은", correct, "입니다!")
#         elif pm == "/":
#             correct = s(num1,num2)
#             if str(correct) == str(a):
#                 sum = sum + 1
#                 sc = sc + 1
#                 print("정답입니다!")
#             else:
#                 print("틀렸습니다!")
#                 print("정답은",round(correct,2), "입니다!")
#
#
#
#
#     more = input("더할래? yes or no 로 답하시오")
#     if more == "yes":
#         continue
#     elif more == "no":
#         print("최고점수는",{max(sc)},"입니다!")
#         print("최저점수는",{min(sc)},"입니다!")
#         print("평균점수는",s(sc,c),"입니다.")
#         print("수고하셨습니다")
#         break
#     else:
#         print("yes or no 만 대답해!")
#         break

# 세개의 정수를 입력받아 최대값을 구하여 리턴하는 함수 작성

# def a(num1,num2,num3):
#     b = [num1,num2,num3]
#     return max(b)

#반지름의 길이를 전달받아 넓이를 출력하는 함수 작성

# def a(num1):
#     return num1*num1*3.14
#
# num1=10
#
# print(round(a(num1),2))

#10 이하의 두 개의 양의 정수를 입력받아서 작은 수부터 큰 수까지의 구구단을 차례대로 출력하는 프로그램을 작성

# num1=3
# num2=5
#
# for x in range(num1, num2+1):
#     print("==" + str(x) + "단==")
#     for y in range(1, 10):
#         print(x, "X", y, "=", x*y)
# print("---------------------")

#자연수 n를 입력받아서 삼각형 모양으로 정렬해주는 코드 작성
# num1 = 5
#
# for i in range(num1+1):
#     print('*' * i)

#자연수 n을 입력받아 삼각형을 뒤집은 모양으로 정렬해주는 코드 작성
# num1 = 3
#
# for i in range(num1+1, 0, -1):
#     print('{:>5}'.format('*' * (i-1)))

#n부터 m까지의 합을 구하는 코드 작성

# n=int(input("첫번째 값을 입력하세요."))
# m=int(input("두번째 값을 입력하세요."))
#
# def solution(n,m):
#     sum = 0
#     for i in range(n,m+1):
#         sum = sum + i
#     return  sum
#
# print(solution(n,m))

#학생들의 키가 들어있는 목록에서 키가 k보다 큰 사람은 몇 명인지 구하는 함수 작성하기
#
# height = [165,170,175,180,184]
# k = 175
#
#
# def solution(height,k):
#     result = 0
#     for i in height:
#         if i > k:
#             result = result+1
#     return result
#
# print(solution(height,k))

#0~99까지 한 라인에 하나씩 순차적 출력하기
#
# s = 0
# for i in range(1,101):
#     print(s)
#     s = s+1

#for문을 이용해 2002년부터 2050년까지 월드컵이 열리는 연도를 출력하기

# s = 2002
# for i in range(13):
#     print(s)
#     s = s+4

#1부터 30까지의 숫자 중 3의 배수를 출력하라

# for i in range(11):
#     print(i*3)

#99부터 0까지 1씩 감소하는 숫자들을, 한 라인에 하나씩 출력하라

# s = 100
# for i in range(1,101):
#     s = s-1
#     print(s)

#for 문을 사용해서 0.0~0.9까지 출력
#
# s = 0
# for i in range(10):
#     n = str(s)
#     print("0."+n)
#     s = s+1

#구구단 3단 출력

# s = 0
#
# for i in range(1,10):
#     s = s+1
#     print(3, "X", s , "=",3*s)
#
# 구구단 3단 출력(홀수만)

# for i in range(1,10,2):
#     print(3,'x',i,'=',i*3)

#1~10까지의 숫자에 대해 모두 더한 값을 출력하는 프로그램을 for 문을 사용하여 작성하기

# print(1+2+3+4+5+6+7+8+9+10) <-날먹

# sum = 0
# for i in range(1,11,1):
#     sum = sum+i
# print(sum)

#1~10까지의 숫자에 대해 모두 홀수의 합을 출력하는 프로그램을 for 문을 사용하여 작성하기

# sum = 0
# for i in range(1,11,2):
#     sum = sum+i
# print(sum)

#1~10까지의 숫자를 모두 곱한 값을 출력하는 프로그램을 for 문을 사용하여 작성하라

# sum = 1
# for i in range(1,11,1):
#     sum = sum * i
# print(sum)

#리스트 변수를 만들고 for 문과 range문을 사용해 리스트값을 출력하라

# price_list = [32100,32150,32000,32500]
# s = 0
#
# for i in range(4):
#     print(price_list[s])
#     s = s+1

#리스트 변수를 만들고 for 문과 range문을 사용해 리스트 값을 출력,단 앞에 몇번째 리스트값인지 표기되게 하자

# price_list = [32100,32150,32000,32500]
# s = 0
#
# for i in range(4):
#     print(s,price_list[s])
#     s = s+1

#아래와 같이 리스트의 데이터를 출력하라. 단,for문과 range문을 사용할 것

# price_list = [32100,32150,32000,32500]
# 100 32150
# 110 32000
# 120 32500

# price_list = [32100,32150,32000,32500]
# s = 1
# n = 100
#
# for i in range(3):
#     print(n,price_list[s])
#     s = s+1
#     n = n+10

#my_list를 아래와 같이 출력하라.

# my_list = ["가","나","다","라"]
# 가 나
# 나 다
# 다 라

# my_list = ["가","나","다","라"]
#
# print(my_list[0],my_list[1])
# print(my_list[1],my_list[2])
# print(my_list[2],my_list[3])

#리스트를 아래와 같이 출력하라.

# my_list = ["가","나","다","라","마"]
# 가 나 다
# 나 다 라
# 다 라 마
#
# my_list = ["가","나","다","라","마"]
#
# print(my_list[0],my_list[1],my_list[2])
# print(my_list[1],my_list[2],my_list[3])
# print(my_list[2],my_list[3],my_list[4])

#반복문과 range 함수를 사용해서 my_list를 아래와 같이 출력하라.

# my_list = ["가","나","다","라"]
# 라 다
# 다 나
# 나 가

# my_list = ["가", "나", "다", "라"]
# a = 3
# s = 2
# for i in range(3):
#     print(my_list[a],my_list[s])
#     a = a-1
#     s = s-1

# 리스트에는 네 개의 정수가 저장되어 있다. 각각의 데이터에 대해서 자신과 우측값과의 차분값을 화면에 출력하라.
# my_list [100,200,400,800]
#
# 예를 들어 100을 기준으로 우측에 위치한 200과의 차분 값을 화면에 출력하고, 200을 기준으로 우측에 위치한 400과의 차분값을 화면에 출력한다.
# 이어서 400을 기준으로 우측에 위치한 800과의 차분값을 화면에 출력한다.
#
# 100
# 200
# 400
#
# my_list = [100,200,400,800]
# a = 0
# s = 1
# for i in range(3):
#     print(my_list[s]-my_list[a])
#     a = a+1
#     s = s+1

#리스트에는 6일 간의 종가 데이터가 저장 되어 있다. 종가 데이터의 3일 이동 평균을 계산하고 이를 화면에 출력하라.

# my_list = [100,200,400,800,1000,1300]
#
# def plus(a,b,c):
#     return a+b+c
#
# def plus2(b,c,d):
#     return b+c+d
#
# def plus3(c,d,e):
#     return c+d+e
#
# def plus4(d,e,f):
#     return d+e+f
#
# a = my_list[0]
# b = my_list[1]
# c = my_list[2]
# d = my_list[3]
# e = my_list[4]
# f = my_list[5]
#
# print(plus(a,b,c)/3)
# print(plus(b,c,d)/3)
# print(plus(c,d,e)/3)
# print(plus(d,e,f)/3)

#리스트에 5일간의 저가,고가 정보가 저장 되어 있다. 고가와 저가의 차를 변등폭이라고 정의할 때, low,high 두 개의 리스트를 사용해서
#5일간의 변등폭을 volatility 리스트에 저장하라
#
# low_prices = [100,200,400,800,1000]
# high_prices = [150,300,430,880,1000]
#
# volatility = []
# a=0
# for i in range(5):
#     volatility.append(high_prices[a]-low_prices[a])
#     a = a+1
#
# print(volatility)

#거북이 잡는 게임
#
# import turtle
# import playsound
# import threading
# import random
# import time
#
# t = turtle.Turtle()
# s = turtle.Screen()
# aim = turtle.Turtle()
# t_write = turtle.Turtle()
# sc=0
#
#
#
# start = time.time()
#
#
#
# t_write.up()
# t_write.speed(0)
# t_write.setposition(-200,200)
# t_write.hideturtle()
#
# aim.up()
# aim.shapesize(0.2)
# aim.shape("circle")
# aim.speed(0)
#
#
#
# t.shape("turtle")
# t.shapesize(5)
#
#
# def fire_on():
#     print("명중")
#     t.penup()
#     t.speed(0)
#     t.setposition(random.randint(-200,200),random.randint(-200,200))
#
# def sound():
#     playsound.playsound("C:/fire.wav")
#
# def on_mouse(x,y):
#     th_sound = threading.Thread(target=sound)
#     th_sound.start()
#     aim.setposition(x,y)
#     aim_range = (t.get_shapepoly()[3][0] - t.get_shapepoly()[3][1]) * -1
#     if aim.distance(t) < aim_range:
#         fire_on()
#         global sc
#         sc= sc+1
#         t_write.clear()
#         t_write.write("score:"+(str(sc)),font=get ("normal",30,"normal"))
#         if sc >= 10:
#             global stop
#             global result
#             t_write.setposition(-150,0)
#             t.hideturtle()
#             t.penup()
#             t.speed(0)
#             t.setposition(1000,1000)
#             t_write.write("게임이 종료되었습니다.",font=("normal",30,"normal"))
#             stop = time.time()
#             result = stop - start
#             time.sleep(3)
#             t_write.clear()
#             t_write.write("걸린 시간:"+(str(round(result,2))),font=("normal",30,"normal"))
#
#
#
# s.onclick(on_mouse)
# s.listen()
#
# s.mainloop()

#크롤러 기본
# from selenium import webdriver
#
# import time
#
# driver = webdriver.Chrome("c:/chromeDriver/chromedriver.exe")
# driver.get("https://google.com")
# a = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
# a.send_keys("피카츄")
# a.send_keys('\n')
# time.sleep(1)
# a = driver.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a')
# a.click()

#크롤러 유튜브
# from selenium import webdriver
#
# import time
#
# driver = webdriver.Chrome("c:/chromeDriver/chromedriver.exe")
# driver.get("https://www.youtube.com/")
# a = driver.find_element_by_xpath('//*[@id="search"]')
# a.send_keys("피카츄")
# a.send_keys('\n')
# time.sleep(1)
# a = driver.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string')
# a.click()

#크롤러를 통해 구글 이미지 자동 다운로드 받기(썸네일만)
# from selenium import webdriver
#
# def search_selenium(search_name, search_path, search_limit):
#     search_url = "https://www.google.com/search?q=" + str(search_name) + "&hl=ko&tbm=isch"
#     browser = webdriver.Chrome('c:/chromedriver/chromedriver.exe')
#     browser.get(search_url)
#     image_count = len(browser.find_elements_by_tag_name("img"))
#     print("로드된 이미지 개수 : ", image_count)
#     browser.implicitly_wait(2)
#     for i in range(search_limit):
#         image = browser.find_elements_by_tag_name("img")[i]
#         image.screenshot("c:/expression/Sad/" + str(i) + ".png")
#     browser.close()
# search_name = input("검색하고 싶은 키워드 : ")
# search_limit = int(input("원하는 이미지 수집 개수 : "))
# search_path = "Your Path"
# # search_maybe(search_name, search_limit, search_path)
# search_selenium(search_name, search_path, search_limit)

#크롤러로 현 공산국가 목록 위키피디아에서 가져오기
# from selenium import webdriver
#
# import time
#
# driver = webdriver.Chrome("c:/chromeDriver/chromedriver.exe")
# driver.get("https://google.com")
# a = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
# a.send_keys("공산국가")
# a.send_keys('\n')
# time.sleep(1)
# a = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div[1]/a/h3')
# a.click()
# a = driver.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/ul[1]').text
# print(a)

#for문과 리스트를 이용해 뽑아오기
#
# from selenium import webdriver
#
# driver = webdriver.Chrome("c:/chromeDriver/chromedriver.exe")
# driver.get("https://ko.wikipedia.org/wiki/%EA%B3%B5%EC%82%B0%EA%B5%AD%EA%B0%80")
#
# a = []
#
# for i in range(1,6):
#     a.append (driver.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/ul[1]/li[' + str(i) + ']').text)
# for i in a:
#     print(i)

#국가별 민주주의 지수 위 방법을 활용해 뽑아오기

# from selenium import webdriver
#
# driver = webdriver.Chrome("c:/chromeDriver/chromedriver.exe")
# driver.get("https://ko.wikipedia.org/wiki/%EB%AF%BC%EC%A3%BC%EC%A3%BC%EC%9D%98_%EC%A7%80%EC%88%98")
#
# a = []
#
# for i in range(1,168):
#     a.append (driver.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[' + str(i) + ']').text)
# for i in a:
#     print(i)
#
# image_count = len(driver.find_elements_by_tag_name("img"))
# print("로드된 이미지 개수 : ", image_count)
# driver.implicitly_wait(2)
# for i in range(4,172):
#     image = driver.find_elements_by_tag_name("img")[i]
#     image.screenshot("c:/expression/Sad/" + str(i) + ".png")
# driver.close()
# search_limit = int(input("원하는 이미지 수집 개수 : "))
# search_path = "Your Path"
# search_maybe(search_name, search_limit, search_path)
# search_selenium(search_name, search_path, search_limit)

#네이버 데이터랩에 들어가서 실시간 패션검색어 리스트 뽑아오기

#
#from selenium import webdriver
# driver = webdriver.Chrome("c:/chromeDriver/chromedriver.exe")
# driver.get("https://datalab.naver.com/")
#
# a = []
#
# a.append (driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[4]/div/div[1]/div/div/div[9]/div').text)
# for i in range(9,13):
#     a.append (driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[4]/div/div[1]/div/div/div[' + str(i) + ']/div/div/ul').text)
#
# for i in a:
#     print(i)

#네이버 데이터랩에 들어가서 5월 6일부터 17일까지 클릭을 활용하여 데이터 전부 뽑아오기
# from selenium import webdriver
# import time
#
# driver = webdriver.Chrome("c:/chromeDriver/chromedriver.exe")
# driver.get("https://datalab.naver.com/")
#
# a = []
#
#
# for i in range(1,10):
#     c = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[4]/div/div[1]/div/a[1]/span')
#     c.click()
#     time.sleep(1)
#
#
# for i in range(1,5):
#     a.append (driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[4]/div/div[1]/div/div/div[' + str(i) + ']/div/div/ul').text)
# for i in range(1,5):
#     c = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[4]/div/div[1]/div/a[2]/span')
#     c.click()
#     time.sleep(1)
# for i in range(4,9):
#     a.append (driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[4]/div/div[1]/div/div/div[' + str(i) + ']/div/div/ul').text)
# for i in range(1,5):
#     c = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[4]/div/div[1]/div/a[2]/span')
#     c.click()
#     time.sleep(1)
# for i in range(9,13):
#     a.append (driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[4]/div/div[1]/div/div/div[' + str(i) + ']/div/div/ul').text)
# for i in range(1,5):
#     c = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[4]/div/div[1]/div/a[2]/span')
#     c.click()
#     time.sleep(1)
#
# for i in a:
#     print(i)


# from selenium import webdriver
# import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# #
# driver = webdriver.Chrome("c:/chromeDriver/chromedriver.exe")
# driver.get("https://datalab.naver.com/local/trend.naver")
#
# a = []
#
# time.sleep(5)
#
# driver= webdriver.Chrome()
# url= "https://datalab.naver.com/local/trend.naver"
# driver.get(url)
# play_button= WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '//*[@id="content"]/div[2]/div/div[2]/div[2]/div[2]/svg/g[1]/g[4]/g[1]/rect[30]')))
# play_button.click()
# time.sleep(10)
#
# for i in range(1,11):
#     a.append (driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[2]/div[2]/div[2]/div/div/div[' + str(i) + ']').text)
#
# for i in a:
#     print(a)

# 체스판 만들기 v2
# import turtle
#
# s = turtle.Screen()
# t = turtle.Turtle()
#
# s.screensize(400,400)
# t.penup()
# t.setposition(-200,200)
# t.pendown()
# t.speed(8)
#
# for i in range(5):
#     for i in range(5):
#         t.begin_fill()
#         t.color("black")
#         for i in range(4):
#             t.forward(40)
#             t.right(90)
#         t.end_fill()
#         t.forward(40)
#         for i in range(4):
#             t.forward(40)
#             t.right(90)
#         t.forward(40)
#     t.penup()
#     t.setposition(-200, t.ycor() - 40)
#     t.pendown()
#     for i in range(5):
#         for i in range(4):
#             t.forward(40)
#             t.right(90)
#         t.begin_fill()
#         t.color("black")
#         t.forward(40)
#         for i in range(4):
#             t.forward(40)
#             t.right(90)
#         t.forward(40)
#         t.end_fill()
#     t.penup()
#     t.setposition(-200, t.ycor() - 40)
#     t.pendown()
#
# s.mainloop()

# import turtle
#
# s = turtle.Screen()
# t = turtle.Turtle()
#
# s.screensize(400,400)
# t.penup()
# t.setposition(-200,200)
# t.pendown()
# t.speed(8)
#
#체스판 만들기 v3

# import turtle
#
# s = turtle.Screen()
# t = turtle.Turtle()
#
# s.screensize(400,400)
# t.penup()
# t.setposition(-200,200)
# t.pendown()
# t.speed(0)
#
# def square(color):
#     t.begin_fill()
#     t.fillcolor(color)
#     for i in range(4):
#         t.forward(40)
#         t.right(90)
#     t.end_fill()
#     t.forward(40)
#
# def skip():
#     t.penup()
#     t.setposition(-200, t.ycor() - 40)
#     t.pendown()
#
# for i in range(5):
#     for i in range(5):
#         square("black")
#         square("white")
#     skip()
#     for i in range(5):
#         square("white")
#         square("black")
#     skip()
#
# s.mainloop()

#체스판 만들기 v4
#
# import turtle
#
# s = turtle.Screen()
# t = turtle.Turtle()
# change = turtle.Turtle()
#
# s.screensize(400,400)
# t.penup()
# t.setposition(-200,200)
# t.pendown()
# t.speed(0)
# change.speed(0)
# s.tracer(0)
#
#
# change.penup()
# change.hideturtle()
# change.shape("square")
# change.shapesize(1.9)
# change.color("white")
#
#
#
# def sub(color):
#     t.begin_fill()
#     t.fillcolor(color)
#     for i in range(4):
#         t.forward(40)
#         t.right(90)
#     t.end_fill()
#     t.forward(40)
#
# def sub2():
#     for i in range(4):
#         t.forward(40)
#         t.right(90)
#     t.forward(40)
#
# def square(color):
#     t.begin_fill()
#     t.fillcolor(color)
#     for i in range(4):
#         t.forward(40)
#         t.right(90)
#     t.end_fill()
#     t.forward(40)
#
# def skip():
#     t.penup()
#     t.setposition(-200, t.ycor() - 40)
#     t.pendown()
#
# for i in range(5):
#     for i in range(5):
#         square("black")
#         square("yellow")
#     skip()
#     for i in range(5):
#         square("yellow")
#         square("black")
#     skip()
#
# def s_click(x, y):
#     change.setposition(x,y)
#     change.stamp()
#     t.penup()
#     t.setposition(-200, 200)
#     t.pendown()
#     for i in range(5):
#         for i in range(5):
#             sub("black")
#             sub2()
#         skip()
#         for i in range(5):
#             sub2()
#             sub("black")
#         skip()
#
# s.onclick(s_click)
#
# s.mainloop()

#체스판 만들기 v4.1

# import turtle
# import random
#
# s = turtle.Screen()
# t = turtle.Turtle()
# change = turtle.Turtle()
#
# s.screensize(400,400)
# t.penup()
# t.setposition(-200,200)
# t.pendown()
# t.speed(0)
# change.speed(0)
# s.tracer(0)
# target_fix = []
# click_target = []
# num = 0
# trycount = 0
# clicklog = []
#
#
# change.penup()
# change.hideturtle()
# change.shape("square")
# change.shapesize(1.9)
# change.color("white")
#
#
#
# def sub(color):
#     t.begin_fill()
#     t.fillcolor(color)
#     for i in range(4):
#         t.forward(40)
#         t.right(90)
#     t.end_fill()
#     t.forward(40)
#
# def sub2():
#     for i in range(4):
#         t.forward(40)
#         t.right(90)
#     t.forward(40)
#
# def square(color):
#     global target_fix
#     t.begin_fill()
#     t.fillcolor(color)
#     for i in range(4):
#         t.forward(40)
#         t.right(90)
#     if color == "yellow":
#         target_fix.append([int(t.xcor()),int(t.ycor())])
#     t.end_fill()
#     t.forward(40)
#
# def skip():
#     t.penup()
#     t.setposition(-200, t.ycor() - 40)
#     t.pendown()
#
#
# for i in range(5):
#     for i in range(5):
#         square("black")
#         square("yellow")
#     skip()
#     for i in range(5):
#         square("yellow")
#         square("black")
#     skip()
#
# def s_click(x, y):
#     global trycount
#     global clicklog
#     change.setposition(x,y)
#     for i in range(len(target_fix)):
#         if target_fix[i][0] + 40 > change.xcor() and target_fix[i][0] < change.xcor() and target_fix[i][1] - 40 < change.ycor() and target_fix[i][1] > change.ycor():
#                 change.setposition(target_fix[i][0]+20,target_fix[i][1]-20)
#                 change.stamp()
#                 clicklog.append([target_fix[i][0],target_fix[i][1]])
#                 for j in range(len(clicklog)):
#                     if clicklog[j][0] + 40 > change.xcor() and clicklog[j][0] < change.xcor() and clicklog[j][1] - 40 < change.ycor() and clicklog[j][1] > change.ycor():
#                         print(trycount)
#                     else:
#                         print(trycount)
#                         trycount = trycount + 1
#                         if target[0] + 40 > change.xcor() and target[0] < change.xcor() and target[1] - 40 < change.ycor() and target[1] > change.ycor():
#                             s.clear()
#                             t.write("게임이 종료되었습니다.", font=("normal", 30, "normal"))
#                             t.setposition(-100,0)
#                             t.write("시도횟수:"+str(trycount), font=("normal", 30, "normal"))
#
# def cancel():
#     change.clearstamps(-1)
#
# target = random.choice(target_fix)
# print(target)
# s.onclick(s_click)
#
# s.onkeypress(cancel,"r")
# s.listen()
#
# s.mainloop()]


#더하기 함수
# def plus(a,b):
#     return a+b
#
# a = int(input("첫번째 값을 입력하세요."))
# b = int(input("두번째 값을 입력하세요."))
#
# print(plus(a,b))

#2
# a = str(input("첫번째 문자열을 입력해주세요."))
# b = str(input("두번째 문자열을 입력해주세요."))
#
# def test(a,b):
#     if a>=b:
#         print(a)
#     elif b>=a:
#         print(b)
# test(a,b)

#입력받은 수 만큼 역삼각형으로 별 출력하기
# num1 = int(input("줄 수를 입력하세요."))
#
# for i in range(num1+1, 0, -1):
#     print('{:>5}'.format('*' * (i-1)))

#입력받은 문자열 양 끝에 쌍따옴표 붙여서 출력하기

# a = input("원하는 문자열을 입력하세요.")
# print('"'+a+'"')

#입력받은 수의 절댓값 출력하기

# a = int(input("숫자를 입력하세요"))
# def va():
#     b = a*-1
#     if a > 0:
#         print(a)
#     if a < 0:
#         print(b)
# va()

#두 숫자가 같으면 두 숫자의 합을,다르면 차를 출력하기
#
# a = int(input("첫번째 숫자를 입력하세요."))
# b = int(input("두번째 숫자를 입력하세요."))
#
# def v(a,b):
#     if a == b:
#         return a+b
#     elif a >= b:
#         return a-b
#     elif b >= a:
#         return b-a
#
# print(v(a,b))

# a = int(input("입력"))
# b= 0
# for i in range(1,a+2):
#     print(b)
#     b = b+1

#첫번째 숫자에서 두번째 숫자를 뺀 값을 모두 출력하기
# a = [1,3,6,2]
#
# for i in range(0,3):
#     b=a[i]-a[i+1]
#     print(b)

#문자열 거꾸로 출력
# num1 = str(input("숫자넣어"))
#
# print(str(num1[::-1]))

#문자열에서 1의 개수 구하기
# print("4156721".count("1"))

#장갑 쌍 찾기

# left_gloves = [2,1,2,2,4]
# right_gloves = [1,2,2,4,4,7]
# count = 0
#
# right_gloves.remove(left_gloves[0])
# for i in range(len(left_gloves)):
#     if left_gloves[i] in right_gloves:
#         count = count+1
# print(count)

#자격증 시험 대비 문제 1번
# a = input()
# print("'"+a+"'")

#자격증 시험 대비 문제 2번
# n = int(input())
# i = 1
# while i<=n:
#     print(i*10)
#     i += 1

#자격증 시험 대비 문제 3번
# a, b = input().split(",")
# a = int(a)
# b = int(b)
# print(a-b)

#자격증 시험 대비 문제 4번
# s= input()
# for i in range(len(s)-1,-1,-1):
#     print(s[i], end='')

# 자격증 시험 대비 문제 5번
# n = int(input())
# arr = input().split(" ")
# for i in range(n):
#     arr[i] = int(arr[i])
# for i in range(len(arr)-1):
#     print(arr[i+1]-arr[i], end=' ')

#자격증 시험 대비 문제 6번
# a = 2
# s = 0
# for i in range(2,10,1):
#     for i in range(1,10):
#         s = s+1
#         print(a, "X", s , "=",a*s)
#     a = a+1
#     s = 0

#자격증 시험 대비 문제 7번
# n = int(input("숫자 입력"))
#
# for i in range(1,n+1):
#     if n % i == 0:
#         print(i , end=" ")

#자격증 시험 대비 문제 8번
# s = int(input())
#
# if s >= 150:
#     print("true")
# else:
#     print("false")

#자격증 시험 대비 문제 9번
# a, b = input().split(",")
# a = int(a)
# b = int(b)
#
# print(a*b)
# print(a//b)

#자격증 시험 대비 2 문제 1번
# n = int(input())
# for i in range(n+1):
#     for j in range(i):
#         print(j+1, end=' ')
#     print("")

#자격증 대비 시험문제 3 문제 1

# count = 0
# while True:
#     a = input("number")
#     count += 1
#     if a == "exit":
#         break
# print(str(count)+ "번 입력함")

#자격증 대비 시험문제 3 문제 2

# a = len(input("문자열1입력"))
# b = len(input("문자열2입력"))
#
# print(a/b)

#자격증 대비 시험문제 3 문제 3

# 6

#자격증 대비 시험문제 3 문제 4

# arr = input().split()
# print(arr)
#
# print(arr[-1::-1])

#자격증 대비 시험문제 3 문제 5

# a = 0
# b = 1
# for i in range(4):
#     a = a+2
#     for i in range(1,10,2):
#         print(a,'x',i,'=',i*a)

#계산기 만들기

# import sys
# from PyQt5.QtWidgets import *
# from PyQt5 import uic
# Calui = "c:/jungyunhwan/jungyunhwan.ui"
#
# class MainDialog(QDialog):
#     def __init__(self):
#         QDialog.__init__(self, None)
#         uic.loadUi(Calui, self)
#
#         self.pushButton.clicked.connect(self.NumClicked)
#         self.pushButton_2.clicked.connect(self.NumClicked_2)
#         self.pushButton_3.clicked.connect(self.NumClicked_3)
#         self.pushButton_4.clicked.connect(self.NumClicked_4)
#         self.pushButton_5.clicked.connect(self.NumClicked_5)
#         self.pushButton_6.clicked.connect(self.NumClicked_6)
#         self.pushButton_7.clicked.connect(self.NumClicked_7)
#         self.pushButton_8.clicked.connect(self.NumClicked_8)
#         self.pushButton_9.clicked.connect(self.NumClicked_9)
#         self.pushButton_10.clicked.connect(self.NumClicked_10)
#         self.Plus.clicked.connect(self.NumClicked_11)
#         self.Minus.clicked.connect(self.NumClicked_12)
#         self.Equal.clicked.connect(self.NumClicked_13)
#         self.multiply.clicked.connect(self.NumClicked_14)
#         self.divide.clicked.connect(self.NumClicked_15)
#         self.Clear.clicked.connect(self.NumClicked_16)
#         self.Backspace.clicked.connect(self.NumClicked_17)
#
#
#     def NumClicked(self):
#         p_value = self.q_lineEdit.text()
#         t_value = self.pushButton.text()
#         self.q_lineEdit.setText(p_value + t_value)
#     def NumClicked_2(self):
#         p_value = self.q_lineEdit.text()
#         t_value = self.pushButton_2.text()
#         self.q_lineEdit.setText(p_value + t_value)
#     def NumClicked_3(self):
#         p_value = self.q_lineEdit.text()
#         t_value = self.pushButton_3.text()
#         self.q_lineEdit.setText(p_value + t_value)
#     def NumClicked_4(self):
#         p_value = self.q_lineEdit.text()
#         t_value = self.pushButton_4.text()
#         self.q_lineEdit.setText(p_value + t_value)
#     def NumClicked_5(self):
#         p_value = self.q_lineEdit.text()
#         t_value = self.pushButton_5.text()
#         self.q_lineEdit.setText(p_value + t_value)
#     def NumClicked_6(self):
#         p_value = self.q_lineEdit.text()
#         t_value = self.pushButton_6.text()
#         self.q_lineEdit.setText(p_value + t_value)
#     def NumClicked_7(self):
#         p_value = self.q_lineEdit.text()
#         t_value = self.pushButton_7.text()
#         self.q_lineEdit.setText(p_value + t_value)
#     def NumClicked_8(self):
#         p_value = self.q_lineEdit.text()
#         t_value = self.pushButton_8.text()
#         self.q_lineEdit.setText(p_value + t_value)
#     def NumClicked_9(self):
#         p_value = self.q_lineEdit.text()
#         t_value = self.pushButton_9.text()
#         self.q_lineEdit.setText(p_value + t_value)
#     def NumClicked_10(self):
#         p_value = self.q_lineEdit.text()
#         t_value = self.pushButton_10.text()
#         self.q_lineEdit.setText(p_value + t_value)
#     def NumClicked_11(self):
#         p_value = self.q_lineEdit.text()
#         t_value = self.Plus.text()
#         self.q_lineEdit.setText(p_value + t_value)
#     def NumClicked_12(self):
#         p_value = self.q_lineEdit.text()
#         t_value = self.Minus.text()
#         self.q_lineEdit.setText(p_value + t_value)
#     def NumClicked_13(self):
#         try:
#             result = eval(self.q_lineEdit.text())
#             self.q_lineEdit.setText(str(result))
#         except Exception as e:
#             print(e)
#     def NumClicked_14(self):
#         p_value = self.q_lineEdit.text()
#         t_value = self.multiply.text()
#         self.q_lineEdit.setText(p_value + t_value)
#     def NumClicked_15(self):
#         p_value = self.q_lineEdit.text()
#         t_value = self.divide.text()
#         self.q_lineEdit.setText(p_value + t_value)
#     def NumClicked_16(self):
#         self.q_lineEdit.setText(" ")
#     def NumClicked_17(self):
#         exist_lint_text = self.q_lineEdit.text()
#         exist_lint_text = exist_lint_text[:-1]
#         self.q_lineEdit.setText(exist_lint_text)
#
#
# app = QApplication(sys.argv)
# main_dialog = MainDialog()
# main_dialog.show()
# app.exec_()

#시험 대비 문제 -양쪽에 작은 따옴표 붙이기

# a = input()                 #시험 문제에서 input은 자동으로 넣어주니 프린트 부분에 집중
# print("'"+a+"'")              #문자간 연결은 +로

#시험 대비 문제 -자연수 10의 배수 N개 구하기

# a = input()
# b = 10                    #b 바깥으로 안뺴두면 같은 결과 계속 나오니 주의
#
# for i in range(int(a)):
#     print(b)
#     b = b + 10

#시험 대비 문제 -두 수의 차 구하기

# a, b = input().split()           #split으로 한번에 입력받고 계산을 위해 int로 변환
# a = int(a)
# b = int(b)
# print(a-b)

#시험 대비 문제 -문자열 s 거꾸로 출력하기

# s = input()
# for i in range(len(s)-1, -1, -1):     #len의 경우 -1을 해주는 이유는 이하이기 떄문에 / for문 안에서는 ::이 아닌 ,로 입력
#     print(s[i],end='')

#시험 대비 문제 - 길이가 n인 배열에서 arr에서 인접한 숫자 중 두번째 숫자에서 첫번쨰 숫자를 뺀 값을 모두 구하기

# n = int(input())
# arr = input().split()
# for i in range(n):
#     arr[i] = int(arr[i])
# for i in range(len(arr)-1):                           #len은 문자열 길이 세주는 거, -1 for 문안에 넣을 경우 -1 넣어주기
#     print(arr[i+1]-arr[i],end=' ')                    #arr의 i+1번째(현재 반복중인 수에서 1을 더한 값 ex.현재 반복이 1번째일 경우 2번째값임)-arr[i](arr의 i번째)
                                                        #end=' ' 해주면 띄어쓰기
                                                        #별개로 \n의 경우 줄넘김 해줌

#시험 대비 문제 -구구단(2~9단)을 출력하는 코드 완성하기
# a = 1                                             #a를 1로 지정하여 단수 변경 대비
# for i in range(2,10):                             #for문 이용 - 이상,미만 이기 때문에 2와 10을 넣어줌
#     a = a + 1                                     #a = a + 1 = 한 종류의 단이 끝나고 돌아올때마다 1을 더하여 다음 단으로 넘어가게끔 하기
#     for i in range(1,10):                         #for문 이용 - 이상,미만이기 때문에 단수*1이기 때문에 1부터 시작하여 9로 마무리 된다.
#         print(a,"*",i,"=",a*i)                    # a - 현재 단수 / "*" - 곱하기 기호 문자로 넣어주기 / i - 반복이 1부터 9까지 진행되기 때문에 따로 변수를 넣을게 아니라 i 활용
                                                    # "=" - =을 문자로 넣어주기 / a*i 컴퓨터 자체 기능을 통해 연산하게 끔 만든다.

#시험 대비 문제 - n이 입력되면 약수를 구하는 코드 작성
# n = int(input("숫자 입력"))                       #자신이 약수를 구할 숫자 입력
#
# for i in range(1,n+1):                          #for문 이용-이상,미만이기 때문에 n의 약수를 구하는 과정에서 미만에 n을 넣을 경우 n 자신이 생략 되기에 n에 1을 더한 값을 미만에 넣어준다.
#     if n % i == 0:                                # % - 나누고 나온 나머지 값 , // - 몫의 값 , 결국 n을 i로 나눈 나머지 값을 구한다. , == 0 - 나머지 값이 0과 같을 경우에만 다음 줄로 넘어감
#         print(i , end=" ")                      #나머지 값이 0이었던 수들만 출력 된다. if문을 통과했던 i번째의 수만 출력이 됨. , end=" "을 통해서 결과값 사이에 띄어쓰기 넣어주기

#시험 대비 문제 - 키를 입력받고 150cm이상은 true,미만은 false를 출력하는 코드 작성

# a = int(input())                                # int를 이용해 숫자값으로 인식 되게끔 변경
#
# if a >= 150:                                    # >= - a가 150과 같거나 150보다 클 경우 true를 출력한다.
#     print("true")
# else:
#     print("false")                              #150보다 작을 경우 false를 출력한다.

#시험 대비 문제 - 두 개의 정수를 입력 받아 곱과 몫을 출력하는 코드 작성
#
# a = input().split(",")                            #input으로 입력받아야 하는데 int로 감싸고 입력받을 경우 split이 연결이 안되기에 input으로 받아 split으로 연결하고 int는 별개로 사용한다
#
# print(int(a[0])*(int(a[1])))                     #리스트의 경우 int가 전체적으로 안되기에 직접적으로 한 가지 수씩 int를 붙여서 계산한다. 리스트는 배열이 0부터 시작이기에 대괄호 안에 배열의 순서를 입력
# print(int(a[0])//(int(a[1])))                    #몫의 경우 //로 구한다.

#시험 대비 복권 맞추기

# import random
#
# import sys
# from PyQt5.QtWidgets import *
# from PyQt5 import uic
# Calui = "c:/jungyunhwan/lotto.ui"
#
#
#
# a = 0
# t = 0
# user1 = []
#
# success = random.sample(range(1, 46), 7)
# bonus = success.pop(random.randint(0, 5))
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         QDialog.__init__(self, None)
#
#         uic.loadUi(Calui, self)
#         self.pushButton.clicked.connect(self.Clicked)
#
#
#     def Clicked(self):
#         try:
#             global user
#             global success
#             global t
#             global a
#             global user1
#             t = 0
#             a = 0
#             user1 = []
#
#             user = self.lineEdit.text().split(" ")
#             self.result(user)
#         except:
#             self.lineEdit_2.setText("다시 쓰세요")
#
#     def result(self,user):
#         global a
#         global t
#         global bonus
#         global user1
#         for x in user:
#                 if x not in user1:
#                     user1.append(x)
#                 else:
#                     break
#         for i in range(6):
#             for j in range(6):
#                 if int(user[i]) == success[j]:
#                     t = t+1
#         for u in range(6):
#             if int(user[u]) == bonus:
#                 a = a + 1
#             if t == 6:
#                 if len(user1) <= 5:
#                     self.lineEdit_2.setText("다시 입력해주세요")
#                 else:
#                     self.lineEdit_2.setText("1등")
#             elif t == 5:
#                 if a == 1:
#                     if len(user1) <= 5:
#                         self.lineEdit_2.setText("다시 입력해주세요")
#                     else:
#                         self.lineEdit_2.setText("2등")
#                 else:
#                     if len(user1) <= 5:
#                         self.lineEdit_2.setText("다시 입력해주세요")
#                     else:
#                         self.lineEdit_2.setText("3등")
#             elif t == 4:
#                 if len(user1) <= 5:
#                     self.lineEdit_2.setText("다시 입력해주세요")
#                 else:
#                     self.lineEdit_2.setText("4등")
#             elif t == 3:
#                 if len(user1) <= 5:
#                     self.lineEdit_2.setText("다시 입력해주세요")
#                 else:
#                     self.lineEdit_2.setText("5등")
#             elif t <= 2:
#                 if len(user1) <= 5:
#                     self.lineEdit_2.setText("다시 입력해주세요")
#                 else:
#                     self.lineEdit_2.setText("꽝")
#
# app = QApplication(sys.argv)
# main_dialog = MainWindow()
# main_dialog.show()
# app.exec_()


#시험 대비 문제 1

# a = input()                   #input을 통해 값을 입력받음
# print("'"+a+"'")              #print에서 문자로 표현하게끔 해주는 "를 이용하여 '를 문자로서 출력한 뒤 +를 통해서 input으로 입력 받은 a값과 연결해준다.

#시험 대비 문제 2

# n = int(input())
# i = 1
# while n>=i:                   #while 오른쪽에 들어가는건 ~할때까지가 아니라 ~할 경우이므로 진입할 수 있는 조건을 넣어준다.
#     print(10*i)               #n>=i i가 n보다 작을 경우에만 반복을 돌려서 10의 배수를 뽑아낸다.
#     i += 1

#시험 대비 문제 3

# a, b = input().split()        #split의 용도:input받은 값을 리스트로 저장해주거나 입력 순서에 따라 다른 변수에 한번에 넣어준다.
# a = int(a)                    #다만 split을 사용할 경우 앞에 int를 붙일 수 없기에 계산을 목적으로 하는 문제에서는 개별적으로 int를 통해 숫자로 인식되도록 해주어야 한다.
# b = int(b)
# print(a-b)

#시험 대비 문제 4

# s = input()
# for i in range(2,-1,-1):         #for문에서 range 뒤 괄호는 (시작,끝,진행 방법)이다. 진행방법에 -1을 넣어주면 거꾸로 출력이 되고 시작과 끝에는 몇번째부터 어디까지 거꾸로 출력할지를 정해준다.
#     print(s[i], end='')

#번외-별찍기 피라미드

# a = 1
# b = 4
# for i in range(4):
#     print(" "*b+"*"*a+" "*b)    #문자열에 *해주면 그만큼 더 출력되는걸 이용한다.
#     b -= 1                      # b -= 1는 b = b - 1과 같은 효과를 준다. (+도 마찬가지)
#     a += 2

#시험 대비 문제 5

# n = int(input())
# arr = input().split()
# for i in range(n):
#     arr[i] = int(arr[i])
# for i in range(n-1):
#     print(arr[i+1]-arr[i],end=' ')            #arr에서 없는 값을 호출했으므로 out of range가 나올 것이기에 위에 for문에서 -1을 해준다.

#시험 대비 문제 6

# a = 2                                         #이렇게 풀기는 했으나 이거보다 간단하게 풀 수 있으므로 위쪽 문제를 참고
# b = 1
#
# for i in range(8):
#     for i in range(9):
#         print(a,"*",b,"=",a*b)
#         b += 1
#     a += 1
#     b = 1

#시험 대비 문제 7

# a = int(input())
#
# for i in range(1,a+1):
#     if a % i == 0:                        #이 또한 위 문제 참고
#         print(i, end=" ")

#시험 대비 문제 8

# a = int(input())
#
# if a >= 150:
#     print("true")
# else:
#     print("false")


#시험 대비 문제 1

# a = 0
# b = 0
#
# for i in range(10):
#     a += 1
#     b += a
#
# print(b)

#시험 대비 문제 2

# a = input("첫번째 문자열을 입력해주세요")
# b = input("두번째 문자열을 입력해주세요")
#
# if len(a) >= len(b):
#     print(a)
# else:
#     print(b)

#시험 대비 문제 3

# n = int(input())
# a = 0
#
# for i in range(n):
#     print("*"*n+" "*a)
#     a += 1
#     n -= 1

#시험 대비 문제 4

# a = int(input("첫번째 숫자"))
# b = int(input("두번째 숫자"))
#
# if a == b:
#     print(a+b)
# else:
#     print(b-a)

#시험 대비 문제 5

# a = input("숫자입력")
#
# print(a[-1::-1])              #문자열 거꾸로 출력 [진행방향:도착지:얼마만큼씩]
                                #[-1::-1]의 경우 -1 방향으로 끝까지(목적지X) -1씩 출력 꼭 참고

#시험 대비 문제 6

# a = input()
# print("'"+a+"'")

#시험 대비 문제 7

# n = int(input())
# i = 1
# while i <= n:
#     print(i*10)
#     i += 1

#시험 대비 문제 8

# a, b = input().split()
# a = int(a)
# b = int(b)
# print(a-b)

#시험 대비 문제 9

# s= input()
# for i in range(2,-1,-1):      #for문에서 range 뒤 괄호는 (시작,끝,진행 방법)이다.
#     print(s[i],end='')        #진행방법에 -1을 넣어주면 거꾸로 출력이 되고 시작과 끝에는 몇번째부터 어디까지 거꾸로 출력할지를 정해준다.

#시험 대비 문제 10

# n = int(input())
# arr = input().split()
# for i in range(n):
#     arr[i] = int(arr[i])
# for i in range(n-1):
#     print(arr[i+1]-arr[i],end=' ')

#시험 대비 문제 11

# for i in range(2,10):
#     for r in range(1,10):
#         print(i,"*",r,"=",i*r)

#시험 대비 문제 12

# a = int(input())
#
# if a >= 150:
#     print("true")
# else:
#     print("false")

#시험 대비 문제 13

# a = input().split(",")
#
# print(int(a[0])*int(a[1]))
# print(int(a[0])//int(a[1]))   #몫은 //로 구한다.

#업다운 게임

# import random
#
# a = random.randint(1,10)
# count = 0
#
# while True:
#     count += 1
#     user = int(input("숫자를 입력"))
#     if user > a:
#         print("다운")
#     elif user < a:
#         print("업")
#     elif user == a:
#         print("맞추셨습니다 정답은", str(a), "입니다.")
#         print(str(count)+"번만에 맞추셨습니다.")
#         break

#어벤져스 캐릭터 맞추기

#if문에서 != 은 같지 않다를 나타낸다.

# import random
#
# Avengers = ["캡틴아메리카","아이언맨","토르","스파이더맨","닥터스트레인지"]
# correct = random.choice(Avengers)
# print("보기:캡틴아메리카/아이언맨/토르/스파이더맨/닥터스트레인지")
# print("보기에 제시된대로 작성하지 않으면 정답처리 되지 않습니다.")
# n = 1
# while True:
#     user = str(input("어벤져스 멤버를 입력"))
#     if user == correct:
#         print("정답입니다. 멤버:"+correct)
#         break
#     elif n == 0:
#         if correct == Avengers[0]:
#             print("힌트:비브라늄 방패")
#         elif correct == Avengers[1]:
#             print("힌트:아크 원자로")
#         elif correct == Avengers[2]:
#             print("힌트:천둥의 신")
#         elif correct == Avengers[3]:
#             print("힌트:우리들의 친절한 이웃")
#         elif correct == Avengers[4]:
#             print("힌트:소서러 슈프림")
#     else:
#         n -= 1
#         print("틀렸습니다 힌트까지 앞으로",str(n+1)+"회")


#2급 시험 대비 문제 1

# def cross_bridge(a):
#     b = 0
#     c = 0
#     for i in range(len(a)):
#         b = b + a[i]
#         if b >= len(a):
#             c = i + 1
#             return c
#
# print(cross_bridge([1,1,2,3,5]))


#2급 시험 대비 문제 2
#
# n = int(input("사각형의 높이"))
# m = int(input("사격형의 너비"))
# a = n*m
# b = n*m

# 1트(오답 가능성 있음)
# for i in range(n):
#     c = []
#     for i in range(m):
#         b -= 1
#         c.append(a-b)
#     print(c[0],c[1],c[2],c[3],c[4])

#2트(정석)
# n = int(input("사각형의 높이"))
# m = int(input("사격형의 너비"))
# b = 0
# a = 1
# for i in range(n):
#     for r in range(a,m+1):
#         b += 1
#         print(r,end = " ")
#         if b >= m:
#             print(" ")
#     m += 5
#     a += 5


#2급 시험 대비 문제 3

# s = int(input("시작"))
# e = int(input("끝"))
#
#
# if s > e:
#     n = s-e+1
#     for i in range(n):
#         for r in range(1,10):
#             print(s,'x',r,'=',r*s)
#         if s > e:
#             s -= 1
# if s < e:
#     n = e-s+1
#     for i in range(n):
#         for r in range(1,10):
#             print(s,'x',r,'=',r*s)
#         if s < e:
#             s += 1

# n = 3
# m = 3
# b = 0
# a = 1
# s = int(input("시작"))
# e = int(input("끝"))
#
# for i in range(3):
#         for r in range(1, 10):
#             b += 1
#             print(s,'x',r,'=',r*s,end=" ")
#             if b >= m:
#                 print("\n")


#디노 런 자동화


# from PIL import ImageGrab, ImageOps
# from numpy import *
# import pyautogui, time
#
# # 전역변수
# replayBtn =(477, 408)
# dino = (257, 454)
# lookBox = (dino[0]+20 ,dino[1], dino[0]+65  ,dino[1]+30)
# pyautogui.click(replayBtn)
#
# def detectObs():
#     image = ImageGrab.grab(lookBox)
#     grayImage = ImageOps.grayscale(image)
#     return array(grayImage.getcolors()).sum()
# count = 0
# while True:
#     # print(pyautogui.position())
#     # time.sleep(0.5)
#     # 장애물이 감지되었을때
#     image = ImageGrab.grab(lookBox)
#     grayImage = ImageOps.grayscale(image)
#     print(array(grayImage.getcolors()).sum())
#     if count > 500 :
#         lookBox = (dino[0] + 17, dino[1], dino[0] + 62 , dino[1] + 30)
#     elif count > 600 :
#         lookBox = (dino[0] + 15, dino[1], dino[0] + 65, dino[1] + 30)
#     else:
#         lookBox = (dino[0] + 20, dino[1], dino[0] + 65, dino[1] + 30)
#     # print(array(grayImage.getcolors()).sum())
#     # #
#     if  1597 != detectObs():
#         pyautogui.keyDown("space")
#         time.sleep(0.096 )
#         # time.sleep(0.5)
#         pyautogui.keyDown("down")
#         pyautogui.keyUp("down")
#
#         # pyautogui.keyUp()
#         # pyautogui.keyDown()
#
#
#     count += 1


    # from selenium import webdriver
    # from urllib.request import urlopen
    # from bs4 import BeautifulSoup as bs
    # from urllib.parse import quote_plus
    # from selenium.webdriver.common.keys import Keys
    # import time
    # import urllib.request
    #
    # driver = webdriver.Chrome('C:\chromedriver\chromedriver')  # 여기에 크롬드라이브 다운로드 받은 경로를 입력한다.
    # driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
    # elem = driver.find_element_by_name("q")
    # elem.send_keys("flying birds")
    # elem.send_keys(Keys.RETURN)
    #
    # # 이미지페이지 끝까지 스크롤링
    # # ----------------------------------------------
    # SCROLL_PAUSE_TIME = 1
    # last_height = driver.execute_script("return document.body.scrollHeight")
    # while True:
    #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #
    #     time.sleep(SCROLL_PAUSE_TIME)
    #
    #     new_height = driver.execute_script("return document.body.scrollHeight")
    #     if new_height == last_height:
    #         try:
    #             driver.find_element_by_css_selector(".mye4qd").click()
    #         except:
    #             break
    #     last_height = new_height
    # # ----------------------------------------------
    # images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
    # count = 1
    #
    # for image in images:
    #     try:
    #         image.click()
    #         time.sleep(2)
    #         imgUrl = driver.find_element_by_xpath(
    #             '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img').get_attribute(
    #             "src")
    #         # urllib.request.urlretrieve(imgUrl, str(count) + ".jpg")
    #         print(imgUrl)
    #         count = count + 1
    #     except:
    #         pass
    #
    # driver.close()

#차트 그리기1 (기본적인 차트에 대한 예시는 matplottlib 사이트에서 탐색)

# from matplotlib import pyplot as plt
# a = ["Seoul", "Paris", "Seattle"]
# b = [55, 25, 55]
#
# plt.plot(a , b )
# # plt.plot(["Seoul", "Paris", "Seattle"], [40, 35, 65])
# plt.xlabel('City')
# plt.ylabel('Response')
# plt.title('Experiment Result')
# # plt.legend(['Mouse', 'Cat'])
# plt.show()

#차트 그리기 2

# import matplotlib.pyplot as plt
#
#
# labels = ['G1', 'G2', 'G3', 'G4', 'G5']
# men_means = [20, 35, 30, 35, 27]
# women_means = [25, 32, 34, 20, 25]
# men_std = [2, 3, 4, 1, 2]
# women_std = [3, 5, 2, 3, 3]
# width = 0.35       # the width of the bars: can also be len(x) sequence
#
# fig, ax = plt.subplots()
#
# ax.bar(labels, men_means, width, yerr=men_std, label='Men')
# ax.bar(labels, women_means, width, yerr=women_std, bottom=men_means,
#        label='Women')
#
# ax.set_ylabel('Scores')
# ax.set_title('Scores by group and gender')
# ax.legend()
#
# plt.show()

#크롤링&차트

# from selenium import webdriver
# from urllib.request import urlopen
# from bs4 import BeautifulSoup as bs
# from urllib.parse import quote_plus
# from selenium.webdriver.common.keys import Keys
# import time
# import urllib.request
# import re
#
# driver = webdriver.Chrome('C:\chromedriver\chromedriver')  # 여기에 크롬드라이브 다운로드 받은 경로를 입력한다.
# driver.get("https://vling.net/search/channel?sort=subscriberCount")
# youtuber = driver.find_elements_by_css_selector(".channel-card-info-title-text")
# sub = driver.find_elements_by_css_selector(".channel-card-info-status-value")
#
# list_youtuber = []
# for i in youtuber:
#     list_youtuber.append(i.text)
# print(list_youtuber)
# list_sub = []
# for i in sub:
#     list_sub.append(i.text)
# list_sub = ' '.join(list_sub).split()
# list_sub_change = []
# for i in list_sub:
#     if i.find(".") > 0:
#         list_sub_change.append(i.replace(".","").replace("만","000"))
#     else:
#         list_sub_change.append(i.replace("만","0000"))
#
# list_sub_change_ex = []
# for i in range(len(list_sub_change)):
#     if i % 3 == 0:
#         list_sub_change_ex.append(int(list_sub_change[i]))
# print(list_sub_change_ex)
#
# driver.close()
#
# from matplotlib import pyplot as plt
#
# plt.plot(list_youtuber , list_sub_change_ex )
# # plt.plot(["Seoul", "Paris", "Seattle"], [40, 35, 65])
# plt.xlabel('Youtuber')
# plt.ylabel('SUB')
# plt.title('Experiment Result')
# # plt.legend(['Mouse', 'Cat'])
# plt.show()



#실패작
# if i.find(".") > 0:
#     for i in range(int(i.find("."))):
#         list_sub = re.sub("\.|만|","",list_sub)
#         print(list_sub+"000")
# else:
#     for i in range(len(list_sub)-int(i.find("."))):
#         list_sub = list_sub.replace("만","")
#         print(list_sub+"0000")


#체스판 조작

# import turtle
# import time
# import random
#
# s = turtle.Screen()
# t = turtle.Turtle()
# s.tracer(0)
# def draw():
#     s.screensize(400, 400)
#     t.penup()
#     t.setposition(-200, 200)
#     t.speed(0)
#     # s.tracer(1)
#     t.hideturtle()
#     t.shape("square")
#     t.shapesize(3)
#     for u in range(10):
#         for i in range(10):
#             t.setposition(t.xcor()+60,t.ycor())
#             if u % 2 == 0 :
#                 if i % 2 == 0:
#                     t.color("red")
#                 else:
#                     t.color("black")
#             else:
#                 if i % 2 == 0:
#                     t.color("black")
#                 else:
#                     t.color("red")
#             t.stamp()
#         t.setposition(-200,t.ycor()-60)
#     t.setposition(-200,200)
# def draw1():
#     s.screensize(400, 400)
#     t.penup()
#     t.setposition(-200, 200)
#     t.speed(0)
#     # s.tracer(1)
#     t.hideturtle()
#     t.shape("square")
#     t.shapesize(3)
#     for u in range(10):
#         for i in range(10):
#             t.setposition(t.xcor()+60,t.ycor())
#             if u % 2 == 0 :
#                 if i % 2 == 0:
#                     t.color("black")
#                 else:
#                     t.color("red")
#             else:
#                 if i % 2 == 0:
#                     t.color("red")
#                 else:
#                     t.color("black")
#             t.stamp()
#         t.setposition(-200,t.ycor()-60)
#     t.setposition(-200,200)

# 토글
# on_key = 0
# def toggle():
#     global on_key
#     if on_key == 1:
#         s.reset()
#         on_key = 0
#     else:
#         draw()
#         on_key = 1
#
# s.onkeypress(toggle, "d")
# s.listen()

# 무한루프
# while True:
#     s.tracer(0)
#     draw()
#     time.sleep(0.2)
#     s.tracer(1)
#     s.tracer(0)
#     draw1()
#     time.sleep(0.2)
#     s.tracer(1)

# s.mainloop()


#자판기 만들기

# money = 50000
# input_money = money
# input_money = int(input("금액을 넣어주세요."))
# money = money - input_money
#
# def loop():
#     global money
#     global input_money
#     while True:
#         print("1. 콜라 - 1100원")
#         print("2. 스프라이트 - 1500원")
#         print("3. 물 - 800원")
#         print("4. 환타 - 1300원")
#         print("5. 코코아 - 3000원")
#         print("6. T.O.P - 6000원")
#         print("0. 반환")
#         menu = int(input("메뉴를 선택하세요."))
#         if menu == 1:
#             input_money = input_money - 1100
#             if input_money < 0:
#                 print("잔액이 부족합니다.")
#                 input_money += 1100
#                 loop()
#         elif menu == 2:
#             input_money = input_money - 1500
#             if input_money < 0:
#                 print("잔액이 부족합니다.")
#                 input_money += 1500
#                 loop()
#         elif menu == 3:
#             input_money = input_money - 800
#             if input_money < 0:
#                 print("잔액이 부족합니다.")
#                 input_money += 800
#                 loop()
#         elif menu == 4:
#             input_money = input_money - 1300
#             if input_money < 0:
#                 print("잔액이 부족합니다.")
#                 input_money += 1300
#                 loop()
#         elif menu == 5:
#             input_money = input_money - 3000
#             if input_money < 0:
#                 print("잔액이 부족합니다.")
#                 input_money += 3000
#                 loop()
#         elif menu == 6:
#             input_money = input_money - 6000
#             if input_money < 0:
#                 print("잔액이 부족합니다.")
#                 input_money += 6000
#                 loop()
#         elif menu == 0:
#             money = money + input_money
#             input_money = 0
#         print("잔액은",input_money,"입니다.")
#         print(money)
#         if input_money <= 0:
#             break
#
# loop()

#터틀 경주

import turtle
import random

player1 = turtle.Turtle()
player2 = turtle.Turtle()
player3 = turtle.Turtle()
draw = turtle.Turtle()
t = turtle.Turtle()
s = turtle.Screen()

draw.penup()
draw.setposition(-300,300)
draw.pendown()
draw.right(90)
draw.pensize(3)
draw.forward(600)

draw.penup()
draw.setposition(300,300)
draw.pendown()
draw.pensize(3)
draw.forward(600)

player1.penup()
player1.setposition(-300,250)
player1.shape("turtle")
player1.shapesize(3)
player1.color("red")
player2.penup()
player2.setposition(-300,0)
player2.shape("turtle")
player2.shapesize(3)
player2.color("blue")
player3.penup()
player3.setposition(-300,-250)
player3.shape("turtle")
player3.shapesize(3)
player3.color("Green")


t.penup()
t.setposition(0,0)
t.hideturtle()

q = s.textinput("질문", "누가 일등인지 예상")

print(q)
def test():
    if player1.xcor() > player2.xcor() and player3.xcor():
        t.write("빨강 승리", font=("굴림체", 30))
        if q == "빨강" or  q == "레드" or q ==  "Red" or  q == "red":
            print("test")
            t.setposition(t.xcor(),t.ycor()-40)
            t.write("예측 성공", font=("굴림체", 30))
        else:
            # print("test")
            t.setposition(t.xcor(),t.ycor()-40)
            t.write("예측 실패", font=("굴림체", 30))
    else:
        if player2.xcor() > player3.xcor():
            t.write("파랑 승리", font=("굴림체", 30))
            if q == "파랑" or q == "블루" or q == "Blue" or q == "blue":
                t.setposition(t.xcor(), t.ycor() - 40)
                t.write("예측 성공", font=("굴림체", 30))
            else:
                t.setposition(t.xcor(), t.ycor() - 40)
                t.write("예측 실패", font=("굴림체", 30))
        else:
            t.write("초록 승리", font=("굴림체", 30))
            if q == "초록" or q == "그린" or q == "Green" or q == "green":
                t.setposition(t.xcor(), t.ycor() - 40)
                t.write("예측 성공", font=("굴림체", 30))
            else:
                t.setposition(t.xcor(), t.ycor() - 40)
                t.write("예측 실패", font=("굴림체", 30))



while True:
    player1.forward(random.randint(1,5))
    player2.forward(random.randint(1,5))
    player3.forward(random.randint(1,5))
    if player1.xcor() >= 300 or player2.xcor() >= 300 or player3.xcor() >= 300:
        if player1.xcor() >= 300:
            test()
        elif player2.xcor() >= 300:
            test()
        elif player3.xcor() >= 300:
            test()
        break

s.mainloop()





