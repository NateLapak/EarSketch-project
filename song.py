#		python code
#		script_name: MySong.py
#
#		author: Nathan Lapak
#		description: My entry for the eark sketch competition.
#

'''
This song is an R&B and hip-hop song.
It has an intro, verse 1, chorus, verse 2 and outro.
I created a function for each part of the song to make the code more organized and maybe reuseable

'''

# Import earsketch
from earsketch import *

# Function to make my intro
def intro():    
    
    # Add instruments to track
    hiHat = YG_RNB_FUNK_HIHAT_1
    fitMedia(hiHat, 1, 1, 13.3)
    fitMedia(RD_RNB_KEYSRHODES_5, 2, 1, 13.3)
    fitMedia(RD_RNB_SFX_LIGHTAIR_1, 3, 13.5, 15.5)
    
    # Make track 1 and track 2 slowly loss volume then regain the volume as verse1 approaches
    setEffect(1, VOLUME, GAIN, 0, 5, -30, 13.5)
    setEffect(2, VOLUME, GAIN, 0, 9, -30, 13.5)
    
    # Instruments for the beat
    closedHat = OS_CLOSEDHAT04
    lowTom = OS_LOWTOM04
    openHat = OS_OPENHAT03
    
    # Patterns for each instrument
    makePattern1 = "0+--0+--0+--0+--"
    makePattern2 = "0000000000000000"
    makePattern3 = "--0+--0+--0+--0+"
    
    # For loop to repeat the same beat from measures 5 to 12
    for measure in range(5, 12):
        makeBeat(closedHat, 3, measure, makePattern2)
        makeBeat(lowTom, 4, measure, makePattern1)
        makeBeat(openHat, 5, measure, makePattern3)
    
    # Instruments and effects to transition into verse 1
    setEffect(3, VOLUME, GAIN, 0, 12, -30, 13.5)
    fitMedia(ENTREP_VOX_JAYZ_BUILD, 6, 9, 11)
    
    # Effects to transition into verse 1
    setEffect(1, VOLUME, GAIN, -30, 13.5, 0, 15.5)
    setEffect(2, VOLUME, GAIN, -30, 13.5, 0, 15.5)
    setEffect(3, VOLUME, GAIN, -30, 13.5, 0, 15.5)
    
# Function for verses
def verse1():
    
    # Fit new instruments onto track
    fitMedia(CIARA_SET_BASSLINE_1, 2, 17.5, 24)
    fitMedia(ENTREP_VOX_PHARRELL_VRS_2, 1, 14.5, 18.5)
    fitMedia(ENTREP_VOX_PHARRELL_VRS_1, 1, 19.5, 19.8)
    fitMedia(YG_NEW_HIP_HOP_CLAP_2, 3, 18.5, 24.5)
    fitMedia(ENTREP_VOX_JAYZ_BUILD, 1, 20.5, 24.5)
    
    # Clap to transition into the chorus
    clapBeat = OS_CLAP01
    transition = "0000000+"
    makeBeat(clapBeat, 1, 24.5, transition)
    
# Function for chorus
def chorus():
    
    # Fit instruments into chorus
    fitMedia(ENTREP_THEME_BRASS, 1, 25, 37)
    fitMedia(ENTREP_PERC_HIHAT, 2, 25, 37)
    fitMedia(ENTREP_VOX_BK_BLKMAN, 5, 27, 28)
    
    # For loop to repeat the same instruments over unique measures
    for measure in range(30, 33):
        
        # Repeat only in measures that are even
        if measure % 2 == 0:
            fitMedia(ENTREP_VOX_BK_BLKMAN, 5, measure, measure + 1)
    
    # Instruments for beat
    kick = ENTREP_PERC_KICK_2
    orchCrash = ENTREP_PERC_ORCH_CRASH
    
    # Pattern for the first beat of chorus (measures 25-28)
    pattern1 = "0-----0-----0--"
    pattern2 = "--0+----0+-----"
    
    # Create the beat from measure 25 to 28
    for measure in range(28, 31):
        
        if measure % 2 != 0:
            makeBeat(kick, 3, measure, pattern1)
            makeBeat(orchCrash, 4, measure, pattern2)
    
    # Pattern for 2nd beat of chorus (measures 33-37)
    pattern1 = "00+---0-00+----"
    pattern2 = "----0+------0+-"
    
    # Create and repeat beat starting from measure 33 until 37
    for measure in range(33, 37):
        makeBeat(kick, 3, measure, pattern1)
        makeBeat(orchCrash, 4, measure, pattern2)
    
    # Transition into 2nd verse
    setEffect(1, VOLUME, GAIN, 0, 37, -30, 38)
    fitMedia(ENTREP_VOX_PHARRELL_VRS_2, 1, 37.5, 41.5)
    setEffect(1, VOLUME, GAIN, -30, 38, 0, 41)
    
def verse2():
    
    # Fit instruments into 2nd verse
    fitMedia(CIARA_SET_BASSLINE_3, 2, 40.5, 41)
    fitMedia(ENTREP_VOX_PHARRELL_VRS_1, 1, 41.5, 41.8)
    fitMedia(CIARA_SET_BASSLINE_1, 2, 41.5, 47.5)
    fitMedia(YG_NEW_HIP_HOP_CLAP_2, 4, 41.5, 47.5)
    fitMedia(ENTREP_VOX_JAYZ_BUILD, 1, 43.5, 47.5)
    fitMedia(RD_RNB_SFX_LIGHTAIR_1, 3, 47.5, 49.5)
    
    # Clapping beat
    clap = OS_CLAP02
    makePattern = "00000000+"
    makeBeat(clap, 3, 41, makePattern)
    
    # Effects to transition into outro
    setEffect(3, VOLUME, GAIN, 0, 49, -30, 55)
    setEffect(1, VOLUME, GAIN, 0, 48, -30, 48)
    
def outro():
    
    # Set volume back to normal and fit instruments
    setEffect(1, VOLUME, GAIN, -30, 49, 0, 51)
    fitMedia(RD_RNB_KEYSRHODES_7, 1, 49, 61)
    fitMedia(YG_RNB_FUNK_HIHAT_1, 2, 53, 57)
    
    # Instruments fade out and end's the song
    setEffect(1, VOLUME, GAIN, 0, 57, -40, 61)
    
# Initialize song and set temp to 85 bpm
init()
setTempo(85)

# Main song. Invoke each part of song
intro()
verse1()
chorus()
verse2()
outro()

# End of song
finish()
