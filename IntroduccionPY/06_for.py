nombre=["Ivan", "Jose", "Anna", "Victor", "Rashid"]
selected=[]
encontrado=0

for item in nombre:
    print(item)
    if(item.find("a")):
        encontrado=1
    if(encontrado==1):
        selected+=item
    else:
        encontrado=0
print("Los nombre que contienen la letra a son: ")
for i in selected:
    print(i)


