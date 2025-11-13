# Name - Devyansh Singh
# Roll No - 2501060034
# Course - BCA
# Semester - 1st
# Subject - Problem Solving with Python
# Assignment : Unit 1 mini project
# Title : Student Profile Console App
# Date - 13/11/2025

#--------------------------------------------------------------------------------------------------------------------------------------------------------

# num1=2
# num2=4
# print(num2 and num1)
# print(num2 or num1 )
# print(not num1>num2)
# print("\\t")

#/\BUGS FIXING/\------------------------------------------------------------------------------------------------------------------------------------------


#TASK 1
print("welcome to the Student Profile Console")
Name = str(input("Enter the full name of the student :"))
Rollno = int(input("Enter the roll number of the student :"))
Prog = str(input("Enter the program of the student :"))
Uni = str(input("Enter the name of the university :"))
City = str(input("Enter the city of the student :"))
Age = int(input("Enter the age of the student :"))
Hobby = str(input("Enter the hobby of the student :"))


#TASK 2
num1 = int(input("enter a number :"))
num2 = int(input("enter second number :"))
print("Arithematic operators to be used on these 2 numbers" "\n")

print(" '+' Operator:" , num1+num2)
print(" '-' Operator:", num1-num2)
print(" '*' Operator:", num1*num2)
print(" '/' Operator:" , num1/num2)
print(" '%' Operator for remainder:" ,num1%num2)
print(" '**' Operator for exponents:" , num1**num2)
print(" '//' Operator for Quotient without remainder:" , num1//num2)

print("\n")

print("Assignment operators ""\n")
num1 += 2
num2 -= 1
a=24

print(" '+=' to add second element to first. eg-(num1+=2):", num1)
print(" '-=' to subtract second element from first. eg-(num2-=1):",num2)
print(" '=' Operator assigns value to a variable. eg-(a=24):",a)

print("\n")

print("Comparison operators")
print(" '>' and '<' Operators for Greater than and Smaller than.","\n"
      ,"eg-(num1>num2):",num1>num2)
print(" '<=' and '>=' Operators for Greater than equal and Smaller than equal.","\n"
      ,"eg-(num2>=num1):" ,num2>=num1 )
print(" '==' Operator checks if two numbers are equal or not ","\n"
      ,"eg-(num1==num2):" , num1==num2)

print("\n")

print("Logical operators")
print(" 'and' operator checks if both the conditions are true it returns True else it returns False.","\n"
      ,"eg-(num2>num1 and num1<num2) :", num2>num1 and num1<num2)
print(" 'or' operator checks if one of the conditions is true it returns True else it returns False.","\n"
      ,"eg-(num2>num1 or num1<num2) :", num2>num1 or num1<num2)
print(" 'not' operator checks if the condition is true it returns False else it returns True","\n"
      ,"eg-(not num1>num2) :", not num1>num2)

print("\n")

print("membership operators")
print(" 'in' checks if the first element is in an element.","\n"
      ,"eg-(num1 not in [1,2,3,4]) :" ,num1 not in [1,2,3,4])
print(" 'not in' checks if the first element is not in an element.","\n"
      ,"eg-(num1 not in [1,2,3,4]) :" ,num1 not in [1,2,3,4])


#TASK 3
print("HELLO" + Name)
print("escape character" "\t" "tab")
print("escape character" "\n" "newline")
print(f"number 1 is {num1} and number 2 is {num2}")


#task 4
text = "this is an example for string functions"
print(text.upper())
print(text.lower())
print(text.count("a"))
print(text.capitalize())
print(text.replace("a","s"))


#TASK 5
print("---------------------------------------------")
print("\t","STUDENT PROFILE SYSTEM")
print("---------------------------------------------")
print("Name:","\t",Name)
print("Course:","\t",Prog )
print("University:","    ", Uni)
print("City:","\t", City)
print("Age:","\t",Age )
print("Hobby:","\t", Hobby)
print("---------------------------------------------")
print("Welcome to Python Programming")


#TASK 6
choice = str(input("enter y if you want to save the profile and n if you don't want to save the profile :"))
if choice == "y" :
    with open("save.txt","w") as f :
        f.write(f"student name :{Name} \n roll number is : {Rollno} \n program is {Prog} \n University : {Uni} \n City is :{City} \n hobby is {Hobby}")
else :
    print("profile not saved")