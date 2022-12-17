# def spam():
#   global eggs
#   eggs = 'spam'

# eggs = 'global'
# spam()
# print(eggs)

def spam(): 
    global eggs
    eggs = 'spam' # eggs is global variable coz global statement is mentioned at the beginning of spam function

def bacon():
    eggs = 'bacon' # eggs is local variable coz assignment statement is mentioned in the function

def ham():
    print(eggs) # eggs is local variable coz assignment statement is not mentioned in the function

eggs = 42 # this is the global
spam()
print(eggs)