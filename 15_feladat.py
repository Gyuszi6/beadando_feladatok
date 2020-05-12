lst=[]

while True:
    name = input("nev:")
    if name == "0":
        break
    age = int(input("kor:"))
    if age==0:
        break
    height = int(input("magassag:"))
    if height==0:
        break
    unit = (name, age, height)
    lst.append(unit)

lst.sort(key=lambda x:(x[0],-x[1],x[2]))

for unit in lst:
    print(unit)
