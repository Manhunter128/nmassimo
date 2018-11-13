cont=2
int(cont)

n1=input("Inserire numero: ")
n2=input("Inserire numero: ")
if n1>n2:
 max=n1;
elif n2>n1:
 max=n2
else:
 max=n1

while cont<9:
 n3=input("Inserire numero: ")
 if n3>max:
  max=n3
  cont += 1

print(max)