import re

def parse_shape(s):
  if type(s) == list:
    return [str(x).strip() for x in s]
  s = s.strip()
  if not s:
    return None
  if s[0] != '[' or s[-1] != ']':
    return None
  return [x.strip() for x in re.split(',+', s[1:-1].strip())]

