# Геометрическая прогрессия
n = int(input("Введите значение n: "))
b = int(input("Введите значение b: "))
q = int(input("Введите значение q: "))
print(b)
b_prev = b
for i in range(1, n):
    b_two = b_prev * q
print("b_two")
b_prev = b_two

# Арефмитическая прогрессия

n = int(input('Введите n (число элементов):'))
d = int(input('Введите d (разность):') or -2)
a = 2
print((2 * a + d * (n - 1)) * n / 2,
    list(range(a, a + d * (n - 1) + d))

#Задание на 4

def binarySearch(nums, target):
    (left, right) = (0, len(nums) - 1)

    while left <= right:

        mid = (left + right) // 2

        if target == nums[mid]:
            return mid

        elif target < nums[mid]:
            right = mid - 1

        else:
            left = mid + 1

    return -1


if __name__ == '__main__':

    nums = [2, 5, 6, 8, 9, 10]
    target = 5

    index = binarySearch(nums, target)

    if index != -1:
        print('Element found at index', index)
    else:
        print('Element found not in the list')