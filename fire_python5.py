import fire 
 
class World(object): 
    def hello(self,name): 
        return 'Hello how are you {}'.format(name) 
 
    def nice(self,name): 
        return 'nice day thank you! {}'.format(name) 
 
    def bye(self,name): 
        return 'bye take care! {}'.format(name) 
 
# converting our function in a Command Line Interface (CLI). 
if __name__ == '__main__': 
    world_instance = World() 
    fire.Fire(world_instance)

#python fire_python5.py hello sachin 
#python fire_python5.py nice sachin 
#python fire_python5.py bye sachin 


# or

# converting our function in a Command Line Interface (CLI). 
#if __name__ == '__main__': 
#    fire.Fire(World) 
