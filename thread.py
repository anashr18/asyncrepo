import os 
import threading

print(f'python process running with id {os.getpid()}')

print(f'Thread count is {threading.activeCount()} and current thread is {threading.current_thread().name}')

def hello_from_thread():
    print(f'hello from thread {threading.current_thread()}')

hello_thread = threading.Thread(target=hello_from_thread)
hello_thread.start()


print(f'active thread {threading.current_thread()} and the count of thread is {threading.active_count()}')
hello_thread.join()