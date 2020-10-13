import fire 
 
# defining a function 
def hello(name): 
    return 'Hello {0}, Have a nice day {0}'.format(name) 
 
if __name__ == '__main__': 
    # converting our function in a Command Line Interface (CLI). 
    fire.Fire() 

# run in cmd: python fire_python.py hello john

"""
By using --help you can know the function's name, whether it's a positional argument, etc.
You can use the --interactive flag on any CLI to enter a Python REPL with all the modules and variables used in the context where fire was called already and available to you for use.
Other useful variables like --, the component, result, and trace of the fire command will also be available."""
# for Help Flag

# python fire_python.py -- --help

# for Interactive Flag

# python fire_python.py hello -- --interactive #opens Interactive console.
