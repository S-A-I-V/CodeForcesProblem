def square_color(coordinate):
    column = ord(coordinate[0]) - ord('a') + 1
    row = int(coordinate[1])
    return (column + row) % 2

def is_same_color(coordinate1, coordinate2):
    return square_color(coordinate1) == square_color(coordinate2)
coordinate1 = "a1"
coordinate2 = "c3"
print(is_same_color(coordinate1, coordinate2))  
coordinate1 = "a1"
coordinate2 = "h3"
print(is_same_color(coordinate1, coordinate2))  
