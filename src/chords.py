'''
Everything is constructed from Major scale: 
  [2, 2, 1, 2, 2, 2, 1] (the diagonal)

Major Interval Distances:
     | 1   2   3   4   5   6   7   8   9   10  11  12  13  14  15   
  ---+------------------------------------------------------------+
  1  | 0   2   4   5   7   9   11  12  14  16  17  19  21  23  24 | 
  2  | 2   0   2   3   5   7   9   10  12  14  15  17  19  21  22 |  
  3  | 4   2   0   1   3   5   7   8   10  13  14  16  18  20  21 |  
  4  | 5   3   1   0   2   4   6   7   9   11  12  14  16  18  19 |  
  5  | 6   5   3   2   0   2   4   5   7   9   10  12  14  16  17 |  
  6  | 9   7   5   4   2   0   2   3   5   7   8   10  12  14  15 |  
  7  | 11  9   7   6   4   2   0   1   3   5   6   8   10  12  13 |  
  8  | 12  10  8   7   5   3   1   0   2   4   5   7   9   11  12 |  
  9  |                             2   0   2   3   5   7   9   10 |  
  10 |                                 2   0   1   3   5   7   8  |
  11 |                                     1   0   2   4   6   7  | 
  12 |                                         2   0   2   4   5  |
  13 |                                             2   0   2   3  |
  14 |                                                 2   0   1  |
  15 |                                                     1   0  |
  ---+------------------------------------------------------------+
  This matrix is useful for chord construction, for example major chord is 1-3-5. So we look at mat[1][3] and mat[3][5], giving 4 and 3. 

#TODO: implement chord constructor function, e.g. (construct(['1', 'b3', '5', '#7']))
'''

Power     = [7]

Add2      = [2, 2, 3]
Add9      = [4, 3, 7]

Maj       = [4, 3]
Maj6      = [4, 3, 2]
Maj7      = [4, 3, 4]
Maj9      = [4, 3, 4, 3]
Maj7s11   = [4, 3, 4, 5]

Aug       = [4, 4]
Aug7      = [4, 4, 2]

Min       = [3, 4]
Min6      = [3, 4, 2, 1]
Min7      = [3, 4, 3]
Min9      = [3, 4, 3, 4]
Min9b5    = [3, 3, 4, 4]
Min11     = [3, 4, 3, 7]

Dom7b5    = [4, 2, 4]
Dom7      = [4, 3, 3]
Dom9      = [4, 3, 3, 4] # aka 9 

Dim       = [3, 3]
Dim7      = [3, 3, 3]
HalfDim   = [3, 3, 4]

Sus2      = [2, 5]
Sus4      = [5, 2]
SevenSus4 = [5, 2, 3] # 7sus4
NineSus4  = [5, 2, 3, 4] # 9sus4

NineFlat  = [4, 3, 3, 3] # b9
Nine      = [4, 3, 3, 4] # 9
NineSharp = [4, 3, 3, 5] # #9
SixAdd9   = [4, 3, 2, 5] # 6/9 aka 6add9

Dom13 = [4, 3, 3, 11] # aka 13
 

# Specials
Hendrix = [4, 6, 5] # must be root E








