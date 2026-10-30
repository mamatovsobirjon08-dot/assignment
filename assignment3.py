def replace_value(values, index, new_value):
    values[index] = new_value
def find_first(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i
        return -1
def summarize(values):
    tupple = (min(values), max(values), sum(values))
    return tupple

num_days = int(input("Enter the number of days: "))
original = []
for _ in range(num_days):
    num_puzzles = int(input("Enter the number of pazzles solved: "))
    original.append(num_puzzles)
updated = original[:]
a = int(input("Enter the index to correct: "))
b = int(input("Enter the new number of pazzles: "))
replace_value(updated, a, b)
target = int(input("Enter the number of puzzles: "))
first_index = find_first(updated, target)
matching_count = updated.count(target)
if first_index == -1:
    index_str = "Target not found"
else:
    index_str = str(first_index) 

minimum, maximum, total = summarize(updated)
sorted_list = sorted(updated)   

print(f"Original: {original}")
print(f"Updated: {updated}")
print(f"Sorted: {sorted_list}")
print(f"Minimum number of puzzles: {minimum}")
print(f"Maximum number of puzzles: {maximum}")
print(f"Total number of puzzles: {total}")
print(f"First matching index: {index_str}")
print(f"Matching values: {matching_count}")

 
