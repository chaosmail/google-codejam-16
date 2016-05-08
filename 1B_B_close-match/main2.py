import fs
# filesystem wrapper from https://pypi.python.org/pypi/pyfs

class Term:
  def __init__(self, factors):
    self.factors = factors

  def solve(self):
    result = 0
    for f in self.factors:
      result += f.coeff*f.base**f.exp
    return result

  def __str__(self):
    return " + ".join(map(str, self.factors))

  def __sub__(self, b):
    return Term([Factor(fa.exp, fa.coeff - fb.coeff) for fa, fb in zip(self.factors, b.factors)])

class Factor:
  def __init__(self, exp, coeff):
    self.base = 10
    self.exp = int(exp)
    self.coeff = int(coeff) if coeff != '?' else 0#None

  def __str__(self):
    return "%s*%i^%i" % (self.coeff if self.coeff != None else '?', self.base, self.exp)

def solve(input):
  arr = [[], []]
  cols = input.split(' ')
  for j, col in enumerate(cols):
    for i, c in enumerate(col):
      arr[j].append(Factor(exp=len(col) - i - 1, coeff=c))

  a = Term(arr[0])
  b = Term(arr[1])

  print(a)
  print(b)
  print(a - b)
  print(abs((a - b).solve()))

  return input

if __name__ == '__main__':
  #IN_NAME = 'B-small-attempt2.in'
  IN_NAME = 'input.txt'
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
    solution += 'Case #%i: %s\n' % (i, str(solve(row)))

  fs.write(OUT_NAME, solution)
  print('====> Writing %s' % OUT_NAME)