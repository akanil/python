# template for "Stopwatch: The Game"
import simplegui
# define global variables

formatted_time = "0:00.0"
t = 0
started =False
no_of_success=0
no_of_attempts=0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global formatted_time
    formatted_time = str(t)
    #get the D
    D = t%10
    temp = t/10
    #get the A
    A=int(temp/60)
    #get the BC
    BC= int(temp%60)
    formatted_time = str(A)+":"+str('%02d' % BC)+"."+str(D)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
#start function defination
def start():
    global started
    timer.start()
    started=True


#stop function defination
def stop():
    global started, no_of_success, no_of_attempts
    timer.stop()
    if started:
        if (t%10==0):
            no_of_success+=1
        started=False
        no_of_attempts+=1
           


#reset function defination
def reset():
    global started, no_of_success, no_of_attempts
    timer.stop()
    no_of_success=0
    no_of_attempts=0
    t=0
    started=0
    format(t)


# define event handler for timer with 0.1 sec interval
#timer_handler defination
def timer_handler():
    global t
    t+=1
    format(t)
    
    
# define draw handler
#draw handler defination
def draw(canvas):
    #canvas.draw_text('A', (20, 20), 12, 'Red')
    canvas.draw_text(formatted_time,[100,150],25, "White")
    canvas.draw_text(str(no_of_success),[200,40],25,"Green")
    canvas.draw_text("/",[214,40],25,"White")
    canvas.draw_text(str(no_of_attempts),[225,40],25,"Red")

# create frame
#simplegui.create_frame(title, canvas_width, canvas_height)
frame = simplegui.create_frame('MyFrame', 275, 275)

# register event handlers
#frame.add_button('Label 1', button_handler)
frame.add_button("Start",start,150)
frame.add_button("Stop",stop,150)
frame.add_button("Reset",reset,150)

timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw)


# start frame
frame.start()

# Please remember to review the grading rubric
