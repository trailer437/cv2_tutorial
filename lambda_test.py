# 1~10까지 람다로 리스트 만들어보기.

def plus(a,b) :
    result  = a + b   
    return result

print(plus(1,6))


plus_lambda = lambda a, b: a + b
print(plus_lambda(1,6))

def word_len(w):
    print(len(w))

word_len("Hello World")

word_len = lambda w: len(w)
print(word_len("Hello World"))

def squ(x):
    print(x*x)

squ(3)

squ = lambda x : x*x
print(squ(3))




max_num = lambda x, y : print(x) if x >y else print(y)
max_num(3,2)

my_list = [x*x for x in range(4)]
print(my_list)

my_list_x = list(map(lambda x : x*x, my_list))
print(my_list_x)

list1 = list(map(lambda x: x, range(11)))
print(list1)

list2 = [x for x in range(11) if x %2 == 0]
print(list2)

list3 = list(filter(lambda x : x % 2 == 0, range(11)))
print(list3)

# 람다를 이용해서 list2와 list3을 더하는 list4를 만들어주기.

list4 = list(map(lambda x, y : x+y, list2, list3))
print(list4)


# 연습문제 5: 주어진 숫자의 제곱 또는 세제곱 계산

# 문제: 주어진 숫자가 짝수인 경우에는 제곱하고, 홀수인 경우에는 세제곱한 결과를 반환하는 
# lambda 함수를 작성하세요.

# 정답코드:
# number = 7



squ3 = lambda x : print(x*x) if x%2==0 else print(x*x*x)
squ3(7)


# 연습문제 6:

# 문제: 1~10까지의 숫자 중 lambda를 이용해서
# 숫자를 짝수, 홀수 그리고 0으로 구분하기

list5 = list(map(lambda x, y : x+y, list2, list3))
print(list5)


# **연습문제 1: 리스트의 각 요소에 2를 더한 새로운 리스트 생성**
# 문제: 주어진 리스트의 각 요소에 2를 더한 새로운 리스트를 생성하는 lambda 함수를 작성하세요.
# 정답 코드:

original_list = [1, 3, 5, 7, 9]

list_1 = list(map(lambda x: x + 2, original_list))

# [3, 5, 7, 9, 11]


# **연습문제 2: 홀수인 경우에만 제곱한 리스트 생성**
# 문제: 주어진 리스트에서 홀수인 경우에만 해당 숫자를 제곱한 새로운 리스트를 생성하는 lambda 함수를 작성하세요.
# 정답 코드:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#[1, 2, 9, 4, 25, 6, 49, 8, 81]

list_2 = list(map(lambda x: x if x %2 ==0 else x *x, numbers))



# **연습문제 3: 문자열의 길이가 5보다 큰 경우만 필터링**
# 문제: 주어진 문자열 리스트에서 길이가 5보다 큰 문자열만 필터링하는 lambda 함수를 작성하세요.
# 정답 코드:

words = ["apple", "banana", "kiwi", "orange", "grape"]

['banana', 'orange']

list_3 = list(filter(lambda x: len(x) > 5, words))

# **연습문제 4: 두 리스트의 각 요소를 곱한 리스트 생성**
# 문제: 두 개의 리스트가 주어졌을 때, 각 요소를 곱한 결과로 이루어진 새로운 리스트를 생성하는 lambda 함수를 작성하세요.
# 정답 코드:

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]


# **연습문제 5: 주어진 숫자의 제곱 또는 세제곱 계산**
# 문제: 주어진 숫자가 짝수인 경우에는 제곱하고, 홀수인 경우에는 세제곱한 결과를 반환하는 lambda 함수를 작성하세요.
# 정답 코드:

number = 7
# 343


# 연습문제 6:  
# 문제: 1~10까지의 숫자 중 lamda를 이용해서 숫자를 짝수, 홀수 그리고 0으로 구분하기


list_6 = list(map(lambda x: "0" if x == 0 else ("홀수" if x %2 ==1 else "not 0"), range(11)))
print(list_6)










