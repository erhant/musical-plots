NOTE_SYSTEM_ABC_SHARPS = 0
NOTE_SYSTEM_CLASSIC_SHARPS = 1
NOTE_SYSTEM_ABC_FLATS = 2
NOTE_SYSTEM_CLASSIC_FLATS = 3
NOTE_SYSTEM_DEFAULT = NOTE_SYSTEM_ABC_SHARPS
_NOTE_SYSTEMS = [ \
  #  0     1      2     3      4     5     6      7      8       9     10     11
  ['C',  'C#',  'D',  'D#',  'E',  'F',  'F#',  'G',   'G#',   'A',  'A#',  'B'],  # 0: NOTE_SYSTEM_ABC_SHARPS
  ['DO', 'DO#', 'RE', 'RE#', 'MI', 'FA', 'FA#', 'SOL', 'SOL#', 'LA', 'LA#', 'SI'], # 1: NOTE_SYSTEM_CLASSIC_SHARPS
  ['C',  'Db',  'D',  'Eb',  'E',  'F',  'Gb',  'G',   'Ab',   'A',  'Bb',  'B'],  # 2: NOTE_SYSTEM_ABC_FLATS
  ['DO', 'REb', 'RE', 'MIb', 'MI', 'FA', 'SOLb','SOL', 'LAb',  'LA', 'SIb', 'SI']  # 3: NOTE_SYSTEM_CLASSIC_FLATS
]                       

DO    = 0
DOs   = 1
REb   = 1
RE    = 2
REs   = 3
MIb   = 3
MI    = 4
FA    = 5
FAs   = 6
SOLb  = 6
SOL   = 7
SOLs  = 8
LAFb  = 8
LA    = 9
LAs   = 10
SI    = 11

C     = 0
Cs    = 1
Db    = 1
D     = 2
Ds    = 3
Eb    = 3
E     = 4
F     = 5
Fs    = 6
Gb    = 6
G     = 7
Gs    = 8
Ab    = 8
A     = 9
As    = 10
B     = 11

class Notes:
  def __init__(self, note_type=NOTE_SYSTEM_DEFAULT):
    self.curIdx = 0 
    self.noteType = note_type 
    self.notes = _NOTE_SYSTEMS[note_type]
    self.noteCount = len(self.notes)

  def change_note_system(self, note_system):
    '''
    Change note system, i.e. use sharps or flats, letters or names. 
    '''
    if note_system < 0 or note_system >= len(_NOTE_SYSTEMS):
      print("Invalid note type, nothing changed.")
      return
    self.noteType = note_system
    self.notes = _NOTE_SYSTEMS[note_system]
    
  def next(self, hs):
    '''
    Go 'hs' halfsteps. Can be negative.
    '''
    self.curIdx = (self.curIdx + hs) % self.noteCount
    return self.notes[self.curIdx]

  def read_then_next(self, hs):
    '''
    Read the current note string, and then move 'hs' halfsteps.
    '''
    tmp = self.notes[self.curIdx] 
    self.curIdx = (self.curIdx + hs) % self.noteCount
    return tmp 

  def cur(self):
    '''
    Read the current note string.
    '''
    return self.notes[self.curIdx]
  
  def read_note(self, note):
    '''
    Read a note.
    '''
    return self.notes[note]
    
  def set_cur(self, note):
    '''
    Set the current note. The input can be a number, or a note variable, which represent their indices.
    '''

    self.curIdx = note % self.noteCount
 

