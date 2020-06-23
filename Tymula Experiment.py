#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.3),
    on June 23, 2020, at 08:22
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.3'
expName = 'Tymula Experiment'  # from the Builder filename that created this script
expInfo = {'passcode': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\jackm\\Desktop\\PsychoPy\\Tymula\\Tymula\\Tymula Experiment.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1000, 1000], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[-1.000,-1.000,-1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instruct_1"
instruct_1Clock = core.Clock()
instruct_text_1 = visual.TextStim(win=win, name='instruct_text_1',
    text='In this task you will be asked to choose between two options.\nOne side will have a constant value and the other will have some chance of two different options.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instruct_text_2 = visual.TextStim(win=win, name='instruct_text_2',
    text='Press spacebar to continue',
    font='Arial',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instruct_1_keys = keyboard.Keyboard()

# Initialize components for Routine "instruct_2"
instruct_2Clock = core.Clock()
instruct_text_3 = visual.TextStim(win=win, name='instruct_text_3',
    text='One side will have the constant value shown, 5 in this case.',
    font='Arial',
    pos=(0.25, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instruct_text_4 = visual.TextStim(win=win, name='instruct_text_4',
    text='Press spacebar to continue',
    font='Arial',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instruct_2_keys = keyboard.Keyboard()
tut_sure = visual.TextStim(win=win, name='tut_sure',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "instruct_3"
instruct_3Clock = core.Clock()
Tutbackdrop = visual.ImageStim(
    win=win,
    name='Tutbackdrop', 
    image='TutorialBackground1.png', mask=None,
    ori=0, pos=(0, 0), size=(1.5, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
instruct_3_keys = keyboard.Keyboard()
instruct_text_5 = visual.TextStim(win=win, name='instruct_text_5',
    text='The other side will present you with a more complicated choice.',
    font='Arial',
    pos=(-0.25, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
instruct_text_6 = visual.TextStim(win=win, name='instruct_text_6',
    text='Press spacebar to continue',
    font='Arial',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "instruct_4"
instruct_4Clock = core.Clock()
Tutbackdrop_2 = visual.ImageStim(
    win=win,
    name='Tutbackdrop_2', 
    image='TutorialBackground1.png', mask=None,
    ori=0, pos=(0, 0), size=(1.5, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
instruct_4_keys = keyboard.Keyboard()
instruct_text_7 = visual.TextStim(win=win, name='instruct_text_7',
    text='The very top and bottom numbers are the two possible outcomes of this choice.',
    font='Arial',
    pos=(-0.25, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
instruct_text_8 = visual.TextStim(win=win, name='instruct_text_8',
    text='Press spacebar to continue',
    font='Arial',
    pos=(-0.35, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
TutArrowTop = visual.ImageStim(
    win=win,
    name='TutArrowTop', 
    image='TutorialArrow.png', mask=None,
    ori=0, pos=(0.15, 0.4), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
TutArrowBottom = visual.ImageStim(
    win=win,
    name='TutArrowBottom', 
    image='TutorialArrow.png', mask=None,
    ori=0, pos=(0.15, -0.4), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)

# Initialize components for Routine "instruct_5"
instruct_5Clock = core.Clock()
Tutbackdrop_3 = visual.ImageStim(
    win=win,
    name='Tutbackdrop_3', 
    image='TutorialBackground1.png', mask=None,
    ori=0, pos=(0, 0), size=(1.5, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
instruct_5_keys = keyboard.Keyboard()
instruct_text_9 = visual.TextStim(win=win, name='instruct_text_9',
    text='The innermost numbers are the percentage chance of each outcome.',
    font='Arial',
    pos=(-0.25, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
instruct_text_10 = visual.TextStim(win=win, name='instruct_text_10',
    text='Press spacebar to continue',
    font='Arial',
    pos=(-0.35, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
TutArrowTop_2 = visual.ImageStim(
    win=win,
    name='TutArrowTop_2', 
    image='TutorialArrow.png', mask=None,
    ori=0, pos=(0.15, 0.28), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
TutArrowBottom_2 = visual.ImageStim(
    win=win,
    name='TutArrowBottom_2', 
    image='TutorialArrow.png', mask=None,
    ori=0, pos=(0.15, -0.28), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)

# Initialize components for Routine "instruct_6"
instruct_6Clock = core.Clock()
Tutbackdrop_5 = visual.ImageStim(
    win=win,
    name='Tutbackdrop_5', 
    image='TutorialBackground2.png', mask=None,
    ori=0, pos=(0, 0), size=(1.5, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
instruct_6_keys = keyboard.Keyboard()
instruct_text_11 = visual.TextStim(win=win, name='instruct_text_11',
    text='Sometimes a grey bar will obscure the middle of the choice so the exact probabilities of the outcomes are unknown.',
    font='Arial',
    pos=(-0.25, 0.25), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
instruct_text_12 = visual.TextStim(win=win, name='instruct_text_12',
    text='Press spacebar to continue',
    font='Arial',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
TutArrowTop_3 = visual.ImageStim(
    win=win,
    name='TutArrowTop_3', 
    image='TutorialArrow', mask=None,
    ori=0, pos=(0.15, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# Initialize components for Routine "instruct_7"
instruct_7Clock = core.Clock()
instruct_7_keys = keyboard.Keyboard()
instruct_text_13 = visual.TextStim(win=win, name='instruct_text_13',
    text=' You will get a bonus based on the points you earned from 3 random trials in the game. So choose wisely. you made.\nTo choose between the right and left choices use the right and left arrow keys.\nGood luck!',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instruct_text_14 = visual.TextStim(win=win, name='instruct_text_14',
    text='Press spacebar, right, or left to continue',
    font='Arial',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
key_resp = keyboard.Keyboard()
Red_Square = visual.Rect(
    win=win, name='Red_Square',
    width=(0.4, 0.325)[0], height=(0.4, 0.325)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
Blue_Square = visual.Rect(
    win=win, name='Blue_Square',
    width=(0.4, 0.325)[0], height=(0.4, 0.325)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1.000,0.004,1.000], lineColorSpace='rgb',
    fillColor=[-1.000,0.004,1.000], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
sure = visual.TextStim(win=win, name='sure',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
or_text = visual.TextStim(win=win, name='or_text',
    text='or',
    font='Arial',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
Option_One = visual.TextStim(win=win, name='Option_One',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.08, wrapWidth=None, ori=0, 
    color='White', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
Option_Two = visual.TextStim(win=win, name='Option_Two',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.08, wrapWidth=None, ori=0, 
    color='White', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
Risk_Text_Top = visual.TextStim(win=win, name='Risk_Text_Top',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.08, wrapWidth=None, ori=0, 
    color='White', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
Risk_Text_Bottom = visual.TextStim(win=win, name='Risk_Text_Bottom',
    text='default text',
    font='Arial',
    pos=[0,0], height=0.08, wrapWidth=None, ori=0, 
    color='White', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
Ambiguity_Bar = visual.Rect(
    win=win, name='Ambiguity_Bar',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[0.004,0.004,0.004], fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)

# Initialize components for Routine "endscreen"
endscreenClock = core.Clock()
endscreen_keys = keyboard.Keyboard()
endscreen_text = visual.TextStim(win=win, name='endscreen_text',
    text='Thank you for participating!\n\nPlease notify the experiment runner that you have completed this portion.',
    font='Arial',
    pos=(0, 0.25), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
finalscore_text = visual.TextStim(win=win, name='finalscore_text',
    text='score',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instruct_1"-------
# update component parameters for each repeat
instruct_1_keys.keys = []
instruct_1_keys.rt = []
# keep track of which components have finished
instruct_1Components = [instruct_text_1, instruct_text_2, instruct_1_keys]
for thisComponent in instruct_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruct_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "instruct_1"-------
while continueRoutine:
    # get current time
    t = instruct_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruct_1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruct_text_1* updates
    if instruct_text_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruct_text_1.frameNStart = frameN  # exact frame index
        instruct_text_1.tStart = t  # local t and not account for scr refresh
        instruct_text_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruct_text_1, 'tStartRefresh')  # time at next scr refresh
        instruct_text_1.setAutoDraw(True)
    
    # *instruct_text_2* updates
    if instruct_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruct_text_2.frameNStart = frameN  # exact frame index
        instruct_text_2.tStart = t  # local t and not account for scr refresh
        instruct_text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruct_text_2, 'tStartRefresh')  # time at next scr refresh
        instruct_text_2.setAutoDraw(True)
    
    # *instruct_1_keys* updates
    waitOnFlip = False
    if instruct_1_keys.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruct_1_keys.frameNStart = frameN  # exact frame index
        instruct_1_keys.tStart = t  # local t and not account for scr refresh
        instruct_1_keys.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruct_1_keys, 'tStartRefresh')  # time at next scr refresh
        instruct_1_keys.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(instruct_1_keys.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instruct_1_keys.status == STARTED and not waitOnFlip:
        theseKeys = instruct_1_keys.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruct_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruct_1"-------
for thisComponent in instruct_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instruct_text_1.started', instruct_text_1.tStartRefresh)
thisExp.addData('instruct_text_1.stopped', instruct_text_1.tStopRefresh)
thisExp.addData('instruct_text_2.started', instruct_text_2.tStartRefresh)
thisExp.addData('instruct_text_2.stopped', instruct_text_2.tStopRefresh)
# the Routine "instruct_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruct_2"-------
# update component parameters for each repeat
instruct_2_keys.keys = []
instruct_2_keys.rt = []
tut_sure.setPos([-0.5,0])
tut_sure.setText('5')
# keep track of which components have finished
instruct_2Components = [instruct_text_3, instruct_text_4, instruct_2_keys, tut_sure]
for thisComponent in instruct_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruct_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "instruct_2"-------
while continueRoutine:
    # get current time
    t = instruct_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruct_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruct_text_3* updates
    if instruct_text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruct_text_3.frameNStart = frameN  # exact frame index
        instruct_text_3.tStart = t  # local t and not account for scr refresh
        instruct_text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruct_text_3, 'tStartRefresh')  # time at next scr refresh
        instruct_text_3.setAutoDraw(True)
    
    # *instruct_text_4* updates
    if instruct_text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruct_text_4.frameNStart = frameN  # exact frame index
        instruct_text_4.tStart = t  # local t and not account for scr refresh
        instruct_text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruct_text_4, 'tStartRefresh')  # time at next scr refresh
        instruct_text_4.setAutoDraw(True)
    
    # *instruct_2_keys* updates
    waitOnFlip = False
    if instruct_2_keys.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruct_2_keys.frameNStart = frameN  # exact frame index
        instruct_2_keys.tStart = t  # local t and not account for scr refresh
        instruct_2_keys.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruct_2_keys, 'tStartRefresh')  # time at next scr refresh
        instruct_2_keys.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(instruct_2_keys.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instruct_2_keys.status == STARTED and not waitOnFlip:
        theseKeys = instruct_2_keys.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # *tut_sure* updates
    if tut_sure.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        tut_sure.frameNStart = frameN  # exact frame index
        tut_sure.tStart = t  # local t and not account for scr refresh
        tut_sure.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tut_sure, 'tStartRefresh')  # time at next scr refresh
        tut_sure.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruct_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruct_2"-------
for thisComponent in instruct_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instruct_text_3.started', instruct_text_3.tStartRefresh)
thisExp.addData('instruct_text_3.stopped', instruct_text_3.tStopRefresh)
thisExp.addData('instruct_text_4.started', instruct_text_4.tStartRefresh)
thisExp.addData('instruct_text_4.stopped', instruct_text_4.tStopRefresh)
thisExp.addData('tut_sure.started', tut_sure.tStartRefresh)
thisExp.addData('tut_sure.stopped', tut_sure.tStopRefresh)
# the Routine "instruct_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruct_3"-------
# update component parameters for each repeat
instruct_3_keys.keys = []
instruct_3_keys.rt = []
# keep track of which components have finished
instruct_3Components = [Tutbackdrop, instruct_3_keys, instruct_text_5, instruct_text_6]
for thisComponent in instruct_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruct_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "instruct_3"-------
while continueRoutine:
    # get current time
    t = instruct_3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruct_3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Tutbackdrop* updates
    if Tutbackdrop.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Tutbackdrop.frameNStart = frameN  # exact frame index
        Tutbackdrop.tStart = t  # local t and not account for scr refresh
        Tutbackdrop.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Tutbackdrop, 'tStartRefresh')  # time at next scr refresh
        Tutbackdrop.setAutoDraw(True)
    
    # *instruct_3_keys* updates
    waitOnFlip = False
    if instruct_3_keys.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruct_3_keys.frameNStart = frameN  # exact frame index
        instruct_3_keys.tStart = t  # local t and not account for scr refresh
        instruct_3_keys.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruct_3_keys, 'tStartRefresh')  # time at next scr refresh
        instruct_3_keys.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(instruct_3_keys.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instruct_3_keys.status == STARTED and not waitOnFlip:
        theseKeys = instruct_3_keys.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # *instruct_text_5* updates
    if instruct_text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruct_text_5.frameNStart = frameN  # exact frame index
        instruct_text_5.tStart = t  # local t and not account for scr refresh
        instruct_text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruct_text_5, 'tStartRefresh')  # time at next scr refresh
        instruct_text_5.setAutoDraw(True)
    
    # *instruct_text_6* updates
    if instruct_text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruct_text_6.frameNStart = frameN  # exact frame index
        instruct_text_6.tStart = t  # local t and not account for scr refresh
        instruct_text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruct_text_6, 'tStartRefresh')  # time at next scr refresh
        instruct_text_6.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruct_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruct_3"-------
for thisComponent in instruct_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Tutbackdrop.started', Tutbackdrop.tStartRefresh)
thisExp.addData('Tutbackdrop.stopped', Tutbackdrop.tStopRefresh)
thisExp.addData('instruct_text_5.started', instruct_text_5.tStartRefresh)
thisExp.addData('instruct_text_5.stopped', instruct_text_5.tStopRefresh)
thisExp.addData('instruct_text_6.started', instruct_text_6.tStartRefresh)
thisExp.addData('instruct_text_6.stopped', instruct_text_6.tStopRefresh)
# the Routine "instruct_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruct_4"-------
# update component parameters for each repeat
instruct_4_keys.keys = []
instruct_4_keys.rt = []
# keep track of which components have finished
instruct_4Components = [Tutbackdrop_2, instruct_4_keys, instruct_text_7, instruct_text_8, TutArrowTop, TutArrowBottom]
for thisComponent in instruct_4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruct_4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "instruct_4"-------
while continueRoutine:
    # get current time
    t = instruct_4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruct_4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Tutbackdrop_2* updates
    if Tutbackdrop_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Tutbackdrop_2.frameNStart = frameN  # exact frame index
        Tutbackdrop_2.tStart = t  # local t and not account for scr refresh
        Tutbackdrop_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Tutbackdrop_2, 'tStartRefresh')  # time at next scr refresh
        Tutbackdrop_2.setAutoDraw(True)
    
    # *instruct_4_keys* updates
    waitOnFlip = False
    if instruct_4_keys.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruct_4_keys.frameNStart = frameN  # exact frame index
        instruct_4_keys.tStart = t  # local t and not account for scr refresh
        instruct_4_keys.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruct_4_keys, 'tStartRefresh')  # time at next scr refresh
        instruct_4_keys.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(instruct_4_keys.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instruct_4_keys.status == STARTED and not waitOnFlip:
        theseKeys = instruct_4_keys.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # *instruct_text_7* updates
    if instruct_text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruct_text_7.frameNStart = frameN  # exact frame index
        instruct_text_7.tStart = t  # local t and not account for scr refresh
        instruct_text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruct_text_7, 'tStartRefresh')  # time at next scr refresh
        instruct_text_7.setAutoDraw(True)
    
    # *instruct_text_8* updates
    if instruct_text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruct_text_8.frameNStart = frameN  # exact frame index
        instruct_text_8.tStart = t  # local t and not account for scr refresh
        instruct_text_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruct_text_8, 'tStartRefresh')  # time at next scr refresh
        instruct_text_8.setAutoDraw(True)
    
    # *TutArrowTop* updates
    if TutArrowTop.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TutArrowTop.frameNStart = frameN  # exact frame index
        TutArrowTop.tStart = t  # local t and not account for scr refresh
        TutArrowTop.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TutArrowTop, 'tStartRefresh')  # time at next scr refresh
        TutArrowTop.setAutoDraw(True)
    
    # *TutArrowBottom* updates
    if TutArrowBottom.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TutArrowBottom.frameNStart = frameN  # exact frame index
        TutArrowBottom.tStart = t  # local t and not account for scr refresh
        TutArrowBottom.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TutArrowBottom, 'tStartRefresh')  # time at next scr refresh
        TutArrowBottom.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruct_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruct_4"-------
for thisComponent in instruct_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Tutbackdrop_2.started', Tutbackdrop_2.tStartRefresh)
thisExp.addData('Tutbackdrop_2.stopped', Tutbackdrop_2.tStopRefresh)
thisExp.addData('instruct_text_7.started', instruct_text_7.tStartRefresh)
thisExp.addData('instruct_text_7.stopped', instruct_text_7.tStopRefresh)
thisExp.addData('instruct_text_8.started', instruct_text_8.tStartRefresh)
thisExp.addData('instruct_text_8.stopped', instruct_text_8.tStopRefresh)
thisExp.addData('TutArrowTop.started', TutArrowTop.tStartRefresh)
thisExp.addData('TutArrowTop.stopped', TutArrowTop.tStopRefresh)
thisExp.addData('TutArrowBottom.started', TutArrowBottom.tStartRefresh)
thisExp.addData('TutArrowBottom.stopped', TutArrowBottom.tStopRefresh)
# the Routine "instruct_4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruct_5"-------
# update component parameters for each repeat
instruct_5_keys.keys = []
instruct_5_keys.rt = []
# keep track of which components have finished
instruct_5Components = [Tutbackdrop_3, instruct_5_keys, instruct_text_9, instruct_text_10, TutArrowTop_2, TutArrowBottom_2]
for thisComponent in instruct_5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruct_5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "instruct_5"-------
while continueRoutine:
    # get current time
    t = instruct_5Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruct_5Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Tutbackdrop_3* updates
    if Tutbackdrop_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Tutbackdrop_3.frameNStart = frameN  # exact frame index
        Tutbackdrop_3.tStart = t  # local t and not account for scr refresh
        Tutbackdrop_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Tutbackdrop_3, 'tStartRefresh')  # time at next scr refresh
        Tutbackdrop_3.setAutoDraw(True)
    
    # *instruct_5_keys* updates
    waitOnFlip = False
    if instruct_5_keys.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruct_5_keys.frameNStart = frameN  # exact frame index
        instruct_5_keys.tStart = t  # local t and not account for scr refresh
        instruct_5_keys.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruct_5_keys, 'tStartRefresh')  # time at next scr refresh
        instruct_5_keys.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(instruct_5_keys.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instruct_5_keys.status == STARTED and not waitOnFlip:
        theseKeys = instruct_5_keys.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # *instruct_text_9* updates
    if instruct_text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruct_text_9.frameNStart = frameN  # exact frame index
        instruct_text_9.tStart = t  # local t and not account for scr refresh
        instruct_text_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruct_text_9, 'tStartRefresh')  # time at next scr refresh
        instruct_text_9.setAutoDraw(True)
    
    # *instruct_text_10* updates
    if instruct_text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruct_text_10.frameNStart = frameN  # exact frame index
        instruct_text_10.tStart = t  # local t and not account for scr refresh
        instruct_text_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruct_text_10, 'tStartRefresh')  # time at next scr refresh
        instruct_text_10.setAutoDraw(True)
    
    # *TutArrowTop_2* updates
    if TutArrowTop_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TutArrowTop_2.frameNStart = frameN  # exact frame index
        TutArrowTop_2.tStart = t  # local t and not account for scr refresh
        TutArrowTop_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TutArrowTop_2, 'tStartRefresh')  # time at next scr refresh
        TutArrowTop_2.setAutoDraw(True)
    
    # *TutArrowBottom_2* updates
    if TutArrowBottom_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TutArrowBottom_2.frameNStart = frameN  # exact frame index
        TutArrowBottom_2.tStart = t  # local t and not account for scr refresh
        TutArrowBottom_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TutArrowBottom_2, 'tStartRefresh')  # time at next scr refresh
        TutArrowBottom_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruct_5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruct_5"-------
for thisComponent in instruct_5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Tutbackdrop_3.started', Tutbackdrop_3.tStartRefresh)
thisExp.addData('Tutbackdrop_3.stopped', Tutbackdrop_3.tStopRefresh)
thisExp.addData('instruct_text_9.started', instruct_text_9.tStartRefresh)
thisExp.addData('instruct_text_9.stopped', instruct_text_9.tStopRefresh)
thisExp.addData('instruct_text_10.started', instruct_text_10.tStartRefresh)
thisExp.addData('instruct_text_10.stopped', instruct_text_10.tStopRefresh)
thisExp.addData('TutArrowTop_2.started', TutArrowTop_2.tStartRefresh)
thisExp.addData('TutArrowTop_2.stopped', TutArrowTop_2.tStopRefresh)
thisExp.addData('TutArrowBottom_2.started', TutArrowBottom_2.tStartRefresh)
thisExp.addData('TutArrowBottom_2.stopped', TutArrowBottom_2.tStopRefresh)
# the Routine "instruct_5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruct_6"-------
# update component parameters for each repeat
instruct_6_keys.keys = []
instruct_6_keys.rt = []
# keep track of which components have finished
instruct_6Components = [Tutbackdrop_5, instruct_6_keys, instruct_text_11, instruct_text_12, TutArrowTop_3]
for thisComponent in instruct_6Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruct_6Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "instruct_6"-------
while continueRoutine:
    # get current time
    t = instruct_6Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruct_6Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Tutbackdrop_5* updates
    if Tutbackdrop_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Tutbackdrop_5.frameNStart = frameN  # exact frame index
        Tutbackdrop_5.tStart = t  # local t and not account for scr refresh
        Tutbackdrop_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Tutbackdrop_5, 'tStartRefresh')  # time at next scr refresh
        Tutbackdrop_5.setAutoDraw(True)
    
    # *instruct_6_keys* updates
    waitOnFlip = False
    if instruct_6_keys.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruct_6_keys.frameNStart = frameN  # exact frame index
        instruct_6_keys.tStart = t  # local t and not account for scr refresh
        instruct_6_keys.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruct_6_keys, 'tStartRefresh')  # time at next scr refresh
        instruct_6_keys.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(instruct_6_keys.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instruct_6_keys.status == STARTED and not waitOnFlip:
        theseKeys = instruct_6_keys.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # *instruct_text_11* updates
    if instruct_text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruct_text_11.frameNStart = frameN  # exact frame index
        instruct_text_11.tStart = t  # local t and not account for scr refresh
        instruct_text_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruct_text_11, 'tStartRefresh')  # time at next scr refresh
        instruct_text_11.setAutoDraw(True)
    
    # *instruct_text_12* updates
    if instruct_text_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruct_text_12.frameNStart = frameN  # exact frame index
        instruct_text_12.tStart = t  # local t and not account for scr refresh
        instruct_text_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruct_text_12, 'tStartRefresh')  # time at next scr refresh
        instruct_text_12.setAutoDraw(True)
    
    # *TutArrowTop_3* updates
    if TutArrowTop_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        TutArrowTop_3.frameNStart = frameN  # exact frame index
        TutArrowTop_3.tStart = t  # local t and not account for scr refresh
        TutArrowTop_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(TutArrowTop_3, 'tStartRefresh')  # time at next scr refresh
        TutArrowTop_3.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruct_6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruct_6"-------
for thisComponent in instruct_6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Tutbackdrop_5.started', Tutbackdrop_5.tStartRefresh)
thisExp.addData('Tutbackdrop_5.stopped', Tutbackdrop_5.tStopRefresh)
thisExp.addData('instruct_text_11.started', instruct_text_11.tStartRefresh)
thisExp.addData('instruct_text_11.stopped', instruct_text_11.tStopRefresh)
thisExp.addData('instruct_text_12.started', instruct_text_12.tStartRefresh)
thisExp.addData('instruct_text_12.stopped', instruct_text_12.tStopRefresh)
thisExp.addData('TutArrowTop_3.started', TutArrowTop_3.tStartRefresh)
thisExp.addData('TutArrowTop_3.stopped', TutArrowTop_3.tStopRefresh)
# the Routine "instruct_6" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruct_7"-------
# update component parameters for each repeat
instruct_7_keys.keys = []
instruct_7_keys.rt = []
# keep track of which components have finished
instruct_7Components = [instruct_7_keys, instruct_text_13, instruct_text_14]
for thisComponent in instruct_7Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruct_7Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "instruct_7"-------
while continueRoutine:
    # get current time
    t = instruct_7Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruct_7Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruct_7_keys* updates
    waitOnFlip = False
    if instruct_7_keys.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruct_7_keys.frameNStart = frameN  # exact frame index
        instruct_7_keys.tStart = t  # local t and not account for scr refresh
        instruct_7_keys.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruct_7_keys, 'tStartRefresh')  # time at next scr refresh
        instruct_7_keys.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(instruct_7_keys.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instruct_7_keys.status == STARTED and not waitOnFlip:
        theseKeys = instruct_7_keys.getKeys(keyList=['space', 'right', 'left'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # *instruct_text_13* updates
    if instruct_text_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruct_text_13.frameNStart = frameN  # exact frame index
        instruct_text_13.tStart = t  # local t and not account for scr refresh
        instruct_text_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruct_text_13, 'tStartRefresh')  # time at next scr refresh
        instruct_text_13.setAutoDraw(True)
    
    # *instruct_text_14* updates
    if instruct_text_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruct_text_14.frameNStart = frameN  # exact frame index
        instruct_text_14.tStart = t  # local t and not account for scr refresh
        instruct_text_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruct_text_14, 'tStartRefresh')  # time at next scr refresh
        instruct_text_14.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruct_7Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruct_7"-------
for thisComponent in instruct_7Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instruct_text_13.started', instruct_text_13.tStartRefresh)
thisExp.addData('instruct_text_13.stopped', instruct_text_13.tStopRefresh)
thisExp.addData('instruct_text_14.started', instruct_text_14.tStartRefresh)
thisExp.addData('instruct_text_14.stopped', instruct_text_14.tStopRefresh)
# the Routine "instruct_7" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Tymula ConditionsModded.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    Red_Square.setPos((RiskXPos, 0.165))
    Blue_Square.setPos((RiskXPos, -0.165))
    sure.setPos([SureXPos,0])
    sure.setText(Sure)
    Option_One.setPos((OptionOneXPos, 0.4))
    Option_One.setText(OptionOne)
    Option_Two.setPos((OptionTwoXPos, -0.4))
    Option_Two.setText(OptionTwo)
    Risk_Text_Top.setPos((RiskX, 0.28))
    Risk_Text_Top.setText(Risk)
    Risk_Text_Bottom.setPos((RiskX, -0.28))
    Risk_Text_Bottom.setText(Risk2)
    Ambiguity_Bar.setPos((RiskXPos, 0))
    Ambiguity_Bar.setSize((0.42, AmbiguityBarH))
    # keep track of which components have finished
    trialComponents = [key_resp, Red_Square, Blue_Square, sure, or_text, Option_One, Option_Two, Risk_Text_Top, Risk_Text_Bottom, Ambiguity_Bar]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['left', 'right'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp.keys = theseKeys.name  # just the last key pressed
                key_resp.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # *Red_Square* updates
        if Red_Square.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Red_Square.frameNStart = frameN  # exact frame index
            Red_Square.tStart = t  # local t and not account for scr refresh
            Red_Square.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Red_Square, 'tStartRefresh')  # time at next scr refresh
            Red_Square.setAutoDraw(True)
        
        # *Blue_Square* updates
        if Blue_Square.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Blue_Square.frameNStart = frameN  # exact frame index
            Blue_Square.tStart = t  # local t and not account for scr refresh
            Blue_Square.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Blue_Square, 'tStartRefresh')  # time at next scr refresh
            Blue_Square.setAutoDraw(True)
        
        # *sure* updates
        if sure.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sure.frameNStart = frameN  # exact frame index
            sure.tStart = t  # local t and not account for scr refresh
            sure.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sure, 'tStartRefresh')  # time at next scr refresh
            sure.setAutoDraw(True)
        
        # *or_text* updates
        if or_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            or_text.frameNStart = frameN  # exact frame index
            or_text.tStart = t  # local t and not account for scr refresh
            or_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(or_text, 'tStartRefresh')  # time at next scr refresh
            or_text.setAutoDraw(True)
        
        # *Option_One* updates
        if Option_One.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Option_One.frameNStart = frameN  # exact frame index
            Option_One.tStart = t  # local t and not account for scr refresh
            Option_One.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Option_One, 'tStartRefresh')  # time at next scr refresh
            Option_One.setAutoDraw(True)
        
        # *Option_Two* updates
        if Option_Two.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Option_Two.frameNStart = frameN  # exact frame index
            Option_Two.tStart = t  # local t and not account for scr refresh
            Option_Two.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Option_Two, 'tStartRefresh')  # time at next scr refresh
            Option_Two.setAutoDraw(True)
        
        # *Risk_Text_Top* updates
        if Risk_Text_Top.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Risk_Text_Top.frameNStart = frameN  # exact frame index
            Risk_Text_Top.tStart = t  # local t and not account for scr refresh
            Risk_Text_Top.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Risk_Text_Top, 'tStartRefresh')  # time at next scr refresh
            Risk_Text_Top.setAutoDraw(True)
        
        # *Risk_Text_Bottom* updates
        if Risk_Text_Bottom.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Risk_Text_Bottom.frameNStart = frameN  # exact frame index
            Risk_Text_Bottom.tStart = t  # local t and not account for scr refresh
            Risk_Text_Bottom.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Risk_Text_Bottom, 'tStartRefresh')  # time at next scr refresh
            Risk_Text_Bottom.setAutoDraw(True)
        
        # *Ambiguity_Bar* updates
        if Ambiguity_Bar.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Ambiguity_Bar.frameNStart = frameN  # exact frame index
            Ambiguity_Bar.tStart = t  # local t and not account for scr refresh
            Ambiguity_Bar.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Ambiguity_Bar, 'tStartRefresh')  # time at next scr refresh
            Ambiguity_Bar.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    trials.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    trials.addData('key_resp.started', key_resp.tStartRefresh)
    trials.addData('key_resp.stopped', key_resp.tStopRefresh)
    trials.addData('Red_Square.started', Red_Square.tStartRefresh)
    trials.addData('Red_Square.stopped', Red_Square.tStopRefresh)
    trials.addData('Blue_Square.started', Blue_Square.tStartRefresh)
    trials.addData('Blue_Square.stopped', Blue_Square.tStopRefresh)
    trials.addData('sure.started', sure.tStartRefresh)
    trials.addData('sure.stopped', sure.tStopRefresh)
    trials.addData('or_text.started', or_text.tStartRefresh)
    trials.addData('or_text.stopped', or_text.tStopRefresh)
    trials.addData('Option_One.started', Option_One.tStartRefresh)
    trials.addData('Option_One.stopped', Option_One.tStopRefresh)
    trials.addData('Option_Two.started', Option_Two.tStartRefresh)
    trials.addData('Option_Two.stopped', Option_Two.tStopRefresh)
    trials.addData('Risk_Text_Top.started', Risk_Text_Top.tStartRefresh)
    trials.addData('Risk_Text_Top.stopped', Risk_Text_Top.tStopRefresh)
    trials.addData('Risk_Text_Bottom.started', Risk_Text_Bottom.tStartRefresh)
    trials.addData('Risk_Text_Bottom.stopped', Risk_Text_Bottom.tStopRefresh)
    trials.addData('Ambiguity_Bar.started', Ambiguity_Bar.tStartRefresh)
    trials.addData('Ambiguity_Bar.stopped', Ambiguity_Bar.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "endscreen"-------
# update component parameters for each repeat
endscreen_keys.keys = []
endscreen_keys.rt = []
# keep track of which components have finished
endscreenComponents = [endscreen_keys, endscreen_text, finalscore_text]
for thisComponent in endscreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endscreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "endscreen"-------
while continueRoutine:
    # get current time
    t = endscreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endscreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *endscreen_keys* updates
    waitOnFlip = False
    if endscreen_keys.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endscreen_keys.frameNStart = frameN  # exact frame index
        endscreen_keys.tStart = t  # local t and not account for scr refresh
        endscreen_keys.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endscreen_keys, 'tStartRefresh')  # time at next scr refresh
        endscreen_keys.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(endscreen_keys.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if endscreen_keys.status == STARTED and not waitOnFlip:
        theseKeys = endscreen_keys.getKeys(keyList=['q'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # *endscreen_text* updates
    if endscreen_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endscreen_text.frameNStart = frameN  # exact frame index
        endscreen_text.tStart = t  # local t and not account for scr refresh
        endscreen_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endscreen_text, 'tStartRefresh')  # time at next scr refresh
        endscreen_text.setAutoDraw(True)
    
    # *finalscore_text* updates
    if finalscore_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finalscore_text.frameNStart = frameN  # exact frame index
        finalscore_text.tStart = t  # local t and not account for scr refresh
        finalscore_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finalscore_text, 'tStartRefresh')  # time at next scr refresh
        finalscore_text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endscreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "endscreen"-------
for thisComponent in endscreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('endscreen_text.started', endscreen_text.tStartRefresh)
thisExp.addData('endscreen_text.stopped', endscreen_text.tStopRefresh)
thisExp.addData('finalscore_text.started', finalscore_text.tStartRefresh)
thisExp.addData('finalscore_text.stopped', finalscore_text.tStopRefresh)
# the Routine "endscreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
