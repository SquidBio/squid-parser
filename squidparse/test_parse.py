from parse import squid_to_gcode


def test_parse():
    with open('test_files/coffee.gcode', 'r') as f:
        test_file_gcode = f.read()
    with open('test_files/coffee.squid', 'r') as f:
        test_file_squid = f.read()
    rendered_gcode = squid_to_gcode(test_file_squid)
    assert rendered_gcode == test_file_gcode
