people_in_the_circle = [int(x) for x in input().split(" ")]
step = int(input())
killed_people = []
index = step - 1

while len(people_in_the_circle) != 0:
    if index >= len(people_in_the_circle):
        index -= len(people_in_the_circle)
        continue

    killed_people.append(people_in_the_circle[index])
    del people_in_the_circle[index]
    index += step - 1

result = ",".join(map(str, killed_people))
print(f"[{result}]")

# 2

# list_digit = [int(x) for x in input().split(" ")]
# n = int(input())
#
# list_result = []
# index = n - 1
# current_index = index
#
# while len(list_digit) != 0:
#     current_index = current_index % len(list_digit)
#     list_result.append(list_digit[current_index])
#     del list_digit[current_index]
#     current_index += index
# result = ",".join(map(str,list_result))
# print(f"[{result}]")


# 3

people_in_the_circle = [x for x in input().split(" ")]
executed_person = int(input())

killed_people = []
while len(people_in_the_circle) != 0:
    index = executed_person - 1
    if len(people_in_the_circle) <= index:
        index = index % (len(people_in_the_circle))
    killed_people.append(people_in_the_circle[index])
    if len(people_in_the_circle) > 1:
        people_in_the_circle = people_in_the_circle[index+1:] + people_in_the_circle[:index]
    else:
        del people_in_the_circle[index]

result = ",".join(killed_people)
print(f"[{result}]")
