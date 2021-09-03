'''Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

'''

def make_readable(seconds):
    # Do something
    hours = seconds//3600
    bal = seconds % 3600
    if hours > 99:
        hours = 99
        bal = seconds - (99*3600)
        minutes = bal//60
        if minutes > 59:
            minutes = 59
            bal = bal - (59*60)
            seconds = bal
            if seconds > 59:
                seconds = 59
        else:
            seconds = bal % 60
    else:
        minutes = bal // 60
        bal = bal % 60
        if minutes > 59:
            bal = minutes - 59
            seconds = bal * 60
            if seconds > 59:
                seconds = 59
        else:
            seconds =  bal
    
    return("%02d:%02d:%02d" % (hours,minutes,seconds))

make_readable(0)
make_readable(5)
make_readable(60)
make_readable(86399)
make_readable(359999)