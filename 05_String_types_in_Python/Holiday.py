#!/usr/bin/python

import argparse
import os


def argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', help='Path for files')
    parser.add_argument('text', type=str, help='Find text', nargs='*')
    return parser.parse_args()


def find_text(file, text):
    words = ' '.join(text)
    count = 0
    for fil in file:
        if fil[0] != '.' and os.path.isfile(fil):
            with open(fil, 'r') as myFile:
                print('Open this file -> {}'.format(fil))
                for num, line in enumerate(myFile, 1):
                    if words in line and count < 100:
                        count += 1
                        print('Found at line: {} -> {}Number in count -> {}\n'.format(num, line, count))
        else:
            continue
        print('---------------------------------------------------------------\n'
              '---------------------------------------------------------------')


def get_files(directory, texts):
    if directory is None:
        directory = os.getcwd()
    files = os.listdir(directory)
    find_text(files, texts)


args = argument_parser()
get_files(args.path, args.text)
