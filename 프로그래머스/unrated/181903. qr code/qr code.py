def solution(q, r, code):
    return ''.join([ v for idx, v in enumerate(code) if idx%q == r ])