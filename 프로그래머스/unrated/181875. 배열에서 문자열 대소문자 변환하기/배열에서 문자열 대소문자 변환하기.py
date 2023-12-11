def solution(strArr):
    return [v.lower() if idx % 2 == 0 else v.upper() for idx , v in enumerate(strArr)]