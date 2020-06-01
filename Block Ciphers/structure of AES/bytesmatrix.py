def bytes2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    tab = []
    for i in range(0,4):
        for j in range(0,4):
            tab.append(matrix[i][j])
    return tab

def tochr(tab):
    flag = ""
    for x in tab:
        flag += chr(x)
    return flag

matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

print(tochr(matrix2bytes(matrix)))
# print(sum(matrix, []))