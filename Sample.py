import random

num_attempts = 5
num_secret=random.randint(1,10)
def difference_num(a):
    c=a-num_secret
    print "difference is",c

for i in range(0,5):
    var_guess = int(input('Guess the random_number:'))
    
    if var_guess < num_secret:
        print"lower value"
        
    elif var_guess>num_secret:
        print"higher value"
        
    else:
        print "Hurray",num_secret
        
    difference_num(var_guess)
    
    #this is sample test
        
            