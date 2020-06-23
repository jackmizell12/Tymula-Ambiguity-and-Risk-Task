/************************** 
 * Tymula Experiment Test *
 **************************/

import { PsychoJS } from 'https://pavlovia.org/lib/core.js';
import * as core from 'https://pavlovia.org/lib/core.js';
import { TrialHandler } from 'https://pavlovia.org/lib/data.js';
import { Scheduler } from 'https://pavlovia.org/lib/util.js';
import * as util from 'https://pavlovia.org/lib/util.js';
import * as visual from 'https://pavlovia.org/lib/visual.js';
import { Sound } from 'https://pavlovia.org/lib/sound.js';

// init psychoJS:
var psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: false,
  color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'Tymula Experiment';  // from the Builder filename that created this script
let expInfo = {'passcode': ''};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(instruct_1RoutineBegin);
flowScheduler.add(instruct_1RoutineEachFrame);
flowScheduler.add(instruct_1RoutineEnd);
flowScheduler.add(instruct_2RoutineBegin);
flowScheduler.add(instruct_2RoutineEachFrame);
flowScheduler.add(instruct_2RoutineEnd);
flowScheduler.add(instruct_3RoutineBegin);
flowScheduler.add(instruct_3RoutineEachFrame);
flowScheduler.add(instruct_3RoutineEnd);
flowScheduler.add(instruct_4RoutineBegin);
flowScheduler.add(instruct_4RoutineEachFrame);
flowScheduler.add(instruct_4RoutineEnd);
flowScheduler.add(instruct_5RoutineBegin);
flowScheduler.add(instruct_5RoutineEachFrame);
flowScheduler.add(instruct_5RoutineEnd);
flowScheduler.add(instruct_6RoutineBegin);
flowScheduler.add(instruct_6RoutineEachFrame);
flowScheduler.add(instruct_6RoutineEnd);
flowScheduler.add(instruct_7RoutineBegin);
flowScheduler.add(instruct_7RoutineEachFrame);
flowScheduler.add(instruct_7RoutineEnd);
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin, trialsLoopScheduler);
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(endscreenRoutineBegin);
flowScheduler.add(endscreenRoutineEachFrame);
flowScheduler.add(endscreenRoutineEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({expName, expInfo});

var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '3.2.3';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0/Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0/60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}

