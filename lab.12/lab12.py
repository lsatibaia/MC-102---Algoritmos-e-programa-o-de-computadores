a = input()
b = input()
c = input()
c = c.split()
d = c.copy()
d[0] = int(d[0])
d[1] = int(d[1])
x = d[0]
y = d[1]
e = input()
pixel = []
c[0] = int(c[0])
c[1] = int(c[1])
for i in range(c[1]):
  f = input()
  f = f.split()
  pixel.append(f)

for j in range(c[0]):
  for i in range(c[1]):
    pixel[i][j] = int(pixel[i][j])

auxiliar = pixel.copy()

if a == 'negativo':
  mat = [[0 for i in range(c[0])] for j in range(c[1])]
  for j in range(c[0]):
    for i in range(c[1]):
      mat[i][j] = 255 - pixel[i][j]
  pixel = mat
  print('P2')
  x = str(x)
  y = str(y)
  print(x + ' ' + y)
  print('255')
  d[0] = int(d[0])
  d[1] = int(d[1])
  for j in range(d[0]):
    for i in range(d[1]):
      pixel[i][j] = str(pixel[i][j])
  for i in pixel:
    print(' '.join(i))


if a == 'mediana':
  mat = [[0 for i in range(c[0])] for j in range(c[1])]
  for i in range(0, c[1]):
    for j in range(0, c[0]):
      med = []
      if i == 0:
        if j == 0:
          med.append(pixel[i][j])
          med.append(pixel[i + 1][j])
          med.append(pixel[i][j + 1])
          med.append(pixel[i + 1][j + 1])
          med.sort()
          mat[i][j] = (med[1] + med[2]) // 2
        if 0 < j and j < c[0] - 1:
          med.append(pixel[i][j - 1])
          med.append(pixel[i][j])
          med.append(pixel[i][j + 1])
          med.append(pixel[i + 1][j - 1])
          med.append(pixel[i + 1][j])
          med.append(pixel[i + 1][j + 1])
          med.sort()
          mat[i][j] = (med[2] + med[3]) // 2
        if j == c[0] - 1:
          med.append(pixel[i][j])
          med.append(pixel[i + 1][j])
          med.append(pixel[i][j - 1])
          med.append(pixel[i + 1][j - 1])
          med.sort()
          mat[i][j] = (med[1] + med[2]) // 2
      if 0 < i and i < c[1] - 1:
        if j == 0:
          med.append(pixel[i - 1][j])
          med.append(pixel[i][j])
          med.append(pixel[i + 1][j])
          med.append(pixel[i - 1][j + 1])
          med.append(pixel[i][j + 1])
          med.append(pixel[i + 1][j + 1])
          med.sort()
          mat[i][j] = (med[2] + med[3]) // 2
        if 0 < j and j < c[0] - 1:
          med.append(pixel[i - 1][j - 1])
          med.append(pixel[i][j - 1])
          med.append(pixel[i + 1][j - 1])
          med.append(pixel[i - 1][j])
          med.append(pixel[i][j])
          med.append(pixel[i + 1][j])
          med.append(pixel[i - 1][j + 1])
          med.append(pixel[i][j + 1])
          med.append(pixel[i + 1][j + 1])
          med.sort()
          mat[i][j] = med[4]
        if j == c[0] - 1:
          med.append(pixel[i - 1][j])
          med.append(pixel[i][j])
          med.append(pixel[i + 1][j])
          med.append(pixel[i - 1][j - 1])
          med.append(pixel[i][j - 1])
          med.append(pixel[i + 1][j - 1])
          med.sort()
          mat[i][j] = (med[2] + med[3]) // 2
      if i == c[1] - 1:
        if j == 0:
          med.append(pixel[i][j])
          med.append(pixel[i - 1][j])
          med.append(pixel[i][j + 1])
          med.append(pixel[i - 1][j + 1])
          med.sort()
          mat[i][j] = (med[1] + med[2]) // 2
        if 0 < j and j < c[0] - 1:
          med.append(pixel[i][j - 1])
          med.append(pixel[i][j])
          med.append(pixel[i][j + 1])
          med.append(pixel[i - 1][j - 1])
          med.append(pixel[i - 1][j])
          med.append(pixel[i - 1][j + 1])
          med.sort()
          mat[i][j] = (med[2] + med[3]) // 2
        if j == c[0] - 1:
          med.append(pixel[i][j])
          med.append(pixel[i - 1][j])
          med.append(pixel[i][j - 1])
          med.append(pixel[i - 1][j - 1])
          med.sort()
          mat[i][j] = (med[1] + med[2]) // 2
  pixel = mat
  print('P2')
  for j in range(c[0]):
    for i in range(c[1]):
      pixel[i][j] = str(pixel[i][j])
  c[0] = str(c[0])
  c[1] = str(c[1])
  print(c[0] + ' ' + c[1])
  print('255')
  for i in pixel:
    print(' '.join(i))


