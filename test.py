import time
from apscheduler.schedulers.blocking import BlockingScheduler
def test():
    print(time.strftime('%Y-%m-%d %X'))
    1/0


if __name__ == '__main__':
    # 定时任务
    scheduler = BlockingScheduler()
    # 22点开始执行，每3秒执行一次
    scheduler.add_job(test,'cron',hour=22,minute=7,second=0)
    try:
        scheduler.start()
    except BaseException:
        scheduler.shutdown()