import numpy as np

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