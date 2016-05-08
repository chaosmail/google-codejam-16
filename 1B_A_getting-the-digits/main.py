import fs
# filesystem wrapper from https://pypi.python.org/pypi/pyfs
from random import shuffle

def solve(input):
  orig = str(input)
  numbers = ["SIX", "SEVEN", "TWO", "EIGHT", "ZERO", "THREE", "FOUR", "FIVE", "NINE", "ONE"]
  count = [0] * 10

  for i, number in enumerate(numbers):

    while True:
      found = False
      tmp_input = str(input)

      for c in number:
        if c not in tmp_input:
          break
        tmp_input = tmp_input.replace(c, "", 1)
      else:
        found = True

      if not found:
        break

      for c in number:
        input = input.replace(c, "", 1)
      count[i] += 1

  if len(input) > 0:
    print("Fail %s" % input)

  final = [count[4], count[9], count[2], count[5], count[6], count[7], count[0], count[1], count[3], count[8]]

  result = "".join(["".join(str(i)*j) for i, j in enumerate(final) if j > 0])

  return result

if __name__ == '__main__':
  IN_NAME = 'A-large.in'
  #IN_NAME = 'input.txt'
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