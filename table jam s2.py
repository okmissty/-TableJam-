#		python code
#		script_name: table jam song 2
#
#		author: Tyeon 
#       Song title: Solarlake or Solar Jam
#		description: Second song in table jam. All sounds from earsketch. A chill yet upbeat song.
#

from earsketch import *

init()
setTempo(120)

#Variables (earsketch)
housechord1 = HOUSE_DEEP_CHORD_001
funkout = YG_FUNK_KICK_OUT_1
drums = Y07_DRUM_SAMPLE
housepiano = HOUSE_ROADS_PIANO_007
midbeat1 = HOUSE_DEEP_AIRYCHORD_001
midbeat2 = YG_NEW_FUNK_SYNTH_3
phonering = TYEONFORD_PHONERING
# Beats made by me
beat1 =  "0--0--000--00-0-"


#intro
def intro():
    fitMedia(housechord1, 3, 2, 9)
    fitMedia(funkout, 2, 1, 2)
    fitMedia(drums,1 , 2, 48)
    fitMedia(housepiano, 4, 9 , 20)
    fitMedia(housechord1 , 5, 9, 20)
#Mid song
def midsong():
    fitMedia(midbeat1, 6, 20,30)
    fitMedia(housepiano, 7, 20, 30 )
    fitMedia(midbeat2, 8 , 30, 34.5)
#Outro
def outro():
    makeBeat(housechord1, 3, 49, beat1)
    fitMedia(housechord1, 3, 35, 49)
    fitMedia(phonering, 9, 35, 35.5)




#Effects
setEffect(2, VOLUME, GAIN, 12)
setEffect(3, VOLUME, GAIN, 0, 35, 3, 38)
setEffect(5, REVERB, REVERB_TIME, 1000.0)
setEffect(5, VOLUME, GAIN, -60, 1, -15, 3)
setEffect(6, VOLUME, GAIN, 8)
setEffect(7, REVERB, REVERB_TIME, 4000.0)
setEffect(7, VOLUME, GAIN, -14) 
setEffect(8, VOLUME, GAIN, 8)
setEffect(9, VOLUME, GAIN, 12)



intro()
midsong()
outro()


finish()


#Might use
#HOUSE_DEEP_AIRYCHORD_001
#YG_ELECTRO_SYNTH_BRASS_1
