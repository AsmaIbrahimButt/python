name, char=input("enter the name and character :").split(",")
print(f"length of ur name is {len(name)}")
print(f"character count :{name.lower().count(char.lower())}") #count iscase sensitive

name2="        Asma       "
dots="........"
#lstrip() method
print(name2+dots)
print(name2.lstrip()+dots)
print(name2.rstrip()+dots)
print(name2.strip()+dots)
name.replace(" ","")
name.strip().lower().count(char.strip().lower())
char.strip().lower()