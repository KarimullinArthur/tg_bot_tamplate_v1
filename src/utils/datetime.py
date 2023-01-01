import datetime


def get_datetime():
    timestamp = str(datetime.datetime.now()).split('.')[0]
    return timestamp
