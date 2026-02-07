import time
from datetime import datetime
from flask import render_template

schedule : dict = {
    "Midnight Snack":datetime(2026,2,7)
}

def timer(target_time : datetime = schedule['Midnight Snack']) :
    delta = target_time - datetime.now()

    total_seconds = int(delta.total_seconds())

    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    return (f"Time: {hours:02}:{minutes:02}:{seconds:02}")

def countdown_index() :
    return render_template('countdown/countdown.html', temp=timer())