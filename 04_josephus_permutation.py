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
