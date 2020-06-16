from Stack.stack import Stack


def option_push(stack, item):
    stack.push(item)


def option_pop(stack):
    print(stack.pop())


def option_peek(stack):
    print(stack.peek())


def option_exit(stack):
    del stack
    print("THANK YOU !!! HAVE A GREAT DAY !!!")
    quit(1)


def option_size(stack):
    print(stack.size())


if __name__ == '__main__':
    user_input = "y"
    stack = Stack()
    print("~" * 10, "STACK", "~" * 10)
    print("Enter p to POP, s for SIZE, v to VIEW TOP, q to QUIT")
    while user_input != "0":
        try:
            user_input = input("Enter item to store >>> ")
            if user_input == "p":
                option_pop(stack)
            elif user_input == "s":
                option_size(stack)
            elif user_input == "v":
                option_peek(stack)
            elif user_input == "q":
                option_exit(stack)
            else:
                option_push(stack, user_input)
        except EOFError or KeyboardInterrupt:
            option_exit(stack)
        except KeyError:
            print("Please enter valid option.")
