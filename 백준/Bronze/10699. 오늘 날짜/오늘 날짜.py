from datetime import datetime

def solution():
    now = datetime.now()
    result = now.strftime("%Y-%m-%d")
    print(result)

if __name__ == '__main__':
    solution()
