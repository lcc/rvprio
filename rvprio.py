"""
Runtime Verification Priorizator
Usage: rvprio [options]

  -h --help         Show this screen.
  -k --kernel=rv    Violations to look for [default: javamop]
"""
import docopt


def main(kernel):
    """ Main function for rvprio. """
    pass


if __name__ == "__main__":
    arguments = docopt.docopt(__doc__, version="beta")
    cli_validator = cerberus.Validator(rvprio.validator.CLI_SCHEMA)
    is_valid = cli_validator.validate(arguments)
    if is_valid:
        arguments = {k.strip("--"): v for (k, v) in arguments.items()}
        main(**arguments)
