list_nums = [int(input('Числа: ')) for _ in range(int(input('Количество элементов: ')))]

print(list_nums)
num = int(input('X: '))
right_num = list_nums[0]

for i in list_nums:
    if abs(num - i) < abs(num - right_num):
        right_num = i

print(right_num)