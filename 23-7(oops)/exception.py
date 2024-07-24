# exception handling using try-except
# we can use multiple except statement for 1 try statement
# indentation error,name error,type error,value error, zerodivisionerror
# try-except-else-finally
print("line1")
print("line2")
print("line3")
print("line4")
n1=int(input("enter first number:"))
n2=int(input("enter second number:"))
try:
    print(n1/n2)
    # open("anudip.txt")
# except(ZeroDivisionError) as e:
#     print("error!",e)
# except(FileNotFoundError) as e:
#     print("error!",e)
# except(ZeroDivisionError,FileNotFoundError) as e:
#     print("error!",e)
except:
    print("spmething went wrong!!")
else:
    print("else block")
finally:
    print("finally!!")
print("line5")
print("line6")
