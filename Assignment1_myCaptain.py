r = int(input("Enter the radius of the circle "))
pi = 3.14159
a= pi*r**2
print("the area of the circle is",a)

filename = input("Input the Filename: ")
split_filename = filename.split('.')
extension = split_filename[-1]
if (extension=="py"):
    print("This is a python file type")



