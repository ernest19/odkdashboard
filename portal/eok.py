import schedule
import time


def job():
    print("print .......")



def code():
    print("print .......")




# schedule.every(5).seconds.do(job)
# schedule.every(10).seconds.do(job)

schedule.every(10).days.at("13:30").do(code)

while True:
    schedule.run_pending()
    time.sleep(1)