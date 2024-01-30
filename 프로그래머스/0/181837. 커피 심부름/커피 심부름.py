def solution(order):
    americano = 0 
    cafelatte = 0
    for idx, coffee in enumerate(order):
        if "americano" in coffee:
            americano += 1
        elif "cafelatte" in coffee: 
            cafelatte += 1
        else: 
            americano += 1
    return americano * 4500 + cafelatte * 5000