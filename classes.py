
class bike:
    pass
    duke=bike()
    duke.name="RC390"
    duke.cc=390
    print(duke.cc)
    RE=bike()
    RE.name="classic350"
    RE.cc=350
    print(RE.name)

class bike:
    def __init__(self,name,cc):
      self.bike_name=name
      self.bike_cc=cc
    def sound(self):
        print(f"{self.bike_name} is loud")
Duke=bike("RC390",390)
RE=bike("classic350",350)
print(Duke.bike_name)
print(RE.bike_name)
RE.sound()

class animal:
    def __init__(self,name,sound,color,breed,legs):
        self.animal_name=name
        self.animal_sound=sound
        self.animal_color=color
        self.animal_breed=breed
        self.animal_legs=legs
    def animal_sound(self):
         print(f"{self.animal_sound}")

    def animal_type(self):
        if self.animal_legs==4:
            print(Cat.animal_name, Cat.animal_sound, Cat.animal_color, Cat.animal_breed)
            print(Dog.animal_name, Dog.animal_sound, Dog.animal_color, Dog.animal_breed)
            print("It is a land animal")
        elif self.animal_legs==2:
            print(parrot.animal_name, parrot.animal_sound, parrot.animal_color, parrot.animal_breed)
            print("It is a land animal")
        else:
            print("It is a aquarium animal")
            print(Fish.animal_name, Fish.animal_sound, Fish.animal_color, Fish.animal_breed)
Cat=animal("Cat","meow...meow","white","persian",4)
Dog=animal("Dog","bow...boww","brown","german_shepard",4)
Fish=animal("Fish","Hmm....hmmmm","brown","gold_fish",0)
parrot=animal("parrot","teee...teeee","green","cockatoo",2)


animal_legs=int(input('enter the number of legs:'))
if animal_legs==4:

    Dog.animal_type()
elif animal_legs==2:
    parrot.animal_type()
else:
    Fish.animal_type()

class Human:
    def __init__(self,hobby,food):
        self.fav_hobby=hobby
        self.fav_food=food
    def display_info(self):
        print(f"she is a {self.fav_hobby}, and  she likes {self.fav_food}")
class Sada(Human):
    def __init__(self,hobby,food,language):
        super().__init__(hobby,food)
        self.fav_language=language
    def display_info(self):
        super().display_info()
        print(f"language she speaks is {self.fav_language}")
user=Sada("mehendi artist","biriyani","urdu")
user.display_info()

class Human:
    def __init__(self,hobby,food):
        self.fav_hobby=hobby
        self.fav_food=food
    def display_info(self):
        print(f"she is a {self.fav_hobby}, and  she likes {self.fav_food}")
class Sada(Human):
    def __init__(self,hobby,food,language):
        super().__init__(hobby,food)
        self.fav_language=language
    def display_info(self):
       super().display_info()
       print(f"language she speaks is {self.fav_language}")
class metu(Human):
    def __init__(self,hobby,food,work):
        super().__init__(hobby,food)
        self.fav_work=work
    def display_info(self):
        super().display_info()
        print(f" And she likes to work in {self.fav_work}")
class afiza(Human):
    def __init__(self,hobby,food,reading):
        super().__init__(hobby,food)
        self.fav_reading=reading
    def display_info(self):
        super().display_info()
        print(f" And she loves too read {self.fav_reading}")
user1=Sada("mehendi artist","biriyani","urdu")
user1.display_info()
user2=metu("watching movies","fish curry","banking agency")
user2.display_info()
user3=afiza("sleeping","chicken curry","novels")
user3.display_info()

#abstractpets classes pgrm
from zoo import Abstractpets
class PetAnimal(Abstractpets):
    def display_details(self):
        print("PetAnimal details:")
        print("color:",self.color)
        print("number of types:",self.num_types)
        print("sound:",self.sound)
class Birds(Abstractpets):
    def display_details(self):
        print("Birds details:")
        print("color:",self.color)
        print("number of types:",self.num_types)
        print("sound:",self.sound)
class Wildanimals(Abstractpets):
    def display_details(self):
        print("Wildanimals details:")
        print("color:",self.color)
        print("number of types:",self.num_types)
        print("sound:",self.sound)
#parent pgrm zoo
from abc import ABC, abstractmethod
class Abstractpets(ABC):
    def __init__(self,color,num_types,sound):
        self.color=color
        self.num_types=num_types
        self.sound=sound
@abstractmethod
def display_details(self):
    pass
#main program()
from Abstractpets import PetAnimal, Birds, Wildanimals

def main():
    petanimal = PetAnimal(color="white", num_types=2, sound="medium")
    birds = Birds(color="parrot green", num_types=3, sound="melodious")
    wildanimals = Wildanimals(color="brown", num_types=1, sound="scary")

    petanimal.display_details()
    print("\n")
    birds.display_details()
    print("\n")
    wildanimals.display_details()

