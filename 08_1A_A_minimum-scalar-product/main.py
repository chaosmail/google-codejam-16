import fs
# filesystem wrapper from https://pypi.python.org/pypi/pyfs

def dot(a, b):
  if len(a) != len(b):
    raise ValueError('a[%i] and b[%i] have different length' % (len(a), len(b)))
  return sum(map(lambda i: a[i]*b[i], range(len(a))))

def solve(v1, v2):
  v1_coef = sorted(map(int, v1.split(' ')))
  v2_coef = sorted(map(int, v2.split(' ')), reverse=True)
  output = dot(v1_coef, v2_coef)

  return output

if __name__ == '__main__':
  IN_NAME = 'A-large-practice.in'
  OUT_NAME = 'output.txt'

  raw_input = fs.read(IN_NAME)
  print('====> Reading %s' % IN_NAME)

  rows = raw_input.split('\n')
  cases = int(rows[0])
  solution = ''

  case = 1
  for i in range(1, len(rows) - 1, 3):
    solution += 'Case #%i: %s\n' % (case, str(solve(rows[i+1], rows[i+2])))
    case += 1

  fs.write(OUT_NAME, solution)
  print('====> Writing %s' % OUT_NAME)