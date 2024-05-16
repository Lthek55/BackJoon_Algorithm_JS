num_list = map(int, (input() for _ in range(5)))
pivot_list = [num if num >= 40 else 40 for num in num_list]
print(sum(pivot_list) // 5)