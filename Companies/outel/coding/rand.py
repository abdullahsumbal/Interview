import random
l = [1,2,3,4,5,6,7]

for _ in range(len(l)):
    first_index  = random.randint(0, len(l)-1)
    second_index = random.randint(0, len(l)-1)
    while(first_index == second_index):
        second_index = random.randint(0, len(l)-1)
    l[first_index] , l[second_index] = l[second_index], l[first_index]

print(l)
