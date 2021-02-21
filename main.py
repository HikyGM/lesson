string = str(input()).split()
print('\n'.join(int(string[i]) * '*' for i in range(len(string))))
