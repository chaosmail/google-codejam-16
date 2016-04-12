import fs

def solve(input):
  n = int(input)
  seen = set()
  hist = set()
  i = 1  

  while True:
    num = i * n

    for s in str(num):
      seen.add(s)

    if len(seen) is 10:
      return num

    if num in hist:
      break

    if i > 1000:
      break

    hist.add(num)
    i += 1

  return 'INSOMNIA'

if __name__ == '__main__':
  IN_NAME = 'A-large.in'
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