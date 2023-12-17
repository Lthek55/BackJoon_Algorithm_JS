def solution(spell, dic):
    pivot_dic = [''.join(sorted(i)) for i in dic]
    pivot_spell = ''.join(sorted(spell))
    
    return 1 if pivot_spell in pivot_dic else 2