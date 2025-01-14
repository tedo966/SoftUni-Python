longest_intersection = set()

for _ in range(int(input())):
    first_range, second_range = input().split("-")
    first_start, first_end = [int(x) for x in first_range.split(",")]
    second_start, second_end = [int(x) for x in second_range.split(",")]

    first_set = set(range(first_start, first_end + 1))
    second_set = set(range(second_start, second_end + 1))

    curr_intersection = first_set.intersection(second_set)

    if len(curr_intersection) > len(longest_intersection):
        longest_intersection = curr_intersection
print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")