# # a=['Dog','cat','lion','bird']
# # # print(a[-1])
# # # print(a[0])
# # #python is a zero index language, to get the first item in a list, tuple or dictionary use [0], 
# # # to get the last item use [-1] just as shown above.the corresponding number shows the
# # # will fetch the corresponding item in the list, tuple or string.
# # # name=('Christy',27,'jollof rice')
# # # # print('christy'[3])
# # # print(a[-3])
# # # print(a[0:3])
# # # print(a[:4])
# # # print(a[-1:1])
# # # #a stride takes every index on a sequence. the specified sequence is 1 however you can change it thus
# # # print(a[0:4:3])

# # # numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] #[::3]
# # # print(numbers)
# # # x=list(range(0,10,2))
# # # print(x)
# # #RANGE ALSO HAS THE STRIDE PROPERTIES
# # # print(numbers[::-1])
# # reverse_name='Christiana'
# # print(reverse_name[::-1])
# # #Use the negative stride index will give the reverse index sequence. this can be used to 
# # #get the reverse of numbers or strings 

# # exercises:

# # name='Christiana'
# # print(name[0])
# # print(name[-1])

# filename='Readonly.jpg' [0:-4]
# print(filename)

def is_paliendrome(x):
    for i in x:
         i=x[::-1]
         if x==i:
             return(True)
         else:
                 return(False)
                 
	   
	
print(is_paliendrome('anna'))
print(is_paliendrome('kayak'))
print(is_paliendrome('chrisy'))
print(is_paliendrome('madam'))
print(is_paliendrome('civic'))