var instruct_1Clock;
var instruct_text_1;
var instruct_text_2;
var instruct_1_keys;
var instruct_2Clock;
var instruct_text_3;
var instruct_text_4;
var instruct_2_keys;
var tut_sure;
var instruct_3Clock;
var Tutbackdrop;
var instruct_3_keys;
var instruct_text_5;
var instruct_text_6;
var instruct_4Clock;
var Tutbackdrop_2;
var instruct_4_keys;
var instruct_text_7;
var instruct_text_8;
var TutArrowTop;
var TutArrowBottom;
var instruct_5Clock;
var Tutbackdrop_3;
var instruct_5_keys;
var instruct_text_9;
var instruct_text_10;
var TutArrowTop_2;
var TutArrowBottom_2;
var instruct_6Clock;
var Tutbackdrop_5;
var instruct_6_keys;
var instruct_text_11;
var instruct_text_12;
var TutArrowTop_3;
var instruct_7Clock;
var instruct_7_keys;
var instruct_text_13;
var instruct_text_14;
var trialClock;
var key_resp;
var Red_Square;
var Blue_Square;
var sure;
var or_text;
var Option_One;
var Option_Two;
var Risk_Text_Top;
var Risk_Text_Bottom;
var Ambiguity_Bar;
var endscreenClock;
var endscreen_keys;
var endscreen_text;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "instruct_1"
  instruct_1Clock = new util.Clock();
  instruct_text_1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruct_text_1',
    text: 'In this task you will be asked to choose between two options.\nOne side will have a constant value and the other will have some chance of two different options.',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  instruct_text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruct_text_2',
    text: 'Press spacebar to continue',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.4)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  instruct_1_keys = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instruct_2"
  instruct_2Clock = new util.Clock();
  instruct_text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruct_text_3',
    text: 'One side will have the constant value shown, 5 in this case.',
    font: 'Arial',
    units : undefined, 
    pos: [0.25, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  instruct_text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruct_text_4',
    text: 'Press spacebar to continue',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.4)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  instruct_2_keys = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  tut_sure = new visual.TextStim({
    win: psychoJS.window,
    name: 'tut_sure',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.3,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "instruct_3"
  instruct_3Clock = new util.Clock();
  Tutbackdrop = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Tutbackdrop', units : undefined, 
    image : 'TutorialBackground1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [1.5, 1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  instruct_3_keys = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  instruct_text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruct_text_5',
    text: 'The other side will present you with a more complicated choice.',
    font: 'Arial',
    units : undefined, 
    pos: [(- 0.25), 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  instruct_text_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruct_text_6',
    text: 'Press spacebar to continue',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.4)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "instruct_4"
  instruct_4Clock = new util.Clock();
  Tutbackdrop_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Tutbackdrop_2', units : undefined, 
    image : 'TutorialBackground1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [1.5, 1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  instruct_4_keys = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  instruct_text_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruct_text_7',
    text: 'The very top and bottom numbers are the two possible outcomes of this choice.',
    font: 'Arial',
    units : undefined, 
    pos: [(- 0.25), 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  instruct_text_8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruct_text_8',
    text: 'Press spacebar to continue',
    font: 'Arial',
    units : undefined, 
    pos: [(- 0.35), (- 0.4)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  TutArrowTop = new visual.ImageStim({
    win : psychoJS.window,
    name : 'TutArrowTop', units : undefined, 
    image : 'TutorialArrow.png', mask : undefined,
    ori : 0, pos : [0.15, 0.4], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  TutArrowBottom = new visual.ImageStim({
    win : psychoJS.window,
    name : 'TutArrowBottom', units : undefined, 
    image : 'TutorialArrow.png', mask : undefined,
    ori : 0, pos : [0.15, (- 0.4)], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -5.0 
  });
  // Initialize components for Routine "instruct_5"
  instruct_5Clock = new util.Clock();
  Tutbackdrop_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Tutbackdrop_3', units : undefined, 
    image : 'TutorialBackground1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [1.5, 1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  instruct_5_keys = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  instruct_text_9 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruct_text_9',
    text: 'The innermost numbers are the percentage chance of each outcome.',
    font: 'Arial',
    units : undefined, 
    pos: [(- 0.25), 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  instruct_text_10 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruct_text_10',
    text: 'Press spacebar to continue',
    font: 'Arial',
    units : undefined, 
    pos: [(- 0.35), (- 0.4)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  TutArrowTop_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'TutArrowTop_2', units : undefined, 
    image : 'TutorialArrow.png', mask : undefined,
    ori : 0, pos : [0.15, 0.28], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  TutArrowBottom_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'TutArrowBottom_2', units : undefined, 
    image : 'TutorialArrow.png', mask : undefined,
    ori : 0, pos : [0.15, (- 0.28)], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -5.0 
  });
  // Initialize components for Routine "instruct_6"
  instruct_6Clock = new util.Clock();
  Tutbackdrop_5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Tutbackdrop_5', units : undefined, 
    image : 'TutorialBackground2.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [1.5, 1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  instruct_6_keys = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  instruct_text_11 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruct_text_11',
    text: 'Sometimes a grey bar will obscure the middle of the choice so the exact probabilities of the outcomes are unknown.',
    font: 'Arial',
    units : undefined, 
    pos: [(- 0.25), 0.25], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  instruct_text_12 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruct_text_12',
    text: 'Press spacebar to continue',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.4)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  TutArrowTop_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'TutArrowTop_3', units : undefined, 
    image : 'TutorialArrow.png', mask : undefined,
    ori : 0, pos : [0.15, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  // Initialize components for Routine "instruct_7"
  instruct_7Clock = new util.Clock();
  instruct_7_keys = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  instruct_text_13 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruct_text_13',
    text: ' You will get a bonus based on the points you earned from 3 random trials in the game. So choose wisely. you made.\nTo choose between the right and left choices use the right and left arrow keys.\nGood luck!',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  instruct_text_14 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruct_text_14',
    text: 'Press spacebar, right, or left to continue',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.4)], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  key_resp = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Red_Square = new visual.Rect ({
    win: psychoJS.window, name: 'Red_Square', 
    width: [0.4, 0.325][0], height: [0.4, 0.325][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1.0, (- 1.0), (- 1.0)]),
    fillColor: new util.Color([1.0, (- 1.0), (- 1.0)]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  Blue_Square = new visual.Rect ({
    win: psychoJS.window, name: 'Blue_Square', 
    width: [0.4, 0.325][0], height: [0.4, 0.325][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([(- 1.0), 0.004, 1.0]),
    fillColor: new util.Color([(- 1.0), 0.004, 1.0]),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  sure = new visual.TextStim({
    win: psychoJS.window,
    name: 'sure',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.3,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  or_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'or_text',
    text: 'or',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.15,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  Option_One = new visual.TextStim({
    win: psychoJS.window,
    name: 'Option_One',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('White'),  opacity: 1,
    depth: -5.0 
  });
  
  Option_Two = new visual.TextStim({
    win: psychoJS.window,
    name: 'Option_Two',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('White'),  opacity: 1,
    depth: -6.0 
  });
  
  Risk_Text_Top = new visual.TextStim({
    win: psychoJS.window,
    name: 'Risk_Text_Top',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('White'),  opacity: 1,
    depth: -7.0 
  });
  
  Risk_Text_Bottom = new visual.TextStim({
    win: psychoJS.window,
    name: 'Risk_Text_Bottom',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('White'),  opacity: 1,
    depth: -8.0 
  });
  
  Ambiguity_Bar = new visual.Rect ({
    win: psychoJS.window, name: 'Ambiguity_Bar', 
    width: [1.0, 1.0][0], height: [1.0, 1.0][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    fillColor: new util.Color([0.004, 0.004, 0.004]),
    opacity: 1, depth: -9, interpolate: true,
  });
  
  // Initialize components for Routine "endscreen"
  endscreenClock = new util.Clock();
  endscreen_keys = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  endscreen_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'endscreen_text',
    text: 'Thank you for participating! Press q to finish!\n\n',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0.25], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

var t;
var frameN;
var instruct_1Components;
function instruct_1RoutineBegin() {
  //------Prepare to start Routine 'instruct_1'-------
  t = 0;
  instruct_1Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  instruct_1_keys.keys = undefined;
  instruct_1_keys.rt = undefined;
  // keep track of which components have finished
  instruct_1Components = [];
  instruct_1Components.push(instruct_text_1);
  instruct_1Components.push(instruct_text_2);
  instruct_1Components.push(instruct_1_keys);
  
  for (const thisComponent of instruct_1Components)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

var continueRoutine;
function instruct_1RoutineEachFrame() {
  //------Loop for each frame of Routine 'instruct_1'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = instruct_1Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *instruct_text_1* updates
  if (t >= 0.0 && instruct_text_1.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instruct_text_1.tStart = t;  // (not accounting for frame time here)
    instruct_text_1.frameNStart = frameN;  // exact frame index
    instruct_text_1.setAutoDraw(true);
  }

  
  // *instruct_text_2* updates
  if (t >= 0.0 && instruct_text_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instruct_text_2.tStart = t;  // (not accounting for frame time here)
    instruct_text_2.frameNStart = frameN;  // exact frame index
    instruct_text_2.setAutoDraw(true);
  }

  
  // *instruct_1_keys* updates
  if (t >= 0.0 && instruct_1_keys.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instruct_1_keys.tStart = t;  // (not accounting for frame time here)
    instruct_1_keys.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { instruct_1_keys.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { instruct_1_keys.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { instruct_1_keys.clearEvents(); });
  }

  if (instruct_1_keys.status === PsychoJS.Status.STARTED) {
    let theseKeys = instruct_1_keys.getKeys({keyList: ['space'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of instruct_1Components)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function instruct_1RoutineEnd() {
  //------Ending Routine 'instruct_1'-------
  for (const thisComponent of instruct_1Components) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // the Routine "instruct_1" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var instruct_2Components;
function instruct_2RoutineBegin() {
  //------Prepare to start Routine 'instruct_2'-------
  t = 0;
  instruct_2Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  instruct_2_keys.keys = undefined;
  instruct_2_keys.rt = undefined;
  tut_sure.setPos([(- 0.5), 0]);
  tut_sure.setText('5');
  // keep track of which components have finished
  instruct_2Components = [];
  instruct_2Components.push(instruct_text_3);
  instruct_2Components.push(instruct_text_4);
  instruct_2Components.push(instruct_2_keys);
  instruct_2Components.push(tut_sure);
  
  for (const thisComponent of instruct_2Components)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function instruct_2RoutineEachFrame() {
  //------Loop for each frame of Routine 'instruct_2'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = instruct_2Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *instruct_text_3* updates
  if (t >= 0.0 && instruct_text_3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instruct_text_3.tStart = t;  // (not accounting for frame time here)
    instruct_text_3.frameNStart = frameN;  // exact frame index
    instruct_text_3.setAutoDraw(true);
  }

  
  // *instruct_text_4* updates
  if (t >= 0.0 && instruct_text_4.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instruct_text_4.tStart = t;  // (not accounting for frame time here)
    instruct_text_4.frameNStart = frameN;  // exact frame index
    instruct_text_4.setAutoDraw(true);
  }

  
  // *instruct_2_keys* updates
  if (t >= 0.0 && instruct_2_keys.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instruct_2_keys.tStart = t;  // (not accounting for frame time here)
    instruct_2_keys.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { instruct_2_keys.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { instruct_2_keys.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { instruct_2_keys.clearEvents(); });
  }

  if (instruct_2_keys.status === PsychoJS.Status.STARTED) {
    let theseKeys = instruct_2_keys.getKeys({keyList: ['space'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  
  // *tut_sure* updates
  if (t >= 0.0 && tut_sure.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    tut_sure.tStart = t;  // (not accounting for frame time here)
    tut_sure.frameNStart = frameN;  // exact frame index
    tut_sure.setAutoDraw(true);
  }

  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of instruct_2Components)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function instruct_2RoutineEnd() {
  //------Ending Routine 'instruct_2'-------
  for (const thisComponent of instruct_2Components) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // the Routine "instruct_2" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var instruct_3Components;
function instruct_3RoutineBegin() {
  //------Prepare to start Routine 'instruct_3'-------
  t = 0;
  instruct_3Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  instruct_3_keys.keys = undefined;
  instruct_3_keys.rt = undefined;
  // keep track of which components have finished
  instruct_3Components = [];
  instruct_3Components.push(Tutbackdrop);
  instruct_3Components.push(instruct_3_keys);
  instruct_3Components.push(instruct_text_5);
  instruct_3Components.push(instruct_text_6);
  
  for (const thisComponent of instruct_3Components)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function instruct_3RoutineEachFrame() {
  //------Loop for each frame of Routine 'instruct_3'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = instruct_3Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *Tutbackdrop* updates
  if (t >= 0.0 && Tutbackdrop.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Tutbackdrop.tStart = t;  // (not accounting for frame time here)
    Tutbackdrop.frameNStart = frameN;  // exact frame index
    Tutbackdrop.setAutoDraw(true);
  }

  
  // *instruct_3_keys* updates
  if (t >= 0.0 && instruct_3_keys.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instruct_3_keys.tStart = t;  // (not accounting for frame time here)
    instruct_3_keys.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { instruct_3_keys.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { instruct_3_keys.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { instruct_3_keys.clearEvents(); });
  }

  if (instruct_3_keys.status === PsychoJS.Status.STARTED) {
    let theseKeys = instruct_3_keys.getKeys({keyList: ['space'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  
  // *instruct_text_5* updates
  if (t >= 0.0 && instruct_text_5.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instruct_text_5.tStart = t;  // (not accounting for frame time here)
    instruct_text_5.frameNStart = frameN;  // exact frame index
    instruct_text_5.setAutoDraw(true);
  }

  
  // *instruct_text_6* updates
  if (t >= 0.0 && instruct_text_6.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instruct_text_6.tStart = t;  // (not accounting for frame time here)
    instruct_text_6.frameNStart = frameN;  // exact frame index
    instruct_text_6.setAutoDraw(true);
  }

  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of instruct_3Components)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function instruct_3RoutineEnd() {
  //------Ending Routine 'instruct_3'-------
  for (const thisComponent of instruct_3Components) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // the Routine "instruct_3" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var instruct_4Components;
function instruct_4RoutineBegin() {
  //------Prepare to start Routine 'instruct_4'-------
  t = 0;
  instruct_4Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  instruct_4_keys.keys = undefined;
  instruct_4_keys.rt = undefined;
  // keep track of which components have finished
  instruct_4Components = [];
  instruct_4Components.push(Tutbackdrop_2);
  instruct_4Components.push(instruct_4_keys);
  instruct_4Components.push(instruct_text_7);
  instruct_4Components.push(instruct_text_8);
  instruct_4Components.push(TutArrowTop);
  instruct_4Components.push(TutArrowBottom);
  
  for (const thisComponent of instruct_4Components)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function instruct_4RoutineEachFrame() {
  //------Loop for each frame of Routine 'instruct_4'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = instruct_4Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *Tutbackdrop_2* updates
  if (t >= 0.0 && Tutbackdrop_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Tutbackdrop_2.tStart = t;  // (not accounting for frame time here)
    Tutbackdrop_2.frameNStart = frameN;  // exact frame index
    Tutbackdrop_2.setAutoDraw(true);
  }

  
  // *instruct_4_keys* updates
  if (t >= 0.0 && instruct_4_keys.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instruct_4_keys.tStart = t;  // (not accounting for frame time here)
    instruct_4_keys.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { instruct_4_keys.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { instruct_4_keys.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { instruct_4_keys.clearEvents(); });
  }

  if (instruct_4_keys.status === PsychoJS.Status.STARTED) {
    let theseKeys = instruct_4_keys.getKeys({keyList: ['space'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  
  // *instruct_text_7* updates
  if (t >= 0.0 && instruct_text_7.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instruct_text_7.tStart = t;  // (not accounting for frame time here)
    instruct_text_7.frameNStart = frameN;  // exact frame index
    instruct_text_7.setAutoDraw(true);
  }

  
  // *instruct_text_8* updates
  if (t >= 0.0 && instruct_text_8.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instruct_text_8.tStart = t;  // (not accounting for frame time here)
    instruct_text_8.frameNStart = frameN;  // exact frame index
    instruct_text_8.setAutoDraw(true);
  }

  
  // *TutArrowTop* updates
  if (t >= 0.0 && TutArrowTop.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    TutArrowTop.tStart = t;  // (not accounting for frame time here)
    TutArrowTop.frameNStart = frameN;  // exact frame index
    TutArrowTop.setAutoDraw(true);
  }

  
  // *TutArrowBottom* updates
  if (t >= 0.0 && TutArrowBottom.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    TutArrowBottom.tStart = t;  // (not accounting for frame time here)
    TutArrowBottom.frameNStart = frameN;  // exact frame index
    TutArrowBottom.setAutoDraw(true);
  }

  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of instruct_4Components)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function instruct_4RoutineEnd() {
  //------Ending Routine 'instruct_4'-------
  for (const thisComponent of instruct_4Components) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // the Routine "instruct_4" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var instruct_5Components;
function instruct_5RoutineBegin() {
  //------Prepare to start Routine 'instruct_5'-------
  t = 0;
  instruct_5Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  instruct_5_keys.keys = undefined;
  instruct_5_keys.rt = undefined;
  // keep track of which components have finished
  instruct_5Components = [];
  instruct_5Components.push(Tutbackdrop_3);
  instruct_5Components.push(instruct_5_keys);
  instruct_5Components.push(instruct_text_9);
  instruct_5Components.push(instruct_text_10);
  instruct_5Components.push(TutArrowTop_2);
  instruct_5Components.push(TutArrowBottom_2);
  
  for (const thisComponent of instruct_5Components)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function instruct_5RoutineEachFrame() {
  //------Loop for each frame of Routine 'instruct_5'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = instruct_5Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *Tutbackdrop_3* updates
  if (t >= 0.0 && Tutbackdrop_3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Tutbackdrop_3.tStart = t;  // (not accounting for frame time here)
    Tutbackdrop_3.frameNStart = frameN;  // exact frame index
    Tutbackdrop_3.setAutoDraw(true);
  }

  
  // *instruct_5_keys* updates
  if (t >= 0.0 && instruct_5_keys.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instruct_5_keys.tStart = t;  // (not accounting for frame time here)
    instruct_5_keys.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { instruct_5_keys.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { instruct_5_keys.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { instruct_5_keys.clearEvents(); });
  }

  if (instruct_5_keys.status === PsychoJS.Status.STARTED) {
    let theseKeys = instruct_5_keys.getKeys({keyList: ['space'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  
  // *instruct_text_9* updates
  if (t >= 0.0 && instruct_text_9.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instruct_text_9.tStart = t;  // (not accounting for frame time here)
    instruct_text_9.frameNStart = frameN;  // exact frame index
    instruct_text_9.setAutoDraw(true);
  }

  
  // *instruct_text_10* updates
  if (t >= 0.0 && instruct_text_10.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instruct_text_10.tStart = t;  // (not accounting for frame time here)
    instruct_text_10.frameNStart = frameN;  // exact frame index
    instruct_text_10.setAutoDraw(true);
  }

  
  // *TutArrowTop_2* updates
  if (t >= 0.0 && TutArrowTop_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    TutArrowTop_2.tStart = t;  // (not accounting for frame time here)
    TutArrowTop_2.frameNStart = frameN;  // exact frame index
    TutArrowTop_2.setAutoDraw(true);
  }

  
  // *TutArrowBottom_2* updates
  if (t >= 0.0 && TutArrowBottom_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    TutArrowBottom_2.tStart = t;  // (not accounting for frame time here)
    TutArrowBottom_2.frameNStart = frameN;  // exact frame index
    TutArrowBottom_2.setAutoDraw(true);
  }

  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of instruct_5Components)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function instruct_5RoutineEnd() {
  //------Ending Routine 'instruct_5'-------
  for (const thisComponent of instruct_5Components) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // the Routine "instruct_5" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var instruct_6Components;
function instruct_6RoutineBegin() {
  //------Prepare to start Routine 'instruct_6'-------
  t = 0;
  instruct_6Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  instruct_6_keys.keys = undefined;
  instruct_6_keys.rt = undefined;
  // keep track of which components have finished
  instruct_6Components = [];
  instruct_6Components.push(Tutbackdrop_5);
  instruct_6Components.push(instruct_6_keys);
  instruct_6Components.push(instruct_text_11);
  instruct_6Components.push(instruct_text_12);
  instruct_6Components.push(TutArrowTop_3);
  
  for (const thisComponent of instruct_6Components)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function instruct_6RoutineEachFrame() {
  //------Loop for each frame of Routine 'instruct_6'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = instruct_6Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *Tutbackdrop_5* updates
  if (t >= 0.0 && Tutbackdrop_5.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Tutbackdrop_5.tStart = t;  // (not accounting for frame time here)
    Tutbackdrop_5.frameNStart = frameN;  // exact frame index
    Tutbackdrop_5.setAutoDraw(true);
  }

  
  // *instruct_6_keys* updates
  if (t >= 0.0 && instruct_6_keys.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instruct_6_keys.tStart = t;  // (not accounting for frame time here)
    instruct_6_keys.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { instruct_6_keys.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { instruct_6_keys.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { instruct_6_keys.clearEvents(); });
  }

  if (instruct_6_keys.status === PsychoJS.Status.STARTED) {
    let theseKeys = instruct_6_keys.getKeys({keyList: ['space'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  
  // *instruct_text_11* updates
  if (t >= 0.0 && instruct_text_11.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instruct_text_11.tStart = t;  // (not accounting for frame time here)
    instruct_text_11.frameNStart = frameN;  // exact frame index
    instruct_text_11.setAutoDraw(true);
  }

  
  // *instruct_text_12* updates
  if (t >= 0.0 && instruct_text_12.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instruct_text_12.tStart = t;  // (not accounting for frame time here)
    instruct_text_12.frameNStart = frameN;  // exact frame index
    instruct_text_12.setAutoDraw(true);
  }

  
  // *TutArrowTop_3* updates
  if (t >= 0.0 && TutArrowTop_3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    TutArrowTop_3.tStart = t;  // (not accounting for frame time here)
    TutArrowTop_3.frameNStart = frameN;  // exact frame index
    TutArrowTop_3.setAutoDraw(true);
  }

  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of instruct_6Components)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function instruct_6RoutineEnd() {
  //------Ending Routine 'instruct_6'-------
  for (const thisComponent of instruct_6Components) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // the Routine "instruct_6" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var instruct_7Components;
function instruct_7RoutineBegin() {
  //------Prepare to start Routine 'instruct_7'-------
  t = 0;
  instruct_7Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  instruct_7_keys.keys = undefined;
  instruct_7_keys.rt = undefined;
  // keep track of which components have finished
  instruct_7Components = [];
  instruct_7Components.push(instruct_7_keys);
  instruct_7Components.push(instruct_text_13);
  instruct_7Components.push(instruct_text_14);
  
  for (const thisComponent of instruct_7Components)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function instruct_7RoutineEachFrame() {
  //------Loop for each frame of Routine 'instruct_7'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = instruct_7Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *instruct_7_keys* updates
  if (t >= 0.0 && instruct_7_keys.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instruct_7_keys.tStart = t;  // (not accounting for frame time here)
    instruct_7_keys.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { instruct_7_keys.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { instruct_7_keys.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { instruct_7_keys.clearEvents(); });
  }

  if (instruct_7_keys.status === PsychoJS.Status.STARTED) {
    let theseKeys = instruct_7_keys.getKeys({keyList: ['space', 'right', 'left'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  
  // *instruct_text_13* updates
  if (t >= 0.0 && instruct_text_13.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instruct_text_13.tStart = t;  // (not accounting for frame time here)
    instruct_text_13.frameNStart = frameN;  // exact frame index
    instruct_text_13.setAutoDraw(true);
  }

  
  // *instruct_text_14* updates
  if (t >= 0.0 && instruct_text_14.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instruct_text_14.tStart = t;  // (not accounting for frame time here)
    instruct_text_14.frameNStart = frameN;  // exact frame index
    instruct_text_14.setAutoDraw(true);
  }

  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of instruct_7Components)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function instruct_7RoutineEnd() {
  //------Ending Routine 'instruct_7'-------
  for (const thisComponent of instruct_7Components) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // the Routine "instruct_7" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var trials;
var currentLoop;
function trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'Tymula ConditionsModded.xlsx',
    seed: undefined, name: 'trials'});
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrial of trials) {
    thisScheduler.add(importConditions(trials));
    thisScheduler.add(trialRoutineBegin);
    thisScheduler.add(trialRoutineEachFrame);
    thisScheduler.add(trialRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}

var trialComponents;
function trialRoutineBegin() {
  //------Prepare to start Routine 'trial'-------
  t = 0;
  trialClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  key_resp.keys = undefined;
  key_resp.rt = undefined;
  Red_Square.setPos([RiskXPos, 0.165]);
  Blue_Square.setPos([RiskXPos, (- 0.165)]);
  sure.setPos([SureXPos, 0]);
  sure.setText(Sure);
  Option_One.setPos([OptionOneXPos, 0.4]);
  Option_One.setText(OptionOne);
  Option_Two.setPos([OptionTwoXPos, (- 0.4)]);
  Option_Two.setText(OptionTwo);
  Risk_Text_Top.setPos([RiskX, 0.28]);
  Risk_Text_Top.setText(Risk);
  Risk_Text_Bottom.setPos([RiskX, (- 0.28)]);
  Risk_Text_Bottom.setText(Risk2);
  Ambiguity_Bar.setPos([RiskXPos, 0]);
  Ambiguity_Bar.setSize([0.42, AmbiguityBarH]);
  // keep track of which components have finished
  trialComponents = [];
  trialComponents.push(key_resp);
  trialComponents.push(Red_Square);
  trialComponents.push(Blue_Square);
  trialComponents.push(sure);
  trialComponents.push(or_text);
  trialComponents.push(Option_One);
  trialComponents.push(Option_Two);
  trialComponents.push(Risk_Text_Top);
  trialComponents.push(Risk_Text_Bottom);
  trialComponents.push(Ambiguity_Bar);
  
  for (const thisComponent of trialComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function trialRoutineEachFrame() {
  //------Loop for each frame of Routine 'trial'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = trialClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *key_resp* updates
  if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp.tStart = t;  // (not accounting for frame time here)
    key_resp.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
  }

  if (key_resp.status === PsychoJS.Status.STARTED) {
    let theseKeys = key_resp.getKeys({keyList: ['left', 'right'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      key_resp.keys = theseKeys[0].name;  // just the last key pressed
      key_resp.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  
  // *Red_Square* updates
  if (t >= 0.0 && Red_Square.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Red_Square.tStart = t;  // (not accounting for frame time here)
    Red_Square.frameNStart = frameN;  // exact frame index
    Red_Square.setAutoDraw(true);
  }

  
  // *Blue_Square* updates
  if (t >= 0.0 && Blue_Square.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Blue_Square.tStart = t;  // (not accounting for frame time here)
    Blue_Square.frameNStart = frameN;  // exact frame index
    Blue_Square.setAutoDraw(true);
  }

  
  // *sure* updates
  if (t >= 0.0 && sure.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    sure.tStart = t;  // (not accounting for frame time here)
    sure.frameNStart = frameN;  // exact frame index
    sure.setAutoDraw(true);
  }

  
  // *or_text* updates
  if (t >= 0.0 && or_text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    or_text.tStart = t;  // (not accounting for frame time here)
    or_text.frameNStart = frameN;  // exact frame index
    or_text.setAutoDraw(true);
  }

  
  // *Option_One* updates
  if (t >= 0.0 && Option_One.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Option_One.tStart = t;  // (not accounting for frame time here)
    Option_One.frameNStart = frameN;  // exact frame index
    Option_One.setAutoDraw(true);
  }

  
  // *Option_Two* updates
  if (t >= 0.0 && Option_Two.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Option_Two.tStart = t;  // (not accounting for frame time here)
    Option_Two.frameNStart = frameN;  // exact frame index
    Option_Two.setAutoDraw(true);
  }

  
  // *Risk_Text_Top* updates
  if (t >= 0.0 && Risk_Text_Top.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Risk_Text_Top.tStart = t;  // (not accounting for frame time here)
    Risk_Text_Top.frameNStart = frameN;  // exact frame index
    Risk_Text_Top.setAutoDraw(true);
  }

  
  // *Risk_Text_Bottom* updates
  if (t >= 0.0 && Risk_Text_Bottom.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Risk_Text_Bottom.tStart = t;  // (not accounting for frame time here)
    Risk_Text_Bottom.frameNStart = frameN;  // exact frame index
    Risk_Text_Bottom.setAutoDraw(true);
  }

  
  // *Ambiguity_Bar* updates
  if (t >= 0.0 && Ambiguity_Bar.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Ambiguity_Bar.tStart = t;  // (not accounting for frame time here)
    Ambiguity_Bar.frameNStart = frameN;  // exact frame index
    Ambiguity_Bar.setAutoDraw(true);
  }

  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of trialComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function trialRoutineEnd() {
  //------Ending Routine 'trial'-------
  for (const thisComponent of trialComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
  if (typeof key_resp.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
      routineTimer.reset();
      }
  
  key_resp.stop();
  // the Routine "trial" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var endscreenComponents;
function endscreenRoutineBegin() {
  //------Prepare to start Routine 'endscreen'-------
  t = 0;
  endscreenClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  endscreen_keys.keys = undefined;
  endscreen_keys.rt = undefined;
  // keep track of which components have finished
  endscreenComponents = [];
  endscreenComponents.push(endscreen_keys);
  endscreenComponents.push(endscreen_text);
  
  for (const thisComponent of endscreenComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function endscreenRoutineEachFrame() {
  //------Loop for each frame of Routine 'endscreen'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = endscreenClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *endscreen_keys* updates
  if (t >= 0.0 && endscreen_keys.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    endscreen_keys.tStart = t;  // (not accounting for frame time here)
    endscreen_keys.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { endscreen_keys.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { endscreen_keys.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { endscreen_keys.clearEvents(); });
  }

  if (endscreen_keys.status === PsychoJS.Status.STARTED) {
    let theseKeys = endscreen_keys.getKeys({keyList: ['q'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  
  // *endscreen_text* updates
  if (t >= 0.0 && endscreen_text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    endscreen_text.tStart = t;  // (not accounting for frame time here)
    endscreen_text.frameNStart = frameN;  // exact frame index
    endscreen_text.setAutoDraw(true);
  }

  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of endscreenComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function endscreenRoutineEnd() {
  //------Ending Routine 'endscreen'-------
  for (const thisComponent of endscreenComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // the Routine "endscreen" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}


function endLoopIteration({thisScheduler, isTrials=true}) {
  // ------Prepare for next entry------
  return function () {
    // ------Check if user ended loop early------
    if (currentLoop.finished) {
      // Check for and save orphaned data
      if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
        psychoJS.experiment.nextEntry();
      }
      thisScheduler.stop();
    } else if (isTrials) {
      psychoJS.experiment.nextEntry();
    }
  return Scheduler.Event.NEXT;
  };
}


function importConditions(loop) {
  const trialIndex = loop.getTrialIndex();
  return function () {
    loop.setTrialIndex(trialIndex);
    psychoJS.importAttributes(loop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});

  return Scheduler.Event.QUIT;
}
