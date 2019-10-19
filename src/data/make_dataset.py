# -*- coding: utf-8 -*-
# import click
# import logging
# from pathlib import Path
# from dotenv import find_dotenv, load_dotenv
from tqdm import tqdm
import sys
import os

sys.path.append('../helpers')
import audio_convert as ac


def convert_audio():
    for item in ['test', 'train', 'validate']:
        ori = '/'.join(['../../data/raw/transcripts/recordings', item])
        for filename in tqdm(os.listdir(ori)):
            y = ac.load_raw("/".join([ori,filename]))

            dest = '/'.join(['../../data/processed', item, filename])
            ac.write_wav(dest, y)
    return


convert_audio()
