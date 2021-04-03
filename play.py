from keras.models import load_model
import cv2
import numpy as np
from random import choice
import serial

REV_CLASS_MAP = {
    0: "rock",
    1: "paper",
    2: "scissors",
    3: "none"
}


def mapper(val):
    return REV_CLASS_MAP[val]





model = load_model("rock-paper-scissors-model.h5")

s1 = serial.Serial('COM60',57600)
cap = cv2.VideoCapture(0)

prev_move = None
computer_move_name = None

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    # rectangle for user to play
    cv2.rectangle(frame, (100, 100), (500, 500), (255, 255, 255), 2)
    # rectangle for computer to play
    cv2.rectangle(frame, (800, 100), (1200, 500), (255, 255, 255), 2)

    # extract the region of image within the user rectangle
    roi = frame[100:500, 100:500]
    img = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (227, 227))

    # predict the move made
    pred = model.predict(np.array([img]))
    move_code = np.argmax(pred[0])
    user_move_name = mapper(move_code)

    # predict the winner (human vs computer)
    if user_move_name != None:
        if user_move_name == "rock":
            computer_move_name = "paper"
            s1.write('p'.encode())
        if user_move_name == "paper":
            computer_move_name = "scissors"
            s1.write('s'.encode())
        if user_move_name == "scissors":
            computer_move_name = "rock"
            s1.write('r'.encode())

    # display the information
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, "Your Move: " + user_move_name,
                (50, 50), font, 1.2, (255, 255, 255), 2, cv2.LINE_AA)


    if computer_move_name != "none":
        #icon = cv2.imread(
        #    "images/{}.png".format(computer_move_name))
        #icon = cv2.resize(icon, (400, 400))
        #frame[100:500, 800:1200] = icon
        #cv2.imshow("computer",icon)
        print (computer_move_name)
        
    cv2.imshow("Rock Paper Scissors", frame)

    k = cv2.waitKey(10)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
