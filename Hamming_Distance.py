def Hamming(x: str, y: str):
  Distance = 0

  # Both strings must be the same length
  if len(x) != len(y):
    raise Exception("x and y must be the same length.")

  # Build list of acceptable characters.
  Bits = ['0', '1']

  # Walk through each string.
  for i in range(len(x)):
    # Check each character is valid.
    if not (x[i] in Bits): raise Exception("Invalid character x = ", x[i])
    if not (y[i] in Bits): raise Exception("Invalid character y = ", y[i])

    # If the characters are different.
    # We have 0 and 1 or 1 and 0.
    # Count distance of 1.
    if x[i] != y[i]: Distance += 1

  return Distance
