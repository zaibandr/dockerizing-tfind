import threading
from update_info import update_one


def writer(event_for_wait, event_for_set):
    while True:
        event_for_wait.wait()  # wait for event
        event_for_wait.clear()  # clean event for future
        update_one()
        event_for_set.set()  # set event for neighbor thread

# init events
e1 = threading.Event()
e2 = threading.Event()
e3 = threading.Event()
e4 = threading.Event()
e5 = threading.Event()


# init threads
t1 = threading.Thread(target=writer, args=(e1, e2))
t2 = threading.Thread(target=writer, args=(e2, e3))
t3 = threading.Thread(target=writer, args=(e3, e4))
t4 = threading.Thread(target=writer, args=(e4, e5))
t5 = threading.Thread(target=writer, args=(e5, e1))

# start threads
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

e1.set()  # initiate the first event

# join threads to the main thread
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
