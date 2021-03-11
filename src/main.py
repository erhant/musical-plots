import numpy as np
import matplotlib.pyplot as plt
import scales
import chords

DIMINISHED_CHORD_COLOR = '#C9C4D9'
MAJOR_CHORD_COLOR = '#CCE7D4'
MINOR_CHORD_COLOR = '#FCD2C2'
ROOT_COLOR = '#5ADD80'
SCALE_MEMBER_COLOR = '#FC8458'
DEFAULT_COLOR = 'white'
TEXT_DEFAULT_COLOR = 'black'

def halfsteps_to_stepnames(halfsteps):
  '''
  Converts the halfstep counts to step names, i.e. whole step, half step etc.
  '''
  stepNames = []
  for s in halfsteps:
    if s == 1:
      stepNames.append('H')
    elif s == 2:
      stepNames.append('W')
    elif s == 3:
      stepNames.append('WH')
    elif s == 4:
      stepNames.append('WW')
    else:
      return "" # this is probably a chord if we see >4
  return "("+','.join(stepNames)+")"

class Notes:
  def __init__(self):
    self.curIdx = 0
    self.notesABC = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    self.notes = ['DO', 'DO#', 'RE', 'RE#', 'MI', 'FA', 'FA#', 'SOL', 'SOL#', 'LA', 'LA#', 'SI']
    assert(len(self.notesABC) == len(self.notes))

  def next(self, halfsteps):
    self.curIdx = (self.curIdx + halfsteps) % len(self.notesABC) 
    return self.notesABC[self.curIdx]

  def read_then_next(self, halfsteps):
    tmp = self.notesABC[self.curIdx] 
    self.curIdx = (self.curIdx + halfsteps) % len(self.notesABC) 
    return tmp

  def read_then_prev(self, halfsteps):
    tmp = self.notesABC[self.curIdx] 
    self.curIdx = (self.curIdx - halfsteps) % len(self.notesABC) 
    return tmp

  def cur(self):
    return self.notesABC[self.curIdx]
  
  def set_cur(self, idx):
    self.curIdx = idx % len(self.notesABC) 

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

def circle_of_fifths(root=None):
  '''
  Creates the circle of fifths, and plots it.

  You can specify a root, it will color the chords.
  '''
  #TODO: add relative minors too
  c = initialCoordinates(12) 
  cx, cy = centerCoordinates(12)
  # Translate the coordinates so that the center is [0,0]
  c[:,0] -= cx
  c[:,1] -= cy
  cx = 0
  cy = 0    

  # rotate 10 degree ccw
  for i in range(len(c)):
    c[i, 0], c[i, 1] = rotate((cx, cy), (c[i, 0], c[i, 1]), np.radians(15))

  ax = plt.axes()

  # Plot the lines, add circles and text
  ax.plot(c[:,0], c[:,1], 'k')

  halfsteps_fifth = 7 # 2 + 2 + 1 + 2
  notes = Notes()
  
  if root == None:
    notes.set_cur(6) # start from 6th so that C is at the top
    for x, y in c: 
      note = notes.read_then_prev(halfsteps_fifth)
      ax.add_patch(plt.Circle((x, y), 0.25, color=DEFAULT_COLOR, fill=True, zorder=5, ec='black'))
      ax.text(x, y, note, c=TEXT_DEFAULT_COLOR, va='center', ha='center', zorder=5)
  else:
    # go to root
    assert(root in notes.notesABC)    
    # TODO: make indexing by root in Notes class
    while notes.cur() != root:
      notes.next(1)
    
    # construct major scale
    majors = []
    dims = []
    minors = []
    majors.append(notes.read_then_next(2)) # I
    minors.append(notes.read_then_next(2)) # ii
    minors.append(notes.read_then_next(1)) # iii
    majors.append(notes.read_then_next(2)) # IV
    majors.append(notes.read_then_next(2)) # V
    minors.append(notes.read_then_next(2)) # vi
    dims.append(notes.read_then_next(1))   # vii*

    notes.set_cur(6) # start from 6th so that C is at the top
    for x, y in c: 
      note = notes.read_then_prev(halfsteps_fifth)
      if note == root:
        ax.add_patch(plt.Circle((x, y), 0.25, color=ROOT_COLOR, fill=True, zorder=5))
      elif note in majors:
        ax.add_patch(plt.Circle((x, y), 0.25, color=MAJOR_CHORD_COLOR, fill=True, zorder=5))
      elif note in minors:
        ax.add_patch(plt.Circle((x, y), 0.25, color=MINOR_CHORD_COLOR, fill=True, zorder=5))
      elif note in dims:
        ax.add_patch(plt.Circle((x, y), 0.25, color=DIMINISHED_CHORD_COLOR, fill=True, zorder=5))
      else:
        ax.add_patch(plt.Circle((x, y), 0.25, color=DEFAULT_COLOR, fill=True, zorder=5, ec='black'))

      ax.text(x, y, note, c=TEXT_DEFAULT_COLOR, va='center', ha='center', zorder=5)
    
  ax.set_title('Circle of Fifths')
  plt.show()

