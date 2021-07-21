# What is this thing?
Every day I (am supposed to) repeat the same chores at around the same time. Every day I struggle to achieve the simplest tasks as a result of being an extremely distractable person.  
This device is meant to provide a quick look at all my pending tasks for the day. This is meant to replace my alarms, calendar events and notepad scratchings.  

There will be a dedicated 'always on' display to only show the most relevant events (maybe with some nice wallpapers) that are to be addressed in the coming hours. By filtering the things I have to focus on, I can (hopefully) keep a clear head and get to what needs doing.  


&nbsp;
# What does it do?
The functionality I am aiming for is a event tracker/alarm. A notification can be ignored easier than a flashing display on your desk.  
*For my day to day use, it will be making sure I go have three meals a day and don't forget to work out.*
- Keeps track of repeating chores 
    - Work out
    - Check emails
    - Laundry
    - Brush teeth
- Keeps track of meetings and my timetable 
- Keeps one off reminders for miscellaneous use (need some kind of web interface to add ad hoc events) 

<div align='center'>

![Furious typing][furioustyping]  
*me creating reminders and events before I forget all about them*

</div>

When there is some event that needs your attention (Winter orientation starts in ten minutes), the device catches your attention by flashing or beeping (depending on h/w).  
**Congratulations! It is now unlikely you will miss the event.**


&nbsp;
# How does it do this stuff?
Defined events are stored in a DB, checked at regular intervals. As an event's due time approaches the item is displayed with more prominence to catch your attention.  
The device itself will be querying this DB regularly to catch updates. The interface will likely be a rotary encoder and buttons to select items and either mark them done, skip or postpone them.  

<div align='center'>

![how does it work][yeahscience]

</div>

# Hardware choices
Beginning with a raspberry pi zero to run python code. The database is currently a mysql server running on a local NAS.  
Two rotary push button encoders have been added. They are using an Encoder library I found and modified (to deal with read voltages on the Pi0). 

    Subject to change based on h/w limitations 

&nbsp;

# Progress
Prototype 0 is a Nokia 3310 LCD screen with two rotary encoders (with push buttons) (picture in images/).  Very simple functionality only. 

Plans for Prototype 1: I'm rolling some wallpaper program into this, and making it an 'always on' picture frame - the notifications/events will be added as layers of text
Framebuffer programming done by someone else: https://github.com/grz0zrg/fbg
This should work to add images and text from the local fs.

[memes]: <>
[prot0]: images/circ_board.jpg "Perf board prototype, dust city"
[furioustyping]: https://media.giphy.com/media/Wer1aEweDWq2Y/giphy.gif "me creating reminders and events before I forget all about them"
[yeahscience]: https://media.giphy.com/media/qCj1NK1rxtnna/giphy.gif "Yeah! Science!"
