from __future__ import print_function

import argparse


def prevent_edits(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames up for edit')
    parser.add_argument('--blacklist', nargs='*', description='List of full-path filenames to blacklist, e.g. mydir/dir2/test.txt')  # dest=blacklist?
    args = parser.parse_args(argv) # argv.split() ?

    retval = 0

    for filename in args.filenames:
        # Ensure args.blacklist is a list (not a single string that gets pieced apart)
        if filename in args.blacklist:
            print(f'{filename}: blacklisted for edits')
            retval = 1

    return retval


if __name__ == '__main__':
    exit(prevent_edits())
