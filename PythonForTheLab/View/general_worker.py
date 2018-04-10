"""
Worker Thread
=============
A Worker Thread is a simple class that re-implements QThread in order to perform a task in a
separate thread.
This is a very simple example, that could be further expanded, but it is more than enough if it is aimed at
working with methods from an Experiment class. The only requisite of QThreads is to reimplement the ``run``
method.
This may not be the correct way of doing things, as pointed out in this `blog post
<https://mayaposch.wordpress.com/2011/11/01/how-to-really-truly-use-qthreads-the-full-explanation/>`_
"""

from PyQt5 import QtCore


class WorkThread(QtCore.QThread):
    def __init__(self,  function, *args, **kwargs):
        super().__init__()
        self.function = function
        self.args = args
        self.kwargs = kwargs

    # def __del__(self):
    #     self.wait()

    def run(self):
        self.function(*self.args,**self.kwargs)
        return


if __name__ == '__main__':
    from time import sleep

    def print_numbers(n=10):
        for i in range(n):
            sleep(0.1)
            print(i)

    worker_thread = WorkThread(print_numbers, 20)
    worker_thread.finished.connect(worker_thread.deleteLater)
    worker_thread.start()
    sleep(1)
    print('Starting')