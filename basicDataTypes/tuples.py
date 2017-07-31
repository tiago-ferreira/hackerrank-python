if __name__ == '__main__':
    value = 0
    n = int(raw_input())
    t = tuple(map(int, raw_input().split()))
    print hash(t)
