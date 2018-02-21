import balloon
import random
import datetime
import time


def time_stamp():
    today = datetime.datetime.now().strftime("%d-%m-%Y")
    return today


def write_todo_list(things):
    if things == "DONE":
        push_me()
    else:
        today = time_stamp()
        f = open("TODO.txt", "a")
        f.write("[" + today + "]\t" + things.ljust(20) + "\t not done"+"\n")
        f.close()
        return True


def slice_it(my_line):
    text = my_line.split('\t')
    return text[1]


def getme():
    lines = open('TODO.txt').read().splitlines()
    myline = random.choice(lines)

    return myline


def ask_and_write(things):
    if write_todo_list(things) is not True:
        return
        #push_me()


def send_message():
    while True:
        things = raw_input("Things TODO :").upper()
        ask_and_write(things)


def push_me():
    while True:
        my_line = getme()
        push = slice_it(my_line)
        print push
        text = str(push)
        balloon.balloon_tip("Did you do", text)
        time.sleep(10)


send_message()
#push_me()


