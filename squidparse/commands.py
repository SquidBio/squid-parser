from const import thing_locations
from util import flatten


def home():
    commands = ['G28 X Y', 'G28 Z']
    return flatten(commands)

def push():
    commands = ['G1 E45 F3600']
    return flatten(commands)

def pull():
    commands = ['G1 E-45 F3600']
    return flatten(commands)

def lower(height=40):
    commands = ['G1 Z{} F3600'.format(height)]
    return flatten(commands)

def lift(height=98):
    commands = ['G1 Z{} F3600'.format(height)]
    return flatten(commands)

def goto(thing):
    if thing not in thing_locations:
        raise(Exception('I don\'t know where {} is'.format(thing)))
    location = thing_locations[thing]
    commands = ['G1 X{} Y{} F3600'.format(location['X'], location['Y'])]
    return flatten(commands)

def get(thing):
    commands = [lift(50), goto(thing), lower(), lift(43), lower(), lift()]
    return flatten(commands)

def detip():
    commands = [lift(), goto('tipstop'), lift(109), lift()]
    return flatten(commands)

known_commands = {
    'home': home,
    'push': push,
    'pull': pull,
    'lower': lower,
    'raise': lift,
    'goto': goto,
    'get' : get,
    'detip': detip
}