if a == 'edge-detect': 
  mat = [[0 for i in range(c[0] - 2)] for j in range(c[1] - 2)]
  for i in range(1, c[1] - 1):
    for j in range(1, c[0] - 1):
      l1 = ((-1) * pixel[i - 1][j - 1]) + ((-1) * pixel[i - 1][j]) + ((-1) * pixel[i - 1][j + 1])
      l2 = ((-1) * pixel[i][j - 1]) + (8 * pixel[i][j]) + ((-1) * pixel[i][j + 1])
      l3 = ((-1) * pixel[i + 1][j - 1]) + ((-1) * pixel[i + 1][j]) + ((-1) * pixel[i + 1][j + 1])
      s = l1 + l2 + l3
      if s <= 0:
        mat[i - 1][j - 1] = 0 
      if s >= 255:
        mat[i - 1][j - 1] = 255
      if 0 < s and s < 255:
        mat[i - 1][j - 1] = s
  pixel = mat
  x = x - 2
  y = y - 2
  print('P2')
  x = str(x)
  y = str(y)
  print(x + ' ' + y)
  print('255')
  d[0] = int(d[0])
  d[1] = int(d[1])
  for j in range(0, d[0] - 2):
    for i in range(0, d[1] - 2):
      pixel[i][j] = str(pixel[i][j])
  for i in pixel:
    print(' '.join(i))


if a == 'blur':
  mat = [[0 for i in range(c[0] - 2)] for j in range(c[1] - 2)]
  for i in range(1, c[1] - 1):
    for j in range(1, c[0] - 1):
      l1 = (pixel[i - 1][j - 1] + pixel[i - 1][j] + pixel[i - 1][j + 1])
      l2 = (pixel[i][j - 1] + pixel[i][j] + pixel[i][j + 1])
      l3 = (pixel[i + 1][j - 1] + pixel[i + 1][j] + pixel[i + 1][j + 1])
      s = (l1 + l2 + l3) // 9
      if s <= 0:
        mat[i - 1][j - 1] = 0 
      if s >= 255:
        mat[i - 1][j - 1] = 255
      if 0 < s and s < 255:
        mat[i - 1][j - 1] = s
  pixel = mat       
  x = x - 2
  y = y - 2
  print('P2')
  x = str(x)
  y = str(y)
  print(x + ' ' + y)
  print('255')
  d[0] = int(d[0])
  d[1] = int(d[1])
  for j in range(0, d[0] - 2):
    for i in range(0, d[1] - 2):
      pixel[i][j] = str(pixel[i][j])
  for i in pixel:
    print(' '.join(i))


if a == 'sharpen':
  mat = [[0 for i in range(c[0] - 2)] for j in range(c[1] - 2)]
  for i in range(1, c[1] - 1):
    for j in range(1, c[0] - 1):
      l1 = ((-1) * pixel[i - 1][j])
      l2 = ((-1) * pixel[i][j - 1]) + (5 * pixel[i][j]) + ((-1) * pixel[i][j + 1])
      l3 = ((-1) * pixel[i + 1][j])
      s = l1 + l2 + l3
      if s <= 0:
        mat[i - 1][j - 1] = 0 
      if s >= 255:
        mat[i - 1][j - 1] = 255
      if 0 < s and s < 255:
        mat[i - 1][j - 1] = s
  pixel = mat
  x = x - 2
  y = y - 2
  print('P2')
  x = str(x)
  y = str(y)
  print(x + ' ' + y)
  print('255')
  d[0] = int(d[0])
  d[1] = int(d[1])
  for j in range(0, d[0] - 2):
    for i in range(0, d[1] - 2):
      pixel[i][j] = str(pixel[i][j])
  for i in pixel:
    print(' '.join(i))
