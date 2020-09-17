def is_comment(item):
    return isinstance(item, str) and item.startswith("#")

def execute(program):
    """Executes a stack program."""
    # Find the start of the 'program' by skipping
    # any item which is a comment
    while program:
        item = program.pop()
        if not is_comment(item):
            program.append(item)
            break
    else: # nobreak
        # executes when there is no non-comment item
        print("Empty program!")
        return

    # Evaluate the program
    pending = []
    while program:
        item = program.pop()
        if callable(item):
            try:
                result = item(*pending)
            except Exception as e:
                print("Error: ", e)
                break
            program.append(result)
            pending.clear()
        else:
            pending.append(item)
            # If popped item is not callable
    else: # nobreak
        print("Program successful.")
        print("Result: :", pending)

    print("Finished")
        

if __name__ == '__main__':
    import operator

    # Top of stack is end of list.So,to get in right order,we use reversed.
    
    program = list(reversed((
        "# A short stack program to add",
        "# and multiply some constants",
        5,
        2,
        operator.add,
        3,
        operator.mul)))
    execute(program)
    
