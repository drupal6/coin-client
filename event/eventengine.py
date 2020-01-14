from typing import Any, Callable
from queue import Empty, Queue
from threading import Thread
from collections import defaultdict
import time

EVENT_TIMER = "eTimer"


class Event:
    def __init__(self, _type: str, data: Any = None):
        self.type = _type
        self.data = data


HandlerType = Callable[[Event], None]


class EventEngine:
    def __init__(self, interval: int = 1):
        self._interval = interval
        self._queue = Queue()
        self._active = False
        self._thread = Thread(target=self._run())
        self._timer = Thread(target=self._run_timer())
        self._handlers = defaultdict(list)
        self._general_handlers = []

    def _run(self):
        while self._active:
            try:
                event = self._queue.get(block=True, timeout=1)
                self._process(event)
            except Empty:
                pass

    def _process(self, event: Event):
        if event in self._handlers:
            [handler(event) for handler in self._handlers[event.type]]
        if event in self._general_handlers:
            [handler(event) for handler in self._general_handlers]

    def _run_timer(self):
        while self._active:
            time.sleep(self._interval)
            event = Event(EVENT_TIMER)
            self._process(event)

    def start(self):
        self._active = True
        self._thread.start()
        self._timer.start()

    def stop(self):
        self._active = False
        self._thread.join()
        self._timer.join()

    def put(self, event:Event):
        self._queue.put(event)

    def register(self, _type: str, handler: HandlerType):
        handler_list = self._handlers[_type]
        if handler not in handler_list:
            handler_list.append(handler)

    def unregister(self, _type: str, handler: HandlerType):
        handler_list = self._handlers[_type]
        if handler in handler_list:
            handler_list.remove(handler)

        if not  handler_list:
            self._handlers.pop(_type)

    def register_general(self, handler: HandlerType):
        if handler not in self._general_handlers:
            self._general_handlers.append(handler)

    def unregister_general(self, handler:HandlerType):
        if handler in self._general_handlers:
            self._general_handlers.pop(handler)


