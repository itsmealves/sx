import sys
import argparse
import importlib


parser = argparse.ArgumentParser()

action_parsers = parser.add_subparsers(dest='action')
boot_parser = action_parsers.add_parser('boot', help='Manage sx-based applications')
boot_parser.add_argument('-s', '--settings', default='application.toml')

create_parser = action_parsers.add_parser('create', help='Create a new sx-based application')

boot_action_parsers = boot_parser.add_subparsers(dest='boot_action')
build_command = boot_action_parsers.add_parser('build', help='Builds application packages')

start_command = boot_action_parsers.add_parser('start', help='Run packages')
start_command.add_argument('-p', '--packages', nargs='+', default=None,
							help='Selects which packages should boot run (default: all packages)')

create_parser.add_argument('name', help='Determine application name')


def main():
	args = parser.parse_args()
	if args.action is None:
		parser.print_help()
		sys.exit()

	package = 'sx.actions.{}'
	action = importlib.import_module(package.format(args.action))
	action.run(args)