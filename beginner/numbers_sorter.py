import random

start_range = 1
end_range = 100_000
num_elements = 1000


random_list = random.sample(range(start_range, end_range + 1), num_elements)
print(random_list)

sorted_list = sorted(random_list)
print(sorted_list)