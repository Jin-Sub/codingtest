Alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
a = input()

for i in Alphabet:
    a = a.replace(i, '*')

print(len(a))
