# HR accepted! Score - 100

def get_max_path(triangle):
    """This function returns the path with max sum"""
    triangle_array = []
    sub_triangle = triangle.strip().split('\n')
    n = len(sub_triangle)
    for l in range(n):
        triangle_array.append([int(x) for x in sub_triangle[l].split(' ')])
    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            triangle_array[i][j] += max(triangle_array[i + 1][j], triangle_array[i + 1][j + 1])
    print(triangle_array[0][0])
    return


t = int(input().strip())
for counter in range(t):
    n = int(input().strip())
    input_tri = " "
    for i in range(n):
        input_tri += input().strip() + '\n'
    get_max_path(input_tri)
