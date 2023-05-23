def convert_alphabet(w):
    return w.lower() if w.isupper() else w.upper()
    
str = list(input())
print(''.join(list(map(convert_alphabet, str))))

