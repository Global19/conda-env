from argparse import RawDescriptionHelpFormatter

from conda.cli import common

from . import helpers

ENTRY_POINTS = helpers.generate_entry_points(__name__)

description = """
List the Conda environments
"""

example = """
examples:
    conda env list
    conda env list --json
"""


def configure_parser(sub_parsers):
    l = sub_parsers.add_parser(
        'list',
        formatter_class=RawDescriptionHelpFormatter,
        description=description,
        help=description,
        epilog=example,
    )

    common.add_parser_json(l)

    l.set_defaults(func=execute)


@helpers.enable_entry_point_override(ENTRY_POINTS["execute"])
def execute(args, parser):
    info_dict = {'envs': []}
    common.handle_envs_list(info_dict['envs'], not args.json)

    if args.json:
        common.stdout_json(info_dict)
