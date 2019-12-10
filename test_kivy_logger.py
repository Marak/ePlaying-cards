import kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
import logging
import _thread as thread
import time

def my_thread(log):

    for i in range(2**20):
        time.sleep(1)
        log.info("WOO %s", i)

class MyLabelHandler(logging.Handler):

    def __init__(self, label, level=logging.NOTSET):
        logging.Handler.__init__(self, level=level)
        self.label = label

    def emit(self, record):
        "using the Clock module for thread safety with kivy's main loop"
        def f(dt=None):
            self.label.text = self.format(record) #"use += to append..."
        Clock.schedule_once(f)


class MyApp(App):
    def build(self):
        label = Label(text="showing the log here")

        log = logging.getLogger("my.logger")
        log.level = logging.DEBUG
        log.addHandler(MyLabelHandler(label, logging.DEBUG))

        thread.start_new(my_thread, (log,))

        return label


if __name__ == '__main__':
    MyApp().run()
