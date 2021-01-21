import time
from plyer import notification
if __name__ == "__main__":
    while True:
        notification.notify(
            title="***Please Drink Water.***",
            message = "If you don't drink water, You will lose your kidney . . But If you drink water , your energy level will boost up .",
            app_icon = "F:\Project\Drinking_Water_Notification\icon.ico",
            timeout =10
        )
        time.sleep(60*60) 