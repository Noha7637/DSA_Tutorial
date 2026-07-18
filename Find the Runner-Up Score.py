if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    y = list(arr)
    y.sort()
    y.reverse()
    sec = 0
    x = y[0]
    for i in range(len(y)):
        if y[i]< x:
            sec = y[i]
            break
    print(sec)
