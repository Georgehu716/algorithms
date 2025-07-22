import sys


def check(m, a, b, k) -> bool:
    for (x, y) in zip(a, b):
        needs = (x*m - y)
        if needs > 0:
            k -= needs
    if k < 0:
        return False
    return True


def main():
    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = 0
    l, r = 0, 1e4
    while l <= r:
        m = (l + r) // 2
        if check(m, a, b, k):
            ans = m
            l = m + 1
        else:
            r = m - 1
    print(int(ans))


if __name__ == "__main__":
    main()
