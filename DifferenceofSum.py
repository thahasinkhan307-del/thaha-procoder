def differenceofSum(n,m):
    sum_divisible=0
    sum_not_divisible=0
    for i in range(1,m+1):
        if i%n == 0:
            sum_divisible+=1
        else:
            sum_not_divisible+= i
    return sum_not_divible-sum_divisible
#sample inputs
n=int(input("Enter n:"))
m=int(input("Enter m:"))
result=differenceofSum(n,m)
print("Difference=",result)
