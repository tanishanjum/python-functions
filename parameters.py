#positional parameter
def add_numbers(a,b):
    return a+b
result = add_numbers(3,9)
print(result)

#default parameter
def greet(name='world'):
    print('Hello,'+ name +'!')
greet()
greet('tanish')

#keyword parameter
def greet(name,greeting):
    print(greeting +"," + name + "!")
greet(greeting="Hello",name="tanish")

#packing and unpacking of list
s=[1,2,3,4,5,6]
print(s)
print(*s)

#arbitrary parameters in functions(args)
def addition(*args):
    result=1
    for num in args:
        result += num
    return result
print(addition(2,3,4,5,6,7,8,9,10))

#arbitrary parameters in functions(kwargs)
def student_info(**kwargs):
    for key,value in kwargs.items():
        print(key + ":" + value)
student_info(name="tanish", age="18",clg="BITM")

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("enter the factorial number"))
print(factorial(n))

def prime(n):
    if(n==1):
        return False
    elif(n==2):
        return True
    else:
        for x in range(2,n):
            if (n%x==0):
                return False
        return True
n=int(input('enter the nor'))
print(prime(n))

def reverse_string(string):
    return string[::-1]
string=input("enter the string")
reversestring=reverse_string(string)
print(reverse_string(string))

num=int(input('enter the number'))
def is_armstrong(num):
    num_digits=len(str(num))
    armstrong_sum=0
    temp=num
    while temp>0:
        digit=temp%10
        armstrong_sum+=digit**num_digits
        temp//=10
    return num==armstrong_sum
print(is_armstrong(num))

def count_vowels(string):
    vowels="a,e,i,o,u,A,E,I,O,U"
    count=0
    for char in string:
        if char in vowels:
            count+=1
    return count
string=input('enter the string')
print(count_vowels(string))

def get_student_details(student_id):
    studentdatabase = {
        21:{"name": "suhail", "sem": 4, "roll no": "21","grade":"B"},
        22:{"name": "shree", "sem": 4, "roll no": "22","grade":"C"},
        23:{"name": "kiran", "sem":4, "roll no": "23","grade":"B+"},
        24:{"name":"anji", "sem":4,  "roll no":"24","grade":"A+"}
    }

    if student_id in studentdatabase:
        return studentdatabase[student_id]
    else:
        return None
def display_studentdetails(student_id):
    student_details = get_student_details(student_id)
    if student_details:
        print("Student ID:", student_id)
        print("Name:", student_details["name"])
        print("Sem:", student_details["sem"])
        print("Roll no:", student_details["roll no"])
        print("Grade:",student_details["grade"])
    else:
        print("Student ID not found.")
student_id = int(input("enter student ID: "))
display_studentdetails(student_id)


n=int(input('enter the no of times'))
availableofficers = 0
untreatedCrimes= 0

for i in range(n):
    event=int(input())
    if event == -1:
        if availableofficers > 0:
            availableofficers -=1
        else:
            untreatedCrimes+= 1
    else:
        availableofficers+=event

print(untreatedCrimes)

n= int(input('Enter the number of problems: '))
def solved_problems(n):
   solved_problems=0
   unsolved_problem=0
   for i in range(n):
        a=int(input('enter the probality of solving the problem'))
        b=int(input('enter the probality of solving the problem'))
        c=int(input('enter the probality of solving the problem'))
        if a+b+c>=2:
            solved_problems+=1
        else:
                 unsolved_problem-=1

   return solved_problems
print(solved_problems(n))