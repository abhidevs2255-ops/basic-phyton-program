def swap_case(s):
  num=""
  for let in s:
    if let.isupper():
      num+=(let.lower())
    else:
      num+=(let.upper())
  return num

s = input()
result = swap_case(s)
print(result)
