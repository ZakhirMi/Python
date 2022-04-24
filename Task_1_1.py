
duration = 7481
day = 86400
hour = 3600
minute = 60
sec = 1

if duration >= day:
    day1 = duration // day
    hour1 = (duration-day*day1) // hour
    minute1 = (duration-day*day1-hour*hour1) // minute
    sec1 = (duration-day*day1-hour*hour1-minute*minute1) // sec
    print(day1, "дн", hour1, "час", minute1, "мин", sec1, "сек")
elif duration >= hour:
    hour2 = duration // hour
    minute2 = (duration-hour*hour2) // minute
    sec2 = (duration-hour*hour2-minute*minute2) // sec
    print(hour2, "час", minute2, "мин", sec2, "сек")
elif duration >= minute:
    minute3 = duration // minute
    sec3 = duration % minute
    print(minute3, "мин", sec3, "сек")
else: print(duration, "сек")


