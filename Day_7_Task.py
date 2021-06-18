def getvalue():
    a=int(input("Enter first number:"))
    b=int(input("Enter Second number:"))
    print("Addition of two numbers is:",addition(a,b))
    print("Subtraction of two numbers is:",subtraction(a,b))
    print("Multiplication of two numbers is:",multiplication(a,b))
    print("Division of two numbers is:",division(a,b))
    
def addition(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    return x/y

getvalue()

def printdetails(pat,temp):
    print("Patient Name:",pat)
    print("Patient current temperature:",temp)
    
    
def covid(name,temperature=98):
    patientname=name
    finaltemp=temperature
    printdetails(patientname,finaltemp)

covid("patient1",99)
covid("patient2")
covid("patient3",10)
