name_food = set()
count_food = int(input())
for i in range(count_food):
    name_food.add(str(input()))
count_days = int(input())
for i in range(count_days):
    for j in range(int(input())):
        food = str(input())
        if food in name_food:
            name_food.remove(food)
for i in name_food:
    print(i)
