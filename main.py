my_list = []
swapped = True
num = int(input("Enter Elements?:"))

for i in range(num):
    val = float(input("Enter a number"))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
           swapped = True
           my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

t = tuple(my_list)
print(t)
print(my_list)