import sys

def main():
    program_name = sys.argv[0]
    arguments = sys.argv[1:]

    # The program expects exactly two arguments
    # Note that you could choose to accept more than two numbers, and add all of them together
    if len(arguments) != 2:
        print(f"Usage: python {program_name} <number1> <number2>")
        sys.exit(1)

    # Arguments are passed as strings, we need to convert them to integers
    a = int(arguments[0])
    b = int(arguments[1])
    result = a + b

    print("Result: {}".format(result))

if __name__ == "__main__":    
    main()