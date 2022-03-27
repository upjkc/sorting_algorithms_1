
numbers=[5,7,2,3,4,1,9,10]

size=len(numbers)


print("liczby przed",numbers)

while size > 1:
    for i in range(size-1):

        if numbers[i] > numbers[i+1]:

            temp = numbers[i]
            numbers[i] = numbers[i+1]
            numbers[i+1] = temp

    size=(size-1)

print("liczby po",numbers)