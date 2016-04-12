import fs
import main

if __name__ == '__main__':
  OUT_NAME = 'output.txt'

  raw_input = fs.read(OUT_NAME)
  print('====> Reading %s' % OUT_NAME)

  rows = raw_input.split('\n')
  # assert len(rows)-2 is 5

  nums = set()

  for i, row in enumerate(rows):
    # Skip first row (contains number of entries)
    if i == 0: continue
    # Skip last row (contains only \n)
    if i == len(rows) - 1: continue
 
    cols = row.split(' ')
    assert len(cols) is 10

    num = cols[0]
    assert num not in nums
    assert num[0] == '1' and num[-1] == '1'

    nums.add(num)

    for i in range(9):
      assert not main.is_prime(int(num, 2 + i))

    for i, col in enumerate(cols[1:]):
      assert int(num, 2 + i) % int(col) is 0