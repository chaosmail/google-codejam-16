import fs
# filesystem wrapper from https://pypi.python.org/pypi/pyfs

def solve(input):
  cols = input.split(' ')
  B = int(cols[0])
  M = int(cols[1])

  if M > 2 ** (B - 2):
    return False, []

  solution = [[0] * B for i in range(B) ]
  for i in range(1, B - 1):
    for j in range(i + 1, B):
      solution[i][j] = 1

  val = list(reversed("{0:b}".format(M)))
  for i in range(B - 1, 1, -1):
    j = B - i - 1
    if j <= len(val) - 1:
      solution[0][i - 1] = val[j]

  if M == 2 ** (B - 2):
    for i in range(1, B):
      solution[0][i] = 1

  submission = []

  for i, row in enumerate(solution):
    submission.append("".join(map(str, row)))

  return "POSSIBLE", submission

if __name__ == '__main__':
  #IN_NAME = 'input.txt'
  IN_NAME = 'B-large-practice.in'
  OUT_NAME = 'output.txt'

  raw_input = fs.read(IN_NAME)
  print('====> Reading %s' % IN_NAME)

  rows = raw_input.split('\n')
  cases = int(rows[0])
  solution = ''

  for i, row in enumerate(rows):
    # Skip first row (contains number of entries)
    if i == 0: continue
    # Skip last row (contains only \n)
    if i == len(rows) - 1: continue
    a, b = solve(row)
    if a == 'POSSIBLE':
      solution += 'Case #%i: %s\n%s\n' % (i, str(a), '\n'.join(map(str, b)))
    else:
      solution += 'Case #%i: IMPOSSIBLE\n' % (i)

  fs.write(OUT_NAME, solution)
  print('====> Writing %s' % OUT_NAME)