from connection_pool import connection_pool
import threading
import time

def consume(cp):
    connection = None
    try:
        connection = cp.get_connection()
        print(f"connection {connection} getting used by thread {threading.current_thread()}")
        cp.print_queue_stats()
        time.sleep(1)
    finally:
        cp.release_connection(connection)

def main():
    cp = connection_pool(5)
    cp.print_queue_stats()
    for i in range(100):
        t = threading.Thread(target=consume, args=(cp,))
        t.start()

    print ("Started all threads")

if __name__=="__main__":
    main()