if __name__ == "__main__":
    main()
from studentdetails import studentdetails
class Student(studentdetails):
    def display_details(self):
        print('student sem')
        print("name",self.name)
        print("usn",self.usn)
        print('rollno',self.rollno)
class Student1(studentdetails):
    def display_details(self):
        print('student sem')
        print("name",self.name)
        print("usn",self.usn)
        print('rollno',self.rollno)
class Student2(studentdetails):
    def display_details(self):
        print('student sem')
        print("name",self.name)
        print("usn",self.usn)
        print('rollno',self.rollno)
class Student3(studentdetails):
    def display_details(self):
        print('student sem')
        print("name",self.name)
        print("usn",self.usn)
        print('rollno',self.rollno)
from abc import ABC
class studentdetails(ABC):
    def _init_(self,sem,name,usn,rollno):
        self.sem=sem
        self.name=name
        self.usn=usn
        self.rollno=rollno
def display_details(self):
   pass
from student_details import Student, Student1, Student2, Student3

def main():
    student = Student( sem=3,name='shifa', usn='3b2r22ec149', rollno=44)
    student1 = Student1(sem=3,name='shobha', usn='3b2r22ec153', rollno=45)
    student2 = Student2(sem=3,name='shree', usn='3b2r22ec154', rollno=46)
    student3 = Student3(sem=3,name='shabbu',usn='3br22ec147', rollno=47)
    student.display_details()
    print("\n")
    student1.display_details()
    print("\n")
    student2.display_details()
    print("\n")
    student3.display_details()
    print("\n")


class User:
    def __init__(self, username, password='Anju..'):
        self._username = username
        self._password = password


    def check_password(self,password):
        return self._password==password

    def change_password(self, new_password):
        self._password =new_password
        print('password changed successfully!')

    def get_username(self):
        return self._username

username = input("Enter your username: ")
user = User(username)
password = input("Enter your password: ")

if user.check_password(password):
    print('Welcome, {}!'.format(user.get_username()))
else:
    print('Password incorrect.')
    change_option=input('Do you wnat to change your password?(yes/no):').lower()
    if change_option=='yes':
        new_password=input('Enter your new password:')
        user.change_password(new_password)
    else:
        print('Goodbye!')

class ComplexNumber:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
    def __add__(self,other):
        return (f"{self.real+other.real}+{self.imaginary+other.imaginary}i")

c1=ComplexNumber(real=2,imaginary=2)
c2=ComplexNumber(real=1,imaginary=2)
print(c1+c2)

class party:
    def __init__(self,name,money):
        self.name=name
        self.money=money
    def __gt__(self,other):
        if self.money>other.money:
            return True
        else:
            return False
p1=party(name="shifa",money=3000)
p2=party(name="shree",money=5000)
if p1>p2:
    print(f"{p1.name} will pay the bill")
else:
    print(f"{p2.name} will pay the bill")



# ATM task program using class 
#main() pgrm
from ATM import ATM
def main():
    atm=ATM()
    print('press ')
    while True:
        print('1 for balance check \n2 for withdraw \n3 for deposit \n4 to Exit')
        choice=int(input('Enter your choice: '))
        if choice==1:
            username=input('Enter your username: ')
            atm.balance(username)
        elif choice==2:
            username=input('Enter your username: ')
            amount=int(input('Enter your amount: '))
            atm.withdraw(username,amount)
        elif choice==3:
            username=input('Enter your username: ')
            amount=int(input('Enter your amount: '))
            atm.deposit(username,amount)
        elif choice==4:
            print('thank you for visiting the ATM!!!!')
            break
        else:
            print('invalid input please try again')

print(main())
# class assigining
class ATM:
    def __init__(self):
        self.user_data=self.load()
    def load(self):
        user_data={}
        with open("test.txt", "r") as file:a
        for line in file:
            username, balance = line.strip().split(',')
            user_data[username] = float(balance)
        print(user_data)
        return user_data

    def update_data(self):
        f=open('test.txt','w')
        for a,b in self.user_data.items():
            f.write(str(a)+','+str(b)+'\n')


    def withdraw(self,username,amount):
        if username in self.user_data:
            if self.user_data[username]<amount:
                print('insufficient funds')
            else:
                self.user_data[username]-=amount
                print('The Available Amount is:',self.user_data[username])
                self.update_data()

    def deposit(self,username,amount):
        self.user_data[username]+=amount
        print('The Available Amount is:', self.user_data[username])
        self.update_data()

    def balance(self,username):
        print('The Available Amount is:', self.user_data[username])
#test.txt file
user1,2000.0
user2,5077.5
user3,1200.75
