_FLAT = "b"
_SHARP = "#"
# This is the major scale interval matrix. M[a][b] shows the number of semitones to reach from a to b. It is 1-indexed. For higher values such as 3 to 11, do 3 to 8 then 1 to 11-8=3
_M = [
    [-1,  -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1],  # 0
    [-1,  0,    2,    4,    5,    7,    9,    11,   12],  # 1
    [-1,  2,    0,    2,    3,    5,    7,    9,    10],  # 2
    [-1,  4,    2,    0,    1,    3,    5,    7,    8],   # 3
    [-1,  5,    3,    1,    0,    2,    4,    6,    7],   # 4
    [-1,  7,    5,    3,    2,    0,    2,    4,    5],   # 5
    [-1,  9,    7,    5,    4,    2,    0,    2,    3],   # 6
    [-1,  11,   9,    7,    6,    4,    2,    0,    1],   # 7
    [-1,  12,   10,   8,    7,    5,    3 ,   1,    0],   # 8
    #0    1     2     3     4     5     6     7     8   
]

def to_interval(formula):
  '''
  Construct the intervals from a chord formula. Input is a string like: 1-3-#5.
  
  An example is:
  in: 1-b3-5
  out: [3, 4] # 1 to b3 = 3, b3 to 5 = 4

  '''
  assert(len(formula) > 1) # cant be a chord with 1 note only
  assert(formula[0] == '1') # first always has to be root.

  x = 0 # this becomes -1 for flat, +1 for sharp etc.
  f = 0 # this is negation of x, to compensate for the changing interval

  ans = []
  formula = formula.split('-')
  pos_from = 1
  for c in formula[1:]:
    # extract modifiers
    n = ""
    for c_i in c:      
      if c_i == _FLAT:
        x -= 1
      elif c_i == _SHARP:
        x += 1
      elif c_i.isdigit():
        n += c_i      
    pos_to = int(n)
    pos_to_backup = pos_to
    interval = 0 

    while pos_from > 8 and pos_to > 8:
      pos_from -= 7
      pos_to -= 7
  
    while pos_to > 8:
      #print("F:",pos_from,"\tT:",8)
      interval += _M[pos_from][8]
      pos_to -= 7
      pos_from = 1 
      

    #print("F:",pos_from,"\tT:",pos_to)
    interval += _M[pos_from][pos_to] + x + f  
    ans.append(interval)
    f = -x # the flattening / sharpening affects the next interval too, in opposite way.
    x = 0 # reset modifier
    pos_from = pos_to_backup 
  return ans

Power     = to_interval('1-5')

Sus2      = to_interval('1-2-5')
Sus4      = to_interval('1-4-5')
Add9      = to_interval('1-3-5-9')
MinAdd9   = to_interval('1-b3-5-9')
Add11     = to_interval('1-3-5-11')
Add13     = to_interval('1-3-5-13')

Maj       = to_interval('1-3-5')
Maj6      = to_interval('1-3-5-6')
Maj6_9    = to_interval('1-3-5-6-9')
Maj7      = to_interval('1-3-5-7')
Maj9      = to_interval('1-3-5-7-9')
Maj11     = to_interval('1-3-5-7-9-11')
Maj13     = to_interval('1-3-5-7-9-11-13')

Aug       = to_interval('1-3-5#')
Aug7      = to_interval('1-3-5#-b7')

Min       = to_interval('1-b3-5')
Min6      = to_interval('1-b3-5-6')
Min7      = to_interval('1-b3-5-b7')
Min9      = to_interval('1-b3-5-b7-9')
Min9b5    = to_interval('1-b3-b5-b7-9')
Min11     = to_interval('1-b3-5-b7-9-11')
Min13     = to_interval('1-b3-5-b7-9-11-13')
MinMaj7   = to_interval('1-b3-5-7')
 
Dom7      = to_interval('1-3-5-b7')
Dom7s5    = to_interval('1-3-5#-b7')
Dom7s9    = to_interval('1-3-5-b7-9#')
Dom7s11   = to_interval('1-3-5-b7-11#')
Dom9      = to_interval('1-3-5-b7-9')
Dom11     = to_interval('1-3-5-b7-9-11')
Dom13     = to_interval('1-3-5-b7-9-11-13')

Dim       = to_interval('1-b3-b5')
Dim7      = to_interval('1-b3-b5-bb7')
HalfDim   = to_interval('1-b3-b5-b7')
Min7b5    = HalfDim
     
Hendrix = Dom7s9 # must be root E though :)








