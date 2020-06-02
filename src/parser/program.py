from .recognizer import RecoRegexRule, RecoCustomRule


RULES = [
    # ("ARGUMENT", ""),  # key=value ignored in the meantime for simplicity.
    # ("HELP_FLAG", "-h"),
    # ("HELP_DOUBLE_FLAG", "--help"),
    # ("ARGS_FLAG", "-a"),
    # ("ARGS_DOUBLE_FLAG", "--args"),
    # ("VERBOSE_FLAG", "-v"),
    # ("VERBOSE_DOUBLE_FLAG", "--verbose"),
    # ("ARG_KEY", ""),  # -key
    RecoRegexRule("PATH", r'[\w\/"\s\.]+\.py'),
    RecoRegexRule("FLAG", r"-[a-zA-Z_]+[a-zA-Z0-9]*"),
    RecoRegexRule("DOUBLE_FLAG", r"--[a-zA-Z_]+[a-zA-Z0-9]*"),
    RecoRegexRule(
        "NUMERIC",
        r"[+-]?(?:\d+(?:[eE][+-]?\d+)|(?:\d+\.\d*|\.\d+)(?:[eE][+-]?\d+)?)|[+-]?\d+",
    ),
    RecoRegexRule("BOOLEAN", r"True|False"),
    RecoRegexRule("IDENTIFIER", r"[a-zA-Z_]+[a-zA-Z0-9]*"),
    RecoRegexRule("STRING", r"[\s\S]*"),
]
