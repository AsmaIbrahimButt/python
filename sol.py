
i=0
name="asma"
temp=""
##practice
while i<len(name):
     if name[i] not in temp:
      print(f"{name[i]} : {name.count(name[i])} ")
      i=i+1
