import tkinter

import PIL.Image  # pip install pillow
import PIL.ImageTk
import cv2  # pip install opencv-python
from functools import partial       #We cannot give argument in button command.import
                                    #we only give function name so to overcome on this we require partisl from functool
import threading
import imutils                  #pip install imutils
import time
from playsound import playsound     #pip install playsound

stream = cv2.VideoCapture("Runout.mp4")

def play(speed):
    '''
    Function to play video
    :return:
    '''
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed, frame = stream.read()
    # frame = cv2.cvtColor(cv2.imread(frame1), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    canvas.create_text(400, 30, fill="white", font="Times 28 bold", text="Decision Pending")



def pending(decision):
    '''
    1. Displaying decision pending
    2. wait 1.5 sec
    3. Display Decision
    :param decision:
    :return:
    '''
    frame = cv2.cvtColor(cv2.imread("Pending.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    time.sleep(3)
    playsound("IplTone.mp3")
    if decision == 'OUT':
        decisonImg='OUT.jpg'
    else:
        decisonImg = 'Not.jpg'
    frame = cv2.cvtColor(cv2.imread(decisonImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    playsound("IplTone.mp3")

def out():
    thread = threading.Thread(target=pending, args=("OUT",))
    thread.daemon = 1
    thread.start()
    print("Decision is OUT")

def Not_out():
    thread = threading.Thread(target=pending, args=("NOT OUT",))
    thread.daemon = 1
    thread.start()
    print("Decision is NOT OUT")


# Setting width and height of main screen
SET_WIDTH = 815
SET_HEIGHT = 496

# tkinter GUI
window = tkinter.Tk()
window.title("Third Umpire Decision Review System")
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
cv_img = cv2.cvtColor(cv2.imread("Welcome1.jpg"), cv2.COLOR_BGR2RGB)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, ancho=tkinter.NW, image=photo)
canvas.pack()


#Control_Panel  (Buttons to control)

btn = tkinter.Button(window, text="<<Backward(fast)", width=50, command=partial(play, -20))
btn.pack()

btn = tkinter.Button(window, text="<<Backward(Slow)", width=50, command=partial(play, -2))
btn.pack()

btn = tkinter.Button(window, text="Forward(fast)>>", width=50, command=partial(play, 20))
btn.pack()

btn = tkinter.Button(window, text="Forward(Slow)>>", width=50, command=partial(play, 0.5))
btn.pack()

btn = tkinter.Button(window, text="OUT", width=50, command= out)
btn.pack()

btn = tkinter.Button(window, text="NOT OUT", width=50, command= Not_out)
btn.pack()

window.mainloop()
