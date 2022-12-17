import sys


print(sys.version)




def sample(x):
  try:
    print("This is the sample function " + str(x))
    10/x # will throw zero division error
  except ZeroDivisionError:
    # print("This is the sample function " + str(x))
    print("This is a zero division error")  
  except:
    # print("This is the sample function " + str(x))
    print("Please pass in appropriate input")
    

# sample(2)

# sample(0)
# sample("0")



def add(x,y,z):
  return x+y+z


# x=5
# y=6
# z=7
# x+y+z

# x=1
# y=2
# z=3
# x+y+z


  





add(add(5,6,7),add(1,2,3),add(3,4,5))
