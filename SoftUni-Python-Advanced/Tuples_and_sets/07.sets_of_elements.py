n, m = map(int, input().split())

n_set = {input() for _ in range(n)}
m_set = {input() for _ in range(m)}

print(*n_set & m_set, sep="\n")
# for _ in range(n):
#     n_set.add(input())
#
# for _ in range(m):
#     m_set.add(input())

# result = n_set.intersection(m_set) # n_set $ m_set
# print(*result, sep="\n")
