# user defined exception handling

def agecheck(age):
    if age>=18:
        print("you can vote")
    else:
        raise ValueError("no")
  
try:  
    agecheck(15)
except ValueError as e:
    print(e)
    