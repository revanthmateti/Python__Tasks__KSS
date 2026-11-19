import time


def calculate_time(func):

    def wrapper():
        start = time.time()

        func()

        end = time.time()

        print("Execution Time:", end - start)

    return wrapper


@calculate_time
def display():
    time.sleep(2)
    print("Program Completed")


display()
