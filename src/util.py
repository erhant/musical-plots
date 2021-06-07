import numpy as np

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
  
def halfsteps_to_stepnames(halfsteps):
  '''
  Converts the halfstep counts to step names, i.e. whole step, half step etc.
  '''
  stepNames = []
  for s in halfsteps:
    if s == 1:
      stepNames.append('T') # tone
    elif s == 2:
      stepNames.append('S') # semitone
    elif s == 3:
      stepNames.append('TS') # tone+semitone
    elif s == 4:
      stepNames.append('TT') # tone+tone
    else:
      return "" # this is ~probably~ a chord if we see >4
  return "("+','.join(stepNames)+")"

def rotate(origin, point, angle_rad):
  """
  Rotate a point counterclockwise by a given angle around a given origin.
  The angle should be given in radians.
  Source: https://stackoverflow.com/questions/34372480/rotate-point-about-another-point-in-degrees-python
  """
  ox, oy = origin
  px, py = point

  qx = ox + np.cos(angle_rad) * (px - ox) - np.sin(angle_rad) * (py - oy)
  qy = oy + np.sin(angle_rad) * (px - ox) + np.cos(angle_rad) * (py - oy)
  return (qx, qy)

# Calculate the center coordinates
def centerCoordinates(m):
  cx = 0.5 # because our first two points are always [0,0] and [1,0]
  cy = 0.5 * np.tan(np.radians((180 - (360/m))/2)) # using the triangle of [0,0], [cx, 0]
  return cx, cy

# Function that returns the coordinates of the center shape
def initialCoordinates(m): 
  OUT = np.zeros((m+1,2))
  # [0,0] and [b,0] will be same no matter what m we give
  OUT[0,0] = 0
  OUT[0,1] = 0
  OUT[1,0] = 1
  OUT[1,1] = 0 
  
  outerAngleRad = np.radians(360/m) # Default: Angle of a regular polygon
  curOuterAngleRad = outerAngleRad
  for i in range(2, m):
    OUT[i,0] = OUT[i-1,0] + np.cos(curOuterAngleRad)
    OUT[i,1] = OUT[i-1,1] + np.sin(curOuterAngleRad)
    curOuterAngleRad += outerAngleRad
  
  OUT[m, 0] = OUT[0, 0]
  OUT[m, 1] = OUT[0, 1]
  return OUT