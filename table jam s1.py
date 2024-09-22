#		python code
#		script_name: table jam song 1
#
#		author: Tyeon Ford
#		description: Funk/pop electric beat, all sounds are from EarSketch.
#       title: Marmalade Jam

from earsketch import *

init()
setTempo(120)

funkbase1 = YG_FUNK_BASS_4
mainbeat = RD_POP_MAINBEAT_16
epiano = YG_FUNK_ELECTRIC_PIANO_1
spice = YG_FUNK_CLAV_1
epiano2 = YG_FUNK_ELECTRIC_PIANO_4
funkbass = YG_NEW_FUNK_SYNTH_BASS_3
funksnare = YG_FUNK_SNARE_TOP_1
kickout = YG_FUNK_KICK_OUT_1
##Music##

# intro/ Sounds that go the entire song.
def intro():
    fitMedia(funkbase1, 1, 1 , 73)
    fitMedia(mainbeat, 3, 7, 72)
    fitMedia(epiano, 2, 3, 21)

# Mid song
def midsong():
    fitMedia(spice, 4, 21, 32)
    fitMedia(epiano2, 4, 32, 36)
    fitMedia(epiano, 5, 36, 44)

# Late song
def latesong():
    fitMedia(funkbass, 5, 44, 60)
    fitMedia(funksnare, 5, 62, 73)
    fitMedia(kickout, 5, 60, 62)


def loopy(clip, startMeasure):
  for measure in range (startMeasure, 8, 4):
    fitMedia(clip, 1, measure, measure + 1)

#this is a transition
beat1 = "0--00-"
makeBeat(spice, 20, 21, beat1)

a = "Tyeon Ford made this"
b = a[10: 14]
print(b)
#Effects
setEffect(1, VOLUME, GAIN, -20, 2, 9, 4)
setEffect(4, VOLUME, GAIN, -50, 17, 0, 25)


loopy(spice, 65)
intro()
midsong()
latesong()

#Might use
#Y07_DRUM_SAMPLE
#YG_NEW_FUNK_SYNTH_BASS_3
#YG_ALT_POP_CRASH_3
finish()
