""" Validates the command line arguments. """

CLI_SCHEMA = {
    "--help": {
        "nullable": False,
        "required": True,
        "type": "boolean",
    },
    "--kernel": {
        "nullable": False,
        "required": True,
        "type": "string",
        "allowed": ["javamop"],
    },
    "--input": {
        "nullable": True,
        "required": False,
        "type": "string",
    },
}
