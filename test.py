import threading

def cb_func():
    "The callback function."
    print 'Callback, in thread %s' % threading.current_thread().name

def th_func(callback):
    "The threaded function."
    # ...
    callback()

thr = threading.Thread(target=th_func, args=(cb_func,)).start()
