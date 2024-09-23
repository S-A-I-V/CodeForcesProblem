def lexicalOrder(n):
   result = []
   num = 1
   for _ in range(n):
      result.append(num)
      if num * 10 <= n:
           num *= 10
      else:
        if num >= n:
            num //= 10
        num += 1
        while num % 10 == 0:
           num //= 10
   return result
n=int(input())
k=int(input())
reql=lexicalOrder(n)
print(reql[k-1])