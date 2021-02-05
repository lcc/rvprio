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
    "--project": {
        "nullable": False,
        "required": True,
        "type": "string",
    },
    "--input": {
        "nullable": False,
        "required": True,
        "type": "string",
    },
    "--output": {
        "nullable": False,
        "required": True,
        "type": "string",
    },
}
