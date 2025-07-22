def islegal_age(age):
    islegal = age >= 18
    return f"age is {age}, and is legally {islegal}"
    
#print(islegal_age(18))

def capital_list(word):
    cap_word = [cword.upper() for cword in word]
    return cap_word
    
    
#print(capital_list(["abcfryg"]))

# this function returns the last letter of the word capital 
def capital_last(word):
    
    if word[-1]:
        return word[:-1] + word[-1].upper()
   
#print(capital_last("rujgswtggh"))

def lower_last(word):
    
    if word[-1]:
        return word[:-1] + word[-1].lower()
        
#print(lower_last("gyyuhgW"))

def capital_word(word):
    
    if word.lower():
        return word.upper()
        
#print(capital_word("ghyyjjftt"))

def lower_word(word):
    
    if word.upper():
        return word.lower()
    
    elif word.upper() and word.lower():
        return word.lower()

#print(lower_word("DRHUUHg"))

def upper_lower(string):
    
    if string.lower() and string.upper():
        return string.upper()
 
#print(upper_lower("fyteSdgu"))


def kilometer(value):
    
    m = value * 1.60934
    return m 

#print(kilometer(50))


def miles(value):
    
    k = value / 1.60934
    return k

#print(miles(100))

def has_a(word):
    
    is_a = [is_word.count("a") > 0 or is_word.count("A") > 0 for is_word in word]
    return is_a
    
words = ["racoon", "plAy", "crocodile", "bird", "cat"]
#print(has_a(words))

#this function filters out the list that has numbers greater than 100
   
def great_100(nums):
    
    fil_num = [num for num in nums if num > 100]
    return fil_num

list_nums = [100, 200, 101, 99, 77, 55, 47, 28, 169, 293, 53]
#print(great_100(list_nums))

nums = [100, 12, 165, 374, 100, 533, 120, 174, 38, 22, 65]

#this function gives us the boolean results based on a condition that filter the list if the list has numbers greater than 100
def boolean_100(nums):
    
    filter_100 = [num > 100 for num in nums]
    return filter_100

#print(boolean_100(nums))

# this function returns a boolean list that has values based on whether if the values capital or not

def is_capital(words):
    
    capital_list = [word.isupper()  for word in words]
    return capital_list
    
char = ["ft", "ET", "DE", "RT", "yT", "Tu"]
#print(is_capital(char))

# this function changes a list of words into lower letters

def list_lower(words):
    
    change = [word.lower() for word in words]
    return change

names = ["Ahmed", "Youssef", "raGab", "MaHer"]
#print(list_lower(names))

# this function checks if a list contains elements with lower letters, if yes it will return true on this element with lower letter, otherwise it will return false

def is_lower(words):
    
    check_lower = [word.islower() for word in words]
    return check_lower

students = ["SAMEER", "Younes", "reda"]
#print(is_lower(students))
    

def cap_last(word):
    last_word = [words[:-1] + words[-1].upper() for words in word]
    return last_word

#print(cap_last(["abcdefg"]))

def second_upper(word):
    
    if word[-2]:
        return word[:-2] + word[-2].upper() + word[-1]
        
#print(second_upper("abriddff"))

def third_upper(word):
    
    if word[-3]:
        return word[:-3] + word[-3].upper() + word[-2] + word[-1] 
        
#print(third_upper("abcdefauyg"))

def reverse_word(word):
    
    return ' '.join(word.split()[::-1])
    
#print(reverse_word("this is the world"))

def reverse_letter(word):
    
    return word[::-1]
    
#print(reverse_letter("World"))

def omit_fletter(word):
    
    return word[1:]

#print(omit_fletter("World"))

def omit_sletter(word):
    
    return word[0:1] + word[2:]

#print(omit_sletter("world"))

def omit_tletter(word):
    
    return word[:2] + word[3:]
    
#print(omit_tletter("world"))

#this function omits the fourth letter from the word

def omitOfFourth(word):
    
    return word[:3] + word[4:]

#print(omitOfFourth("Girrafe"))

def upperOfThirds(word):
    
    change = ''.join(
        word[i].upper() if i % 3 == 0 else word[i]
        for i in range(len(word))
        )
    return change
    
#print(upperOfThirds("Greater"))

def check_type(value):
    
    return type(value)

#print(check_type(4))

def Calclist1(looping):
    
    print("The first loop: ")
    for loop in looping:
        print(loop * 2)
        
    print("-------------------")
    
    print("The second loop: ")
    for loop2 in looping:
        print(loop2 * 4)
    
    return loop2
        
        
nums = [3, 6, 9, 11]
#print(Calclist1(nums)) # 

def calclist2(looping):
    result = [(loop * 2, loop * 4) for loop in looping]
    return result 

nums = [4, 6, 8, 10]
#print(calclist2(nums))

def Doublelist(iterate):
    
    double = [i * 2 for i in iterate]
    return double
    

list_num = [4, 10, 15, 18, 62]
#print(Doublelist(list_num))

def Quadlist(elements):
    
    quad = [element * 4 for element in elements]
    return quad 

numbers = [10, 52, 78, 27, 299]
#print(Quadlist(numbers))

def minimum(min_num):
    
    check_num = [min(mins) for mins in min_num]
    return check_num
    
    
min_list = [[4, 1, 6], [5, 7, 9]]
#print(minimum(min_list))

def min_num(num):
    return min(num)

items = [4, 5, 7, 4, 0, -1, -10000]
#print(min_num(items))

