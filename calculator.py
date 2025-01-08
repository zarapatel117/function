def add(p,q):
  return  (p+q)
def substract(p,q):
  return  (p-q)
def multiply(p,q):
  return  (p*q)
def division(p,q):
  return  (p/q)
print("a= addition")
print("b= subtration")
print("c= multiplication")
print("d= division")
option= input("choose a opration")

number1=int(input("enter a number"))
number2=int(input("enter another number"))

if option=="a" :
   
   print(add(number1,number2))
elif option=="b" :
  print(substract(number1,number2))

elif option=="c" :
  print(multiply(number1,number2)) 

else:
  print(division(number1,number2))

  
   
  
    


     



    