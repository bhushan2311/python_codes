def bin(n):
    if n>=1:
        bin(n//2)
    r=n%2
    print(r,end="")


if __name__ == '__main__':
    n=int(input())
    bin(n)


# OR

# def dec_to_bin(n):
#     return bin(n).replace("0b","")
#
# if __name__ == '__main__':
#     n=int(input())
#     print(dec_to_bin(n))

# --------- Hacker Rank --------------
l = []
def bin(n):
    if n >= 1:
        bin(n // 2)
    r = n % 2
    l.append(r)


if __name__ == '__main__':
    n = int(input())
    bin(n)
    count = 0
    l.remove(l[0])

    for i in l:
        if i == 1:
            count += 1
        else:
            break
    l2 = count

    count = 0

    for i in l:
        if i == 1:
            count += 1
        else:
            count = 0
            continue
    l3 = count

    if l2 > l3:
        print(l2)
    else:
        print(l3)