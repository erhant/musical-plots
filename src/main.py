import numpy as np
import matplotlib.pyplot as plt
from util import initialCoordinates, centerCoordinates, rotate
import scales
import chords
import notes
from copy import deepcopy

DIMINISHED_CHORD_COLOR = '#C9C4D9'
MAJOR_CHORD_COLOR = '#CCE7D4'
MINOR_CHORD_COLOR = '#FCD2C2'
MAJOR_ROOT_COLOR = '#5ADD80'
MINOR_ROOT_COLOR = '#FF9A75'
SCALE_MEMBER_COLOR = '#C9C4D9'
DEFAULT_COLOR = 'white'
TEXT_DEFAULT_COLOR = 'black'

_notes = notes.Notes()

def circle_of_fifths(root=None):
  '''
  Creates the circle of fifths, and plots it. It includes relative minors.

  You can specify a root, it will color the chords in major and relative minor scale.
  ''' 
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

  # copy to another
  c_rel = deepcopy(c) # relative minors
  CIRCLE_SCALE_FACTOR = 0.75
  c_rel[:,0] *= CIRCLE_SCALE_FACTOR
  c_rel[:,1] *= CIRCLE_SCALE_FACTOR


  ax = plt.axes()

  # Plot the lines, add circles and text
  ax.plot(c[:,0], c[:,1], 'k')
  ax.plot(c_rel[:,0], c_rel[:,1], 'k--')

  halfsteps_fifth = 7 # 2 + 2 + 1 + 2 

  
  # outer  
  majors = []
  dims = []
  minors = []
  if root != None:
    # go to root 
    _notes.set_cur(root)
    rootName = _notes.cur()
    # construct major scale
    majors.append(_notes.read_then_next(2)) # I
    minors.append(_notes.read_then_next(2)) # ii
    minors.append(_notes.read_then_next(1)) # iii
    majors.append(_notes.read_then_next(2)) # IV
    majors.append(_notes.read_then_next(2)) # V
    minors.append(_notes.read_then_next(2)) # vi
    dims.append(_notes.read_then_next(1))   # VII*

  _notes.set_cur(notes.Fs) 
  for x, y in c: 
    note = _notes.read_then_next(-halfsteps_fifth)
    if note == rootName:
      ax.add_patch(plt.Circle((x, y), 0.25, color=MAJOR_ROOT_COLOR, fill=True, zorder=5))
    elif note in majors:
      ax.add_patch(plt.Circle((x, y), 0.25, color=MAJOR_CHORD_COLOR, fill=True, zorder=5))
    elif note in minors:
      ax.add_patch(plt.Circle((x, y), 0.25, color=MINOR_CHORD_COLOR, fill=True, zorder=5))
    elif note in dims:
      ax.add_patch(plt.Circle((x, y), 0.25, color=DIMINISHED_CHORD_COLOR, fill=True, zorder=5))
    else:
      ax.add_patch(plt.Circle((x, y), 0.25, color=DEFAULT_COLOR, fill=True, zorder=5, ec='black'))
    ax.text(x, y, note, c=TEXT_DEFAULT_COLOR, va='center', ha='center', zorder=5)
  
  # inner  
  majors = []
  dims = []
  minors = []
  if root != None: 
    _notes.set_cur(root)
    _notes.next(-3) # move to relative minor
    rootName = _notes.cur()
    # construct minor scale
    minors.append(_notes.read_then_next(2)) # i
    dims.append(_notes.read_then_next(1)) # II*
    majors.append(_notes.read_then_next(2)) # III
    minors.append(_notes.read_then_next(2)) # iv
    minors.append(_notes.read_then_next(1)) # v
    majors.append(_notes.read_then_next(2)) # VI
    majors.append(_notes.read_then_next(2))   # VII

  _notes.set_cur(notes.Eb) 
  for x, y in c_rel: 
    note = _notes.read_then_next(-halfsteps_fifth)
    if note == rootName:
      ax.add_patch(plt.Circle((x, y), 0.18, color=MINOR_ROOT_COLOR, fill=True, zorder=5))
    elif note in majors:
      ax.add_patch(plt.Circle((x, y), 0.18, color=MAJOR_CHORD_COLOR, fill=True, zorder=5))
    elif note in minors:
      ax.add_patch(plt.Circle((x, y), 0.18, color=MINOR_CHORD_COLOR, fill=True, zorder=5))
    elif note in dims:
      ax.add_patch(plt.Circle((x, y), 0.18, color=DIMINISHED_CHORD_COLOR, fill=True, zorder=5))
    else:
      ax.add_patch(plt.Circle((x, y), 0.18, color=DEFAULT_COLOR, fill=True, zorder=5, ec='black'))
    ax.text(x, y, note, c=TEXT_DEFAULT_COLOR, va='center', ha='center', zorder=5)

  ax.set_title('Circle of Fifths')
  plt.axis('off')
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
 
   
    
  # construct the scale
  scaleNotes = []
  rootName = ""

  if halfsteps != None and root != None:
    _notes.set_cur(root)
    rootName = _notes.cur()
    for steps in halfsteps:
      scaleNotes.append(_notes.read_then_next(steps))
    scaleNotes.append(_notes.cur())

  # outer hex
  _notes.set_cur(notes.Fs)
  for x, y in h1: 
    note = _notes.read_then_next(2)
    if note == rootName:
      ax.add_patch(plt.Circle((x, y), 0.25, color=MAJOR_ROOT_COLOR, fill=True, zorder=5))
    elif note in scaleNotes:
      ax.add_patch(plt.Circle((x, y), 0.25, color=SCALE_MEMBER_COLOR, fill=True, zorder=5))
    else:
      ax.add_patch(plt.Circle((x, y), 0.25, color=DEFAULT_COLOR, fill=True, zorder=5, ec='black'))
    ax.text(x, y, note, c=TEXT_DEFAULT_COLOR, va='center', ha='center', zorder=5)

  # inner hex
  _notes.set_cur(notes.F)
  for x, y in h2: 
    note = _notes.read_then_next(2)
    if note == rootName:
      ax.add_patch(plt.Circle((x, y), 0.25, color=MAJOR_ROOT_COLOR, fill=True, zorder=5))
    elif note in scaleNotes:
      ax.add_patch(plt.Circle((x, y), 0.25, color=SCALE_MEMBER_COLOR, fill=True, zorder=5))
    else:
      ax.add_patch(plt.Circle((x, y), 0.25, color=DEFAULT_COLOR, fill=True, zorder=5, ec='black'))
    ax.text(x, y, note, c=TEXT_DEFAULT_COLOR, va='center', ha='center', zorder=5)

  ax.set_title('Hexes of Tenths')

  plt.xlim([-2, 2])
  plt.ylim([-2, 2])
  plt.axis('off')
  plt.show()

