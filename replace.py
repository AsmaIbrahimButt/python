#replace and find method
string ="she is a girl"
print(string.replace(" ","_"))
print(string.replace("is","was"))

#find method
#to find the postion of a character
print(string.find("is",1))
pos=string.find("is")
pos2=string.find("is",pos)
print(pos2)