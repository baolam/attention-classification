from space import ClientListener
from space import end_changging_listener
from space import observer

myname = ClientListener()

def hello(**kwargs):
  print("Hello world")
  
ClientListener.add_listener(myname)

myname.on("hello_world", hello)
myname.emit(name="hello_world")

end_changging_listener()