def hexes_of_tenths(halfsteps=None, root=None):
  '''
  Creates the hexes of tenths, and plots it.

  One hex starts from C, the other from B. Tenth is basically a whole step forward.

  You can specify a halfstep sequence to highlight it's notes, together with a root.
  '''
  h1 = initialCoordinates(6) 
  h2 = initialCoordinates(6) 
  hx, hy = centerCoordinates(6)
  h1[:,0] -= hx
  h1[:,1] -= hy 
  h2[:,0] -= hx
  h2[:,1] -= hy 
  hx = 0
  hy = 0 

  # h1 is the outer hex, so we scale it
  HEX_SCALE_FACTOR = 1.6
  h1[:,0] *= HEX_SCALE_FACTOR
  h1[:,1] *= HEX_SCALE_FACTOR

  # rotate the outer h1 hex 30 degrees
  for i in range(len(h1)):
    h1[i, 0], h1[i, 1] = rotate((hx, hy), (h1[i, 0], h1[i, 1]), np.radians(30))

  ax = plt.axes()
  ax.plot(h1[:,0], h1[:,1], 'k')
  ax.plot(h2[:,0], h2[:,1], 'k')

  # inner to outer lines (on same index) 
  for i in range(6): 
    ax.add_line(plt.Line2D([h1[i,0], h2[i, 0]], [h1[i, 1], h2[i, 1]], color='black', linestyle="--"))

  # outer to inner lines (outer to next inner)
  for i in range(5):
    ax.add_line(plt.Line2D([h1[i,0], h2[i+1, 0]], [h1[i, 1], h2[i+1, 1]], color='black', linestyle="--"))
  ax.add_line(plt.Line2D([h1[5, 0], h2[0, 0]], [h1[5, 1], h2[0, 1]], color='black', linestyle="--"))

  notes = Notes() 
  if halfsteps == None or root == None:
    # outer hex
    notes.set_cur(6)
    for x, y in h1: 
      ax.add_patch(plt.Circle((x, y), 0.25, color=DEFAULT_COLOR, fill=True, zorder=5, ec='black'))
      ax.text(x, y, notes.read_then_next(2), c=TEXT_DEFAULT_COLOR, va='center', ha='center', zorder=5)

    # inner hex
    notes.set_cur(5)
    for x, y in h2: 
      ax.add_patch(plt.Circle((x, y), 0.25, color=DEFAULT_COLOR, fill=True, zorder=5, ec='black'))
      ax.text(x, y, notes.read_then_next(2), c=TEXT_DEFAULT_COLOR, va='center', ha='center', zorder=5)
    
    ax.set_title('Hexes of Tenths')
  else:
    assert(root in notes.notesABC)
    # TODO: make indexing by root in Notes class
    while notes.cur() != root:
      notes.next(1)

    # construct the scale
    scaleNotes = []
    for steps in halfsteps:
      scaleNotes.append(notes.read_then_next(steps))
    scaleNotes.append(notes.cur())

    # outer hex
    notes.set_cur(6)
    for x, y in h1: 
      note = notes.read_then_next(2)
      if note == root:
        ax.add_patch(plt.Circle((x, y), 0.25, color=ROOT_COLOR, fill=True, zorder=5))
      elif note in scaleNotes:
        ax.add_patch(plt.Circle((x, y), 0.25, color=SCALE_MEMBER_COLOR, fill=True, zorder=5))
      else:
        ax.add_patch(plt.Circle((x, y), 0.25, color=DEFAULT_COLOR, fill=True, zorder=5, ec='black'))
      ax.text(x, y, note, c=TEXT_DEFAULT_COLOR, va='center', ha='center', zorder=5)

    # inner hex
    notes.set_cur(5)
    for x, y in h2: 
      note = notes.read_then_next(2)
      if note == root:
        ax.add_patch(plt.Circle((x, y), 0.25, color=ROOT_COLOR, fill=True, zorder=5))
      elif note in scaleNotes:
        ax.add_patch(plt.Circle((x, y), 0.25, color=SCALE_MEMBER_COLOR, fill=True, zorder=5))
      else:
        ax.add_patch(plt.Circle((x, y), 0.25, color=DEFAULT_COLOR, fill=True, zorder=5, ec='black'))
      ax.text(x, y, note, c=TEXT_DEFAULT_COLOR, va='center', ha='center', zorder=5)

    ax.set_title('Hexes of Tenths '+halfsteps_to_stepnames(halfsteps))

  plt.xlim([-2, 2])
  plt.ylim([-2, 2])
  plt.show()

if __name__ == "__main__":
  hexes_of_tenths()
  circle_of_fifths()