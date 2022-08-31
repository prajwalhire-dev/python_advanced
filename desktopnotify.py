from email import message
from re import M
import time
from turtle import title
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "ALERT!!",
            message = "Take a break! It has been n hour!",
            timeout = 10
        )
        time.sleep(3600)