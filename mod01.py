import datetime, schedule, time
from schedule import every, repeat


def get_time():
    return datetime.datetime.now()


@repeat(every(10).seconds, 'busta', 'rhymz')
def task(arg1, arg2):
    print("Doing task...", f"args = {arg1, arg2} ", get_time())


# schedule.every(5).seconds.do(task, 10, 'luigi ')

while True:
    schedule.run_pending()
    time.sleep(1)
