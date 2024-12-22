#Array Question 1

exp = [2200,2350,2600,2130,2190]

FebExp = exp[1]-exp[0]
print(FebExp)
FirQuat= exp[0]+exp[1]+exp[2]
print(FirQuat)
Exact = 2000 in exp
print(Exact)
exp.append(1980)
print(exp)
exp[3]=exp[3]-200
print(exp)

#Array Question 2

heros=['spider man','thor','hulk','iron man','captain america']

print(len(heros))
heros.append("black panther")
print(heros)
heros.remove("black panther")
heros.insert(3,"black panther")
print(heros)
heros[1:3]=["doctor strange"]
print(heros)
heros.sort()
print(heros)


#Array Question 3

max = int(input("Enter the max number= "))

odd_numbers=[]

for i in range(1,max):
    if i%2==1:
        odd_numbers.append(i)
print("odd__numbers",odd_numbers)


#PrimeNumber
max = int(input("Enter the max number = "))
prime_number=[]

for num in range(2,max+1):
    is_prime = True
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
         is_prime=False
         break
    if is_prime:
     prime_number.append(num)
print(prime_number)
