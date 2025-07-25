import psutil
from plyer import notification
import time

LOW_BATTERY_THRESHOLD = 22  # Battery Level
CHECK_INTERVAL = 10  # Check every 10 seconds

alerted = False  

while True:
    battery = psutil.sensors_battery()
    percent = battery.percent
    plugged = battery.power_plugged

    print(f"Battery: {percent}% | Charging: {plugged}")

    if not plugged and percent <= LOW_BATTERY_THRESHOLD:
        if not alerted:
            notification.notify(
                title="Low Battery Alert",
                message=f"Battery is at {percent}%. Please plug in your charger.",
                timeout=15
            )
            alerted = True  # Mark alert as sent
    else:
        alerted = False  # Reset alert once charging or battery is fine

    time.sleep(CHECK_INTERVAL)
