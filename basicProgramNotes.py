
'''
########## OPTION 1
myfile = open("Filename", "w")
#Do something here
myfile.close()
########## OPTION 2
with open("Filename", "w") as myfile:
    #Do something here
'''

myfile = open("C:\\Users\\patri\\PycharmProjects\\GreatCoursesPlus\\MyDataFile", "r")
linefromfile = myfile.readline()
myfile.close()
print(linefromfile)
myfile = open("C:\\Users\\patri\\PycharmProjects\\GreatCoursesPlus\\MyDataFile", "w")
myfile.write("This line is written to the file.")
myfile.close()