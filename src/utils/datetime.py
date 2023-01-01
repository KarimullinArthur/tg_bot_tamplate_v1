import datetime


def get_datetime(object=False, only_time=False):
    timestamp = datetime.datetime.utcnow()

    if only_time:
        return str(timestamp.strftime("%H:%M"))

    elif not only_time:
        return str(timestamp).split('.')[0]

    if object:
        return timestamp
