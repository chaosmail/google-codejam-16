import fs

def solve(input):
  cols = input.split(' ')

  needs_people = 0  
  shy_max = int(cols[0])
  shy_people = str(cols[1])

  for i, col in enumerate(shy_people):
    if int(col) != 0:
      has_people = sum(map(int, shy_people[:i]))
      if has_people + needs_people < i:
        needs_people += i - (has_people + needs_people)

  return needs_people

if __name__ == '__main__':
  IN_NAME = 'A-large-practice.in'
  OUT_NAME = 'output.txt'

  raw_input = fs.read(IN_NAME)
  print('====> Reading %s' % IN_NAME)

  rows = raw_input.split('\n')
  cases = int(rows[0])
  solution = ''

  for i, row in enumerate(rows):
    if i == 0: continue
    if i == len(rows) - 1: continue
    solution += 'Case #%i: %s\n' % (i, str(solve(row)))

  fs.write(OUT_NAME, solution)
  print('====> Writing %s' % OUT_NAME)