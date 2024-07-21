
import threading
import math

lock = threading.Lock()
shared_variable = 2


def thread_function(name):
    global shared_variable
    i = 0
    with lock:
        while i < 5:
            if validate_prime(shared_variable):
                print(f"Thread {name}: prime number = {shared_variable}")
                i += 1
            shared_variable += 1


def validate_prime(shared_variable):
    prime_flag = 0
    for i in range(2, int(math.sqrt(shared_variable)) + 1):
        if shared_variable % i == 0:
            prime_flag = 1
            break
    if prime_flag == 0:
        return True
    return False


def main():
    threads = []
    for i in range(4):
        thread = threading.Thread(
            target=thread_function,
            args=(str(i),)
        )
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Final value of prime number: "
          f"{shared_variable}")


if __name__ == "__main__":
    main()
