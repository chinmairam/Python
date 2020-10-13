import fire

def hello(name): 
    return 'Hello how are you {}'.format(name) 
 
def nice(name): 
    return 'nice day thank you! {}'.format(name) 
 
def bye(name): 
    return 'bye take care! {}'.format(name)

# converting our function in a Command Line Interface (CLI). 
if __name__ == '__main__': 
    fire.Fire({ 
        'hello' : hello, 
        'nice': nice, 
        'bye' : bye 
    })

#python fire_python4.py hello sachin 
#python fire_python4.py nice sachin 
#python fire_python4.py bye sachin 


"""By using a dictionary,
you can selectively expose the functions to the command line."""
