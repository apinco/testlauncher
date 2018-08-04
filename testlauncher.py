import argparse
import configparser
import configparser
from pathlib import Path
import os.path
import sys

def parse_args():
    parser = argparse.ArgumentParser(add_help=False, prog=os.path.basename(__file__))

    # Add script_name as a positional argument
    parser.add_argument("script_name", help="script to run")

    # Create a new groups to differentiate the launcher args from the script args
    # Also, create two groups for the launcher so that you can tell which are optional and
    # which are required (Python, by default, considers all -- parameters as optional so
    # this is a way to make some required)
    required = parser.add_argument_group("Required Launcher Arguments")
    # The store action makes is so that if --help is supplied (no value) then
    # it has the value true.  Otherwise false.  I am adding help here so
    # that I can print the launcher usage and roll the help down to the test
    # script.  This won't work if you use the build in help as it exits.
    required.add_argument("--help", help="Get Help message", action='store_true')
    required.add_argument("--la1", help="first launcher arg", required=True)
    required.add_argument("--la2", help="first launcher arg", required=True)
    required.add_argument("--la3", help="first launcher arg", required=True)

    optional = parser.add_argument_group("Optional Launcher Arguments")
    optional.add_argument("--la4", help="first launcher arg")
    optional.add_argument("--la5", help="first launcher arg")
    optional.add_argument("--la6", help="first launcher arg")

    (la, sa) = parser.parse_known_args()

    if (la.help is True):
        parser.print_help()
        print("\n")
        print("### Script Arguments below ###")
        print("\n")
        # We parsed out the --help already, so add it back into the sa (the script arguments)
        # so that we can get the help for the script as well
        sa.append("--help")
    return (la,sa)

def read_globals():
    home = str(Path.home())
    user_settings = home + "/user_config.ini"

    config_parser = configparser.ConfigParser()
    # Read the global configurations
    config_parser.read("global_config.ini")

    # If there is a team_settings defined as one of the pyuniti settings,
    # read that in (attributes that match with the ones in global_config will
    # override the globals)
    team_settings = config_parser.get('pyuniti', 'team_settings', fallback=None)
    if (team_settings != None):
        print("Reading team settings:")
        config_parser.read(team_settings)
    else:
        print("Found no team config settings:")

    return config_parser

### Start of Main ###

# Parse all arguments to the launcher.
#   la are the launcher arguments
#   sa are the script arguments that need to be passed down to the script
(la, sa) = parse_args()

# Create a module object dynamically using the name provided to argparse
# and call the function runit
script = __import__(la.script_name)
# Pass in sa which is all of the script arguments
# and pass in globals where are the files read from
# the .ini files
script.runit(args=sa,globals=globals)