def num_type(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
        
#print(num_type(3))

def increlist(listing):
    
    add = [incre + 1 for incre in listing]
    return add

nums_list = [2,4,6,8,10,12]
#print(increlist(nums_list))

def decrelist(decrease):
    
    decre_num = [decre - 1 for decre in decrease]
    return decre_num

dec_list = [10, 9, 8, 7, 6, 5, 4]
#print(decrelist(dec_list))

def Addlist(adding):
    
    result = [add + add for add in adding]
    return result
    
add_list = [10, 20, 30, 40, 50, 60]
#print(Addlist(add_list))

def Half_list(nums):
    halved = [num * 0.5 for num in nums]
    return halved
 
prop_list = [10, 20, 2, 25, 87 , 50]
#print(Half_list(prop_list))

def Division_list(lists):
    
    divide = [x // x for x in lists]
    return divide

num = [44, 28, 91, 102, 199]
#print(Division_list(num))

def square_list(square):
    
    fill_list = [squares * 2 for squares in square]
    return fill_list
    
numbers_list = [5, 8, 9, 18, 46, 2]
#print(square_list(numbers_list))

def One(num):
    return num // num
 
#print(One(10))

def fahrenheit(fahrs):
    
    reverse = [(y * 9//5) + 32 for y in fahrs]
    return reverse

degrees = [25, 40, 35, 45, 50]
#print(fahrenheit(degrees))

def celcius(cel):
    
    reverse = [(x - 32) * 5//9 for x in cel]
    return reverse
    
degree_list = [45, 33, 66, 20, 10, 3]
#print(celcius(degree_list))

def fcapital_list(word):
    
    capitalized = [words[0].upper() + words[1:] for words in word]
    return capitalized

students_b = ["mohamed", "sami", "nader", "youssef", "rami"]
#print(fcapital_list(students_b))

# this function returns the highest and smallest element in the list and it only accepts one list as a parameter


def size_elem(element):
    highest = max(element)
    smallest = min(element)
    return highest, smallest

list_nums = [50, 100, 200, 500, 400, 1000, 24, 843, 12, 9, 2000, 5]
#print(size_elem(list_nums))


def capital(word):
    cap_word = [cword.upper() for cword in word]
    return cap_word
    
    
#print(capital(["abcfryg"]))


def has_a(word):
    
    is_a = [is_word.count("a") > 0 or is_word.count("A") > 0 for is_word in word]
    return is_a
    
words = ["racoon", "plAy", "crocodile", "bird", "cat"]
#print(has_a(words))

#this function filters out the list that has numbers greater than 100
   
def great_100(nums):
    
    fil_num = [num for num in nums if num > 100]
    return fil_num

list_nums = [100, 200, 101, 99, 77, 55, 47, 28, 169, 293, 53]
#print(great_100(list_nums))

nums = [100, 12, 165, 374, 100, 533, 120, 174, 38, 22, 65]

#this function gives us the boolean results based on a condition that filter the list if the list has numbers greater than 100
def boolean_100(nums):
    
    filter_100 = [num > 100 for num in nums]
    return filter_100

#print(boolean_100(nums))

# this function returns a boolean list that has values based on whether if the values capital or not

def is_capital(words):
    
    capital_list = [word.isupper()  for word in words]
    return capital_list
    
char = ["ft", "ET", "DE", "RT", "yT", "Tu"]
#print(is_capital(char))

def list_lower(words):
    
    change = [word.lower() for word in words]
    return change

names = ["Ahmed", "Youssef", "raGab", "MaHer"]
#print(list_lower(names))

# this function checks if a list contains elements with lower letters, if yes it will return true on this element with lower letter, otherwise it will return false

def is_lower(words):
    
    check_lower = [word.islower() for word in words]
    return check_lower

students = ["SAMEER", "Younes", "reda"]
#print(is_lower(students))

def divided_list(nums):
    
    divide = [num / num for num in nums]
    return divide

num_list = [3, 5, 2, 7, 8, 5, 9, 100]
#print(divided_list(num_list))

def add_list(nums):
    
    add = [num + num for num in nums]
    return add

add_num = [2, 3, 7, 10, 50, 20, 2]
#print(add_list(add_num))

def mul_list(nums):
    
    multiple = [num * num for num in nums]
    return multiple
    
list_multi = [2, 5, 4, 100, 200, 372, 33]
#print(mul_list(list_multi))

def mean(nums):
    
    mean_list = sum([num for num in nums]) / len(nums)
    return mean_list
    
num_mean = [400, 500, 666, 457, 987]
#print(mean(num_mean))

def calc_list(lists):
    return sum(lists)
    
adding_list = [2 ,4]
 
#print(calc_list(adding_list))
    
    
def list_com_cal(lists):
    
    calc = [lst for lst in lists if sum(lst)]
    return calc
    
list_cal = [10, 20, 30]
#print(list_com_cal(list_cal))
    
def compound_interest(interests, rate, n, time):
    list_interest = [interest * (1 + rate / n) ** (n * time)
        for interest in interests]
    return list_interest
    
interests = [1000, 5000, 10000, 500000]
#print(compound_interest(interests, 0.10, 1, 5))

def compound_interest_monthly(interests, rate, n, time, deposit):
    interest = [interest * (1 + rate / n) ** (n * time) for interest in interests]
    return interest

num_list = [4000, 5000, 10000, 50000]
print(compound_interest_monthly(num_list, 0.05, 1, 5, 500))







    
    
