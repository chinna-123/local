# when our expected conditions are not matching then our goal is to fail the test

ItemsInCart = 0
# 2 items will be added to cart

if ItemsInCart != 2:
    pass
    # raise Exception("Products cart count not matching")

assert(ItemsInCart == 0)


'''
we write a code and when we think our code may fail but i don't want test case to stop the execution when we come across that failure
then i can wrap that specific code in try-block( code may get fail in future )
it will raise the exception in try block and sends to catch-block
And in catch-block we can write statements like what is an error, 
'''

# try catch block

try:
    with open('test.txt') as reader:
        reader.read()
except:
    print('you came here bcz of failure in ur code')

try:
    with open('test.txt') as reader:
        reader.read()
except Exception as e:
    print(e)
finally:
    print('finally')



'''
finally keyword will run always no matter if there is a failure or pass in our try catch mechanism

'''

