def solution():
    inputLoopCount = int(input())
    for i in range(1, inputLoopCount+1) :
        num1, num2 = map(int, input().split())
        result = num1 + num2

        print(f"Case #{i}: {num1} + {num2} =", result)

if __name__ == '__main__':
    solution()
