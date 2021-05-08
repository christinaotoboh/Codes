# Exercise number 1:

# def is_odd(a):
#     '''
#     returns true if the interger is odd and false if the interger is even
#     '''
#     if a%2==0:
#        return False
#     else: 
#         return True    
  
# a=print(is_odd(65))

# Exercise number 2:

def is_prime(x):
    '''
    Returns True if the number is a prime and false if it is not
    '''
    if x > 1:
        for i in range(2,x):
            if x%i==0:
                return False
            else:
                return True
                break
    else:
        return False
    
print(is_prime(21))


    