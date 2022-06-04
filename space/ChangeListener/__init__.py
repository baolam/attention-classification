from .Observer import Observer

observer = Observer()

from .ClientListener import ClientListener

def emit(**kwargs):
  observer.emit(**kwargs)