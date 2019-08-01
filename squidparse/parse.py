from commands import known_commands
from util import flatten


def command_to_gcode(cmd):
    cmd_list = cmd.split(' ')
    cmd_main = cmd_list[0]

    if cmd_main in known_commands:
        return known_commands[cmd_main](*cmd_list[1:])
    return cmd

def commands_to_gcode(cmds):
    return [command_to_gcode(c) for c in cmds]

def squid_to_gcode(squid_file):
    squid_commands = squid_file.split('\n')
    gcode_commands = commands_to_gcode(squid_commands)
    headers = ['M83', 'G90']
    return flatten(headers + gcode_commands)
