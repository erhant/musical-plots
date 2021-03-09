import numpy as np
import matplotlib.pyplot as plt

class Notes:
  def __init__(self):
    self.curIdx = 0
    self.notesABC = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    self.notes = ['Do', 'Do#', 'Re', 'Re#', 'Mi', 'Fa', 'Fa#', 'Sol', 'Sol#', 'La', 'La#', 'Si']
    assert(len(self.notesABC) == len(self.notes))

  def next(self, halfsteps):
    self.curIdx = (self.curIdx + halfsteps) % len(self.notesABC) 
    return self.notesABC[self.curIdx]

  def read_then_next(self, halfsteps):
    tmp = self.notesABC[self.curIdx] 
    self.curIdx = (self.curIdx + halfsteps) % len(self.notesABC) 
    return tmp

  def cur(self):
    return self.notesABC[self.curIdx]
  
  def set_cur(self, idx):
    self.curIdx = idx % len(self.notesABC) 

# Calculate the center coordinates
def centerCoordinates(m):
  cx = 0.5; # because our first two points are always [0,0] and [b,0]
  cy = 0.5 * np.tan(np.radians((180 - (360/m))/2)); # using the triangle of [0,0], [cx, 0]
  return cx, cy

#def scaleCoordinates(m)
  # TODO: Scale the shape to a desired length edges


# Function that returns the coordinates of the center shape (2 of them at
# [0,0] and [1,0] for sure
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

def circle_of_fifths():
  '''
  Creates the circle of fifths, and plots it
  '''
  c = initialCoordinates(12) 
  cx, cy = centerCoordinates(12)
  # Translate the coordinates so that the center is [0,0]
  c[:,0] -= cx
  c[:,1] -= cy
  cx = 0
  cy = 0   

  # scale
  # TODO

  ax = plt.axes()

  # Plot the lines, add circles and text
  ax.plot(c[:,0], c[:,1], 'k')

  halfsteps_fifth = 7 # 2 + 2 + 1 + 2
  notes = Notes()
  for x, y in c: 
    ax.add_patch(plt.Circle((x, y), 0.25, color='black', fill=True))
    ax.text(x, y, notes.read_then_next(halfsteps_fifth), c='white', va='center', ha='center')
  plt.show()

def hexes_of_tenths():
  '''
  Creates the hexes of tenths, and plots it.

  One hex starts from Do, the other from Si. Tenth is basically a whole step forward :)
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
  h1[:,0] *= 1.6
  h1[:,1] *= 1.6

  ax = plt.axes()
  ax.plot(h1[:,0], h1[:,1], 'k')
  ax.plot(h2[:,0], h2[:,1], 'k')

  notes = Notes() 

  # outer hex
  notes.set_cur(0)
  for x, y in h1: 
    ax.add_patch(plt.Circle((x, y), 0.25, color='black', fill=True))
    ax.text(x, y, notes.read_then_next(2), c='white', va='center', ha='center')

  # inner hex
  notes.set_cur(-1)
  for x, y in h2: 
    ax.add_patch(plt.Circle((x, y), 0.25, color='black', fill=True))
    ax.text(x, y, notes.read_then_next(2), c='white', va='center', ha='center')

  # inner to outer lines (on same index)
  # TODO

  # outer to inner lines (outer to next inner)
  # TODO 

  plt.show()

hexes_of_tenths()