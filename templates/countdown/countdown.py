import time
from datetime import datetime, timedelta
from flask import render_template

schedule : dict = {
    "Midnight Snack":datetime(2026,2,7)
}

def timer(target_time : datetime = schedule['Midnight Snack']) :
    delta : timedelta = target_time - datetime.now()

    total_seconds : int = int(delta.total_seconds())

    hours : int = total_seconds // 3600
    minutes : int = (total_seconds % 3600) // 60
    seconds : int = total_seconds % 60

    return (f"Time: {hours:02}:{minutes:02}:{seconds:02}")

def countdown_index() :
    return render_template('countdown/countdown.html', temp=timer())