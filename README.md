# Musical Plots

This repo uses `matplotlib` to plot some cool things:
- **Circle of Fifths**:
  Can specify a root to highlight it's major key and the relative minor key.
- **Hexes of Tenths** (a structure made up by me):
  Can specify a root and an array of intervals which make up a chord or a scale.
- **Fretboard**:
  Can specify a root and an array of intervals which make up a chord or a scale. Can also specify fret count and string tuning.
- **Keyboard**:
  Can specify a root and an array of intervals which make up a chord or a scale. Can also specify number of octaves to display.

There is also a chord constructor in `chords.py`. You can give it an input such as `"1-b3-5-b7"` and it will create the necessary array of intervals, which is used by the actual plots.

## Examples
Hexes of Tenths, [G# Minor](https://open.spotify.com/track/6GzMz3s0K1YKwRVI36CgRx?si=a5-Jz81pRbuIVQsfP2h2RQ) scale.

![1](https://github.com/erhant/hexes-of-tenths/blob/main/img/hex_gs_minor.png?raw=true) 

Circle of Fifths, [C Major](https://open.spotify.com/track/5rkBnTgLJa6xBuBSZTbuCT?si=Vf7whUFEQLmZLXESsh84QQ) key (with relative [A Minor](https://open.spotify.com/track/0NcSIGbvjOxxbdKCGhKfF3?si=AFJPoOQzT8iGZDeMR7nkMA) key).

![2](https://github.com/erhant/hexes-of-tenths/blob/main/img/circle_c.png?raw=true)

### Guitar (6-string, standard)

Fretboard, [G Minor Pentatonic](https://open.spotify.com/track/3af6czaWDVsWKdMNtVykhX?si=ladZE-FXSsWkI21jDuxzxA)

![3](https://github.com/erhant/hexes-of-tenths/blob/main/img/fret_g_penta.png?raw=true)

Fretboard, [Hendrix Chord](https://open.spotify.com/track/0wJoRiX5K5BxlqZTolB2LD?si=2XgX2-zSQ0Wz6fjgMyUIdA) (notes highlighted, not the actual position)

![4](https://github.com/erhant/hexes-of-tenths/blob/main/img/fret_hendrix.png?raw=true)

### Keyboard

Piano, [A Flat Major](https://open.spotify.com/track/0SwKt4T6PMsdqU5q6Pv234?si=jqlPWngxT4SdIImAWIBdmw)

![5](https://github.com/erhant/hexes-of-tenths/blob/main/img/piano_aflat_major.png?raw=true)

Piano, [C Blues](https://open.spotify.com/track/4CZfPaDW5madfScpZl0nDU?si=Edc98YizR_OiWNsJANWL6Q)

![6](https://github.com/erhant/hexes-of-tenths/blob/main/img/piano_c_blues.png?raw=true)

### Bass (4-string, standard)

![7](https://github.com/erhant/hexes-of-tenths/blob/main/img/bass.png?raw=true)

### Violin

![8](https://github.com/erhant/hexes-of-tenths/blob/main/img/violin.png?raw=true)
