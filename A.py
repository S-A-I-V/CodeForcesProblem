'''
xc yc

be a line midpt

'''
# def kpts(xc, yc, k):
#     points = []
#     total_x = 0
#     total_y = 0
    
#     for i in range(k - 1):
#         x = xc + i
#         y = yc - i
#         points.append((x, y))
#         total_x += x
#         total_y += y
    
#     x_last = xc * k - total_x
#     y_last = yc * k - total_y
#     points.append((x_last, y_last))
#     return points
# t = int(input())
# for _ in range(t):
#     xc, yc, k = map(int, input().split())
#     points = kpts(xc, yc, k)
#     for x, y in points:
#         print(x, y)
def kpts(xc, yc, k):
    points = []
    
    if k % 2 == 1:
        points.append((xc, yc))
        k -= 1  
    
    half_k = k // 2
    for i in range(1, half_k + 1):
        points.append((xc - i, yc))
        points.append((xc + i, yc))
    
    return points
t = int(input())
for _ in range(t):
    xc, yc, k = map(int, input().split())
    points = kpts(xc, yc, k)
    for x, y in points:
        print(x, y)
