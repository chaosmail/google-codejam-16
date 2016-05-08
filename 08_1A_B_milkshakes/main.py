import fs
# filesystem wrapper from https://pypi.python.org/pypi/pyfs

def solve(n_flavors, customers):
  # Parse customers to array of int
  customers = [list(map(int, c.split(" "))) for c in customers]
  malted = [0] * n_flavors
  unmalted = [0] * n_flavors

  for c in customers:
    for i in range(1, len(c) - 1, 2):
      flavor = c[i]
      typ = c[i + 1]
      if typ == 0:
        unmalted[flavor - 1] += 1
      elif typ == 1:
        malted[flavor - 1] += 1
      else:
        raise ValueError('%flavor is not 0 or 1')

  return str(malted) + " : " + str(unmalted)

if __name__ == '__main__':
  IN_NAME = 'input.txt'
  OUT_NAME = 'output.txt'

  raw_input = fs.read(IN_NAME)
  print('====> Reading %s' % IN_NAME)

  rows = raw_input.split('\n')
  cases = int(rows[0])
  solution = ''

  i = 1
  case = 1
  while True:
    # End the loop
    if i >= len(rows) - 1:
      break
    n_flavors = int(rows[i])
    n_customers = int(rows[i+1])
    solution += 'Case #%i: %s\n' % (case, str(solve(n_flavors, rows[i+2:i+2+n_customers])))
    i += n_customers + 2
    case += 1

  fs.write(OUT_NAME, solution)
  print('====> Writing %s' % OUT_NAME)