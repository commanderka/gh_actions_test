def sum(a:int, b:int)->int:
  return a+b

def test_sum():
  assert(sum(1,2)==3)
  assert(sum(1,-1)==0)
