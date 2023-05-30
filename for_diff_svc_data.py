import glob
import os
import logging
import librosa
import soundfile as sf

logging.basicConfig(format='%(asctime)s: %(message)s', level=logging.INFO, datefmt='%x %a %X')

pitches = [-0.5, 0.5]  # 피치 변경 값

def shift_pitch(path):
    directory = os.path.abspath(path)
    fname = os.path.basename(path)
    loc, ext = os.path.splitext(fname)

    logging.info(f'Loading {fname}')
    x, sr = librosa.load(directory, sr=None)

    logging.info(f'Analyzing {fname}')
    for i in pitches:
        if i == 0:
            continue
        logging.info(f'Shifting pitch of {fname} by {i} semitones')
        y = librosa.effects.pitch_shift(x, sr=sr, n_steps=i)

        shifted_fname = f'{loc}_{i:+}{ext}'
        sf.write(shifted_fname, y, sr, format='WAV')
        logging.info(f'Saved {shifted_fname}')

if __name__ == '__main__':
    logging.info('Starting pitch shifting')
    for mp3_file in glob.glob('*.mp3'):
        shift_pitch(mp3_file)
