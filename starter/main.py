import fs

def solve(input):
  cols = input.split(' ')
  # ###############
  # Code goes here
  # ###############
  return input

if __name__ == '__main__':
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