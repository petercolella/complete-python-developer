picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
]

# for i, row in enumerate(picture):
#     for j, num in enumerate(row):
#         if bool(num):
#             picture[i][j] = '*'
#         else:
#             picture[i][j] = ' '
#     print(''.join(row))

# for row in picture:
#     for j, num in enumerate(row):
#         if bool(num):
#             row[j] = '*'
#         else:
#             row[j] = ' '
#     print(''.join(row))

for row in picture:
    print(''.join(['*' if num else ' ' for num in row]))

# Clean
# Readable
# Predictable
# DRY


for row in picture:
    for num in row:
        if num:
            print('*', end='')
        else:
            print(' ', end='')
    print('')