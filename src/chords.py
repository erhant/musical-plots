from util import to_interval

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








