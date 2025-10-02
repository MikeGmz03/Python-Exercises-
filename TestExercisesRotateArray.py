def ritateLeft(d, arr):
  """
  Performs a left rotation on an array.
  Args:
    d: the number of left rotations to perform.
    arr: the array to rotate.
  Returns:
    The rotate array.
  """
  n=len(arr)
  d %=n # handle cases where d is larger tan the array length
  rotated_part = arr [d:]
  wrapped_part = arr[:d]
  return rotated_part + wraped_part
