"Hello"
print("hello")
print("python is awesome!")
print('After all, "tomorrow" is just another day')
print(27)
print(2+7)
print('I am learning python')# I am new here
a="Hello"
print(a)
b=10
print(b)
int(9)
Car="BMW"
car="Jaguwa"
CAR="Honda"
print(Car)
print(car)
print(CAR)
My_Name="Riches Etim"
print(My_Name)
print("Hi There, Welcome to Python")
print("Hi There, \nWelcome to Python!")
print(12345)
print("\t1\t2\t3\t4\t5")
print("Hello\tWorld")
print("Hello World")
a="Give Love"
print(a)
print(len(a))
b="Mark"
name="Shelock here"
print(name)
print(len(name))
print(len(name[9:]))
print(name[9:])
print(name[-4])
print(name[0:3]) # Upper bound Excluded
print(My_Name[0:6])
print(My_Name[3:6])
print(name[::]) #Step Size
print(name[::3])
# [Start: Stop: Step Size]
print(name[0:7:2])
print(name[0:7:3])
print(name[0:7:4])
print(name[::-1])
print(name[::-2])
boy="Sam"
print(boy)
print(boy[1:])
b=(boy[1:])
print("P"+ b)
x="Hello Boo,"
y="Let's go for a walk"
print(x +" " +y)
print(x+"\t"+y)
p="Love it"
print(p.lower())
print(p.upper())
print(p.split())
print(p.split("u"))
print(p.split("v"))
print("My name is {}".format("Etim Riches"))
print("The colors are {} {} {}".format("Red","Yellow","Blue"))
print("The colors are {} {} {}".format("Red,","Yellow, and","Blue"))
print("The colors are {0} {1} {2}".format("Red","Yellow","Blue"))
print("The colors are {0} {0} {0}".format("Red","Yellow","Blue"))
print("The colors are {1} {2} {0}".format("Red","Yellow","Blue"))
print("The colors are {y} {b} {y}".format(r="Red",y="Yellow",b="Blue"))
pie=22/7
print(pie)
print("The value is {}".format(pie))
print("The value is {p}".format(p=pie))
print("The value is {p:2.3f}".format(p=pie))
print("The value is {p:10.5f}".format(p=pie))
name="Mark"
Age="8"
print("{} is {} years old".format(name,Age))
print(f"{name} is {Age} years old") # f-string method 
print(2%3)
print(2**6)
print(2+5*6/2-7)
#list
my_list=["Hello",100,23.80]
print(my_list)
list2=["one","two","three"] #Concantenation
new_list=list2+my_list
print(new_list)
#Indexing and Slicing
students=("Shade","Oreoluwa","Tolulope","Amina")
print(students[0])
print(students[0:2])
print(students[1:])
print(students[::-1])
print(students[-1])
print(students[-2:])
print(students[0:3])
#Editing Lists
fruits=["Mango","Banana","Grapes","Pear"]
print(fruits)
#Replace Value
fruits[0]="Orange"
print(fruits)
#Add Values
fruits.append("Tangerine")
print(fruits)
fruits.append("Lemonade")
print(fruits)
#Remove values
fruits.remove("Pear")
print(fruits)

fruits.pop() #Remove last item
print(fruits)
fruits.pop(1) #Remove an exact item
print(fruits)
#Add one list to another
college_students=["A","B","C","D"]
Grade_Number=[1,2,3,4]
college_students.extend(Grade_Number)
print(college_students)
#build-in functions with the lists
l=[2,1,5,3,6,4,7,8,9,10];
print(l.sort())
print(max(l))
#Define an empty list
empty_list=[]
print(empty_list);
print(type(empty_list));

#Define a dictionary
my_dict={"key1":"value1","key2":"value2"};
print(my_dict)
print(my_dict["key1"]);
alvan={"book":5,"football":1,"work":7}
print(alvan["book"])
#Dictionary with all data types
d={"key1":34,"key2":[15,21,93],"key3":{"Apple":6}}
print(d)
print(d["key2"][2])
print(d["key3"]["Apple"])
 #Editing Dictionary
d={"key1":"temi","key2":"tiwa"}
d["key3"]=400;
print(d)
d["key1"]="lade"
print(d)
#keys, values and items
d={"key1":34,"key2":[15,21,93],"key3":{"Apple":6}}
print(d.keys())
print(d.values())
print(d.items())
#Defining a tuples
t=(1,2,3,4,5)
print(type(t))
print(t)
print(len(t))
#indexing and slicing
m=("Hello",80,46.11,"Hello")
print(m[0:2]) #Upper bound excluded
print(m[1])
print(m[-1])
print(m.count("Hello"))
print(m.count(46.11))
#Difference between List and Tuples
t=[1,2,3,4,5]
print(type(t))
print(t[0])
t[1]=30
print(t)

t=(1,2,3,4,5)
print(type(t))
print(t[0])
#t(0)=10 #Tuples cannot assign to function call

##Set
my_set=set()
print(my_set)
my_set.add("Hello")
my_set.add(23)
print(my_set)
my_set.add("Hello")
print(my_set)
g=(1,2,2,4,5,6,8,9,5,6,3,10)
set(g)
print(set(g))
p=(3,4,6,8,0,3,5,4,7,8,9,1,2,10,"Hello")
print(set(p))
##Boolean
print(3==5)
print(True)
print(9>3)
print(type(True))













































































