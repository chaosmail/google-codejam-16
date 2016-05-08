import fs
# filesystem wrapper from https://pypi.python.org/pypi/pyfs

def solve(input):
  in_arr = [[],[]]
  cols = input.split(' ')
  for j, col in enumerate(cols):
    for i in col:
      if i == '?':
        in_arr[j].append(None)
      else:
        in_arr[j].append(int(i))

  sc_0 = in_arr[0]
  sc_1 = in_arr[1]
  fn_0 = 0
  fn_1 = 0

  not_zero = False

  for i, (num_0, num_1) in enumerate(zip(sc_0, sc_1)):
    if num_0 != None and num_1 != None and num_0 != num_1:
      fn_0 = num_0
      fn_1 = num_1
      break
    if num_0 != None or num_1 != None:
      break

  # print(fn_0, fn_1)

  for i, (num_0, num_1) in enumerate(zip(sc_0, sc_1)):
    if num_0 is None or num_1 is None:
      # Check number after
      if i is 0 or (sc_0[i - 1] is None and sc_1[i - 1] is None):
        if i < len(sc_0) - 1:
          if sc_0[i + 1] != None and sc_1[i + 1] != None:
            if abs(sc_0[i + 1] - sc_1[i + 1]) >= 5 and sc_0[i + 1] > 5:
              if sc_0[i] is None:
                sc_0[i] = 0
              if sc_1[i] is None:
                sc_1[i] = 1
            elif abs(sc_0[i + 1] - sc_1[i + 1]) >= 5 and sc_1[i + 1] > 5:
              if sc_0[i] is None:
                sc_0[i] = 1
              if sc_1[i] is None:
                sc_1[i] = 0
      # Check number before
      elif i > 0 and (sc_0[i - 1] != None and sc_1[i - 1] != None) and fn_0 != 0 and fn_1 != 0:
        if fn_0 > fn_1:
          if sc_0[i] is None:
            sc_0[i] = 0
          if sc_1[i] is None:
            sc_1[i] = 9
        elif fn_0 < fn_1:
          if sc_0[i] is None:        
            sc_0[i] = 9
          if sc_1[i] is None:
            sc_1[i] = 0

    if sc_0[i] is None and sc_1[i] != None:
      sc_0[i] = sc_1[i]
    elif sc_0[i] != None and sc_1[i] is None:
      sc_1[i] = sc_0[i]
    elif sc_0[i] is None and sc_1[i] is None:
      sc_0[i] = 0
      sc_1[i] = 0

  # print(sc_0, sc_1)
    
  return "".join(map(str, sc_0)) + " " + "".join(map(str, sc_1))

if __name__ == '__main__':
  IN_NAME = 'B-small-attempt2.in'
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