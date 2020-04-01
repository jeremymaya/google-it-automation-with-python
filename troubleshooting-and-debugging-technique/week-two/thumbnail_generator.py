#!/usr/bin/env python3

from concurrent import futures

import argparse
import logging
import os
import sys

import PIL
import PIL.Image

from tqdm import tqdm

def process_options():
    kwargs = {
        'format': '[%(levelname)s] %(message)s'
    }

    parser = argparse.ArgumentParser(
        description="Thumbnail generator",
        fromfile_prefix_chars='@'
    )
    parser.add_argument('--debug', action='store_true')
    parser.add_argument('-v', '--verbose', action='store_true')

def progress_bar(files):
    return tqdm(files, desc='Processing', total=len(files), dynamic_ncols=True)

def main():

    process_options()

    # Create the thumbnail directory
    if not os.path.exists('thumbnails'):
        os.mkdir('thumbnails')

    excutor = futures.ThreadPoolExecutor()
    for root, _, files in os.walk('images'):
        for basename in progress_bar(files):
            if not basename.endswith('.jpg'):
                continue
            excutor.submit(process_file, root, basename)
    print('Waiting for all threads to finish.')
    excutor.shutdown()
    return 0

if __name__ == "__main__":
    sys.exit(main())