




from apscheduler.schedulers.background import BackgroundScheduler



# https://www.reddit.com/r/flask/comments/49vqb2/af_flask_paramiko_apscheduler_working_outside_of/
def sched():
    sched = BackgroundScheduler()
    sched.add_job(update_printer, 'interval', seconds=30)
    sched.start()



def update_printer():
    print "hello world"
