from Queue.queue import Queue


def option_enqueue(queue, item):
    queue.enqueue(item)


def option_dequeue(queue):
    print(queue.dequeue())


def option_peek(queue):
    print(queue.peek())


def option_exit(queue):
    del queue
    print("THANK YOU !!! HAVE A GREAT DAY !!!")
    quit(1)


def option_size(stack):
    print(stack.size())


if __name__ == '__main__':
    user_input = "y"
    queue = Queue()
    print("~" * 10, "STACK", "~" * 10)
    print("Enter p to DEQUEUE, s for SIZE, v to VIEW TOP, q to QUIT")
    while user_input != "0":
        try:
            user_input = input("Enter item to ENQUEUE >>> ")
            if user_input == "p":
                option_dequeue(queue)
            elif user_input == "s":
                option_size(queue)
            elif user_input == "v":
                option_peek(queue)
            elif user_input == "q":
                option_exit(queue)
            else:
                option_enqueue(queue, user_input)
        except EOFError or KeyboardInterrupt:
            option_exit(queue)
        except KeyError:
            print("Please enter valid option.")
