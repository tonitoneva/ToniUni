def gen_seq(range_info):
    start, end = [int(x) for x in range_info.split(",")]
    return set(range(start, end +1))


n = int(input())
best_intersection = set()
for _ in range(n):
    line = input().split("-")
    first_set = gen_seq(line[0])
    second_set = gen_seq(line[1])
    current_intersection = first_set.intersection(second_set)
    if len(current_intersection) > len(best_intersection):
        best_intersection = current_intersection

print(f"Longest intersection is {list(best_intersection)} with length {len(best_intersection)}")
