from .parse import squid_to_gcode

class SquidParse(object):
    """Convert squid files to gcode"""

    def __str__(self):
        return "Convert squid files to gcode"

    def parse(self, filename):
        # TODO: make this into its own function
        
        filename_parts = filename.split('.')
        
        if len(filename_parts) != 2 or filename_parts[1] != 'squid':
            print '{} doesn\'t look like a squid file'.format(filename)
            return

        with open(filename, 'r') as f:
            squid = f.read()

        gcode = squid_to_gcode(squid)

        gcode_filename = '{}.gcode'.format(filename_parts[0])
        with open(gcode_filename, 'w') as f:
            f.write(gcode)
            print 'GCODE written to {}'.format(gcode_filename)
