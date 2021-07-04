import hashlib

string = input('enter your name :\n')
result = hashlib.md5(string.encode())

print('the entered name is :')
print(string)

print("The hash code is : \n", end ="")
print(result.hexdigest())