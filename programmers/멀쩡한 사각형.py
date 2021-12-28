# 전체개수에서 가로개수 세로개수를 뺀다.
# 최대공약수가 가로와 세로의 중복된 개수이므로 더해주면 된다.
from math import gcd
def solution(w,h):

    return w*h - (w+h) + gcd(w,h)
