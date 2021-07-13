import queue
import threading

class connection_pool:

    def __init__(self, no_of_connections):
        self.queue = []
        self.no_of_connections = no_of_connections
        self.lock = threading.Lock()
        self.conditionFull = threading.Condition(self.lock)
        self.conditionEmpty = threading.Condition(self.lock)
        for i in range(no_of_connections):
            self.queue.append(i)

    def get_connection(self):
        try:
            self.lock.acquire()
            while(len(self.queue) == 0):
                self.conditionEmpty.wait()
            connection = self.queue.pop(0)
            self.conditionFull.notify_all()
        finally:
            self.lock.release()
        return connection

    def release_connection(self, connection):
        try:
            self.lock.acquire()
            while(len(self.queue) == self.no_of_connections):
                self.conditionFull.wait()
            self.queue.append(connection)
            self.conditionEmpty.notify_all()
        finally:
            self.lock.release()

    def print_queue_stats(self):
        print(len(self.queue))