def fretboard(fretcount=12, strings=[notes.E, notes.A, notes.D, notes.G, notes.B, notes.E], root=None, halfsteps=None):
  '''
  The fretboard is constructed in matplotlib.

  You can pass in root and halfsteps for highlighting.
  '''
  stringcount = len(strings)
  assert(stringcount > 0)
  f = np.empty((fretcount+2, 2 , stringcount)) # fretboard coordinates
  # A fret is of size (F_X, F_Y) 
  F_X = 1
  F_Y = 1
  START_X = 0.0
  START_Y = 0.0
  for i in range(fretcount+2):
    f[i, 0, 0] = START_X + i * F_X
    f[i, 1, 0] = START_Y
    for j in range(1,stringcount):
      f[i, 0, j] = f[i, 0, 0] # X is same for every string
      f[i, 1, j] = f[i, 1, 0] + j * F_Y
  
  ax = plt.axes()

  # plot verticals
  for i in range(1,fretcount+2):
    ax.plot(f[i,0,:], f[i,1,:], 'k')
  # plot horizontals
  for j in range(stringcount):
    ax.plot(f[1:,0,j], f[1:,1,j], 'k') 

  scaleNotes = []
  rootName = ""
  if halfsteps != None and root != None:
    _notes.set_cur(root)
    rootName = _notes.cur()
    for steps in halfsteps:
      scaleNotes.append(_notes.read_then_next(steps))
    scaleNotes.append(_notes.cur())

  # Create circles
  for j in range(stringcount):
    _notes.set_cur(strings[j])
    for i in range(fretcount+1):
      note = _notes.read_then_next(1)
      x = (f[i, 0, j] + f[i+1, 0, j]) / 2
      y = (f[i, 1, j] + f[i+1, 1, j]) / 2
      if note == rootName:
        ax.add_patch(plt.Circle((x, y), 0.25, color=MAJOR_ROOT_COLOR, fill=True, zorder=5))
      elif note in scaleNotes:
        ax.add_patch(plt.Circle((x, y), 0.25, color=SCALE_MEMBER_COLOR, fill=True, zorder=5))
      else:
        ax.add_patch(plt.Circle((x, y), 0.25, color=DEFAULT_COLOR, fill=True, zorder=5, ec='black'))
      ax.text(x, y, note, c=TEXT_DEFAULT_COLOR, va='center', ha='center', fontsize='medium', zorder=5)

  for i in range(fretcount+1):
    ax.text((f[i, 0, 0] + f[i+1, 0, 0]) / 2, START_Y - 0.5 * F_Y, str(i), c=TEXT_DEFAULT_COLOR, va='center', ha='center', zorder=5) 
  ax.set_title("Fretboard")
  plt.xlim([START_X-F_X, F_X*(fretcount+2)]) # one +1 for the open fret, other +1 for the boundary
  plt.ylim([START_Y-F_Y, F_Y*(stringcount)])
  plt.axis('off')
  plt.show()

