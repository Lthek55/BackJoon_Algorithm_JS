def solution(myString, pat):
    pivot = ''.join(["B" if i == "A" else "A" for i in myString])
    return 1 if pivot.find(pat) >= 0 else 0