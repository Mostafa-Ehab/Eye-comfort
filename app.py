from plyer import notification
import time
import screen_brightness_control as sbc


# 20 minutes = 1200 seconds

def main():
    # Start the first notification
    notification.notify(
        title='Started',
        message='Eye comforter has benn started',
        app_name='Eye Comfort'
    )
    time.sleep(1)
    while True:
        try:
            # Wait 20 minutes before sending a notification {Feel free to chnage it}
            time.sleep(1200)
            # Getting the old value for the brightness
            old = sbc.get_brightness()
            # Decreasing the brightness to half its original value
            sbc.set_brightness(old/2)
            print("!!")
            # Display the notification
            notification.notify(
                title='Take a break',
                message='Look away from the monitor for 20 seconds',
                app_name='Eye Comfort'
            )
            # Wait for 20 seconds before setting the brightness to its original value
            time.sleep(20)
            sbc.set_brightness(old)
            print("!")
            notification.notify(
                title='Take a break',
                message='Look away from the monitor for 20 seconds',
                app_name='Eye Comfort'
            )
        except KeyboardInterrupt:
            print("Closed")
            break


if __name__ == '__main__':
    main()
