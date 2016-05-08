import string
import fs
# filesystem wrapper from https://pypi.python.org/pypi/pyfs

LETTERS = list(string.ascii_uppercase)

def split_by_index(arr, i):
  m = [a for j, a in enumerate(arr) if i is not j]
  return arr[i], m

def is_absolute(b, arr):
  a = sum(arr)
  if a == 0 and b == 0:
    return False
  return b / (b + a) > 0.5

def no_absolute(arr):
  for i, a in enumerate(arr):
    if is_absolute(*split_by_index(arr, i)):
      return False
  return True

def solve(N, p):
  
  p = list(map(int, p.split(' ')))
  out = ""
  leaving = 0

  while sum(p) > 0:
    for i, m in enumerate(p):
      for j, k in enumerate(p):
        tmp_out = ""
        tmp = list(p)
        if tmp[i] > 0:
          tmp[i] -= 1
          tmp_out += LETTERS[i]
        else:
          continue
        if tmp[j] > 0:
          tmp[j] -= 1
          tmp_out += LETTERS[j]
        else:
          continue
        if no_absolute(tmp):
          out += tmp_out + " "
          p = tmp
          break
      else:
        if p[i] > 0:
          tmp = list(p)
          tmp[i] -= 1
          if no_absolute(tmp):
            out += LETTERS[i] + " "
            p = tmp
            break

  return out

if __name__ == '__main__':
  #IN_NAME = 'input.txt'
  #IN_NAME = 'A-small-attempt0.in'
  IN_NAME = 'A-large.in'
  OUT_NAME = 'output.txt'

  raw_input = fs.read(IN_NAME)
  print('====> Reading %s' % IN_NAME)

  rows = raw_input.split('\n')
  cases = int(rows[0])
  solution = ''

  j = 1
  for i in range(1, len(rows)-1, 2):
    solution += 'Case #%i: %s\n' % (j, str(solve(int(rows[i]), rows[i+1])))
    j += 1

  fs.write(OUT_NAME, solution)
  print('====> Writing %s' % OUT_NAME)