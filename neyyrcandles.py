'''
a candles, burn for 1 hour
b candles make one candle
'''
a, b=map(int, input().split())
time=a
while a>=b:
    time+=(a//b)
    a=(a//b)+(a%b)
print(time)