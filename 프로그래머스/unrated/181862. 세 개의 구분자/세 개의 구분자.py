import re

def solution(myStr):
    ans = list(filter(None, re.split("a|b|c",myStr)))
    return [ "EMPTY" ] if len(ans) == 0 else ans