def piano(octaves=2, root=None, halfsteps=None):
  '''
  Piano keys. Each octave starts with C.
  
  '''
  START_X = 0.0
  START_Y = 0.0
  SCALE_X=1.3
  SCALE_Y=1.8
  # W_X W_Y are white key dims, B_X B_Y are black key dims.
  W_X = 2.35*SCALE_X
  W_Y = W_X*SCALE_Y
  B_X = 1.37*SCALE_X
  B_Y = B_X*SCALE_Y
  ax = plt.axes()

  _notes.set_cur(notes.C)
  CUR_X = START_X
  
  scaleNotes = []
  rootName = ""
  if halfsteps != None and root != None:
    _notes.set_cur(root)
    rootName = _notes.cur()
    for steps in halfsteps:
      scaleNotes.append(_notes.read_then_next(steps))
    scaleNotes.append(_notes.cur())

  _notes.set_cur(notes.C)
  for o in range(octaves):
    for i in range(7):
      note = _notes.read_then_next(1) 
      # white key
      if note == rootName:
        ax.add_patch(plt.Rectangle((CUR_X, START_Y), W_X, -W_Y, color=MAJOR_ROOT_COLOR, fill=True, zorder=5, ec='black')) 
        ax.text(CUR_X+W_X/2, START_Y-3*W_Y/4, note, c='white', va='center', ha='center', zorder=5)
      elif note in scaleNotes:
        ax.add_patch(plt.Rectangle((CUR_X, START_Y), W_X, -W_Y, color=SCALE_MEMBER_COLOR, fill=True, zorder=5, ec='black')) 
        ax.text(CUR_X+W_X/2, START_Y-3*W_Y/4, note, c='white', va='center', ha='center', zorder=5)
      else:
        ax.add_patch(plt.Rectangle((CUR_X, START_Y), W_X, -W_Y, color='white', fill=True, zorder=5, ec='black')) 
        ax.text(CUR_X+W_X/2, START_Y-3*W_Y/4, note, c='black', va='center', ha='center', zorder=5)
      
      # black key
      if i != 2 and i != 6:
        note = _notes.read_then_next(1) 
        if note == rootName:
          ax.add_patch(plt.Rectangle((CUR_X+W_X-(B_X/2), START_Y), B_X, -B_Y, color=MAJOR_ROOT_COLOR, fill=True, zorder=6, ec='black')) 
        elif note in scaleNotes:
          ax.add_patch(plt.Rectangle((CUR_X+W_X-(B_X/2), START_Y), B_X, -B_Y, color=SCALE_MEMBER_COLOR, fill=True, zorder=6, ec='black')) 
        else:
          ax.add_patch(plt.Rectangle((CUR_X+W_X-(B_X/2), START_Y), B_X, -B_Y, color='black', fill=True, zorder=6, ec='black'))
        ax.text(CUR_X+W_X, START_Y-3*B_Y/4, note, c='white', va='center', ha='center', zorder=6)
    
      CUR_X += W_X
  

  ax.set_title("Piano")
  plt.xlim([START_X-W_X, CUR_X+W_X]) # one +1 for the open fret, other +1 for the boundary
  plt.ylim([START_Y-W_Y, START_Y])
  plt.tight_layout()
  plt.axis('off')
  plt.show()

  
if __name__ == "__main__":
  #hexes_of_tenths(root=notes.Gs, halfsteps=scales.Minor)
  #circle_of_fifths(root=notes.C)
  #fretboard(root=notes.G, halfsteps=scales.Minor_Pentatonic)
  #fretboard(root=notes.E, halfsteps=chords.Hendrix)
  #piano(root=notes.Ab, halfsteps=scales.Major)
  #piano(root=notes.C, halfsteps=scales.Blues)
  pass