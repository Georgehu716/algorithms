import sys


def main():
    input = sys.stdin.readline

    n = int(input())
    prices = list(map(int, input().split()))
    prices.sort()

    q = int(input())
    for _ in range(q):
        m = int(input())
        # bisect.bisect_right()
        count = binary_search(prices, m)
        print(count)


def binary_search(nums, target):
    l, r = 0, len(nums)
    while l < r:
        m = (l + r) // 2
        if nums[m] <= target:
            l = m + 1
        else:
            r = m
    return l


if __name__ == "__main__":
    main()
