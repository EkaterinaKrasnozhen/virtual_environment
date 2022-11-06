
def sum_float(num):
    sum = 0
    for i in num:
        sum += int(i)
    return(sum)

#print(sum_float('123'))


def multi_N(n):
    result = [1, ]
    if n == 0:
        print(0)
    else:
        for i in range(2, n+1):
            res = i*result[i-2]
            result.append(res)
        return(result)


#print(multi_N(3))