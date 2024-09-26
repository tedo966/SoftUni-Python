nums = int(input())
count_positives = []
count_negatives = []
for i in range(nums):
    curr_numm = int(input())
    if curr_numm >= 0:
        count_positives.append(curr_numm)
    else:
        count_negatives.append(curr_numm)
print(count_positives)
print(count_negatives)
print(f"Count of positives: {len(count_positives)}\nSum of negatives: {sum(count_negatives)}")

