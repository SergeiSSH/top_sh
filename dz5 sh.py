#1
start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

if start > end:
    start, end = end, start

for number in range(start, end + 1):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            print(number, end=" ")
print()

#2
for i in range(1, 11):
    for n in range(1, 11):
        print(str(n) + " * " + str(i) + " = " + str(n * i), end="\t")
    print()

#3
start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

if start > end:
    start, end = end, start

for i in range(start, end + 1):
    for n in range(1, 11):
        print(str(i) + " * " + str(n) + " = " + str(i * n), end="\t")
    print()

