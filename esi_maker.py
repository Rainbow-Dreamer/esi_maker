import os
import sys
from ast import literal_eval
from io import BytesIO
import pickle
from pydub import AudioSegment
from pydub.playback import _play_with_simpleaudio as play_sound
# ESI file is Easy Sampler Instrument, an ESI file combines a folder of audio files (samples)
# and a settings file (not necessary) into one file, and can be loaded in Easy Sampler or to
# unzip as a folder of sound files and a settings file.
# It can also be loaded as a python object, which is an instance of class esi.
with open('settings.py', encoding='utf-8-sig') as f:
    exec(f.read())


class esi:
    def __init__(self,
                 samples,
                 settings=None,
                 info=None,
                 others=None,
                 name_dict=None):
        self.samples = samples
        self.settings = settings
        self.info = info
        self.others = others
        self.name_dict = name_dict


def make_esi(file_path,
             name='untitled',
             settings=None,
             info=None,
             others=None,
             asfile=True):
    abs_path = os.getcwd()
    filenames = os.listdir(file_path)
    current_samples = {}
    current_settings = None
    if settings is not None:
        if asfile:
            with open(settings, encoding='utf-8-sig') as f:
                current_settings = f.read()
        else:
            current_settings = settings

    if not filenames:
        print('There are no sound files to make ESI files')
        return
    os.chdir(file_path)
    for t in filenames:
        with open(t, 'rb') as f:
            current_samples[t] = f.read()
    current_esi = esi(current_samples, current_settings, info, others)
    os.chdir(abs_path)
    with open(f'{name}.esi', 'wb') as f:
        pickle.dump(current_esi, f)
    print(f'Successfully made ESI file: {name}.esi')


def unzip_esi(file_path, folder_name=None):
    if folder_name is None:
        folder_name = os.path.basename(file_path)
        folder_name = folder_name[:folder_name.rfind('.')]
    if folder_name not in os.listdir():
        os.mkdir(folder_name)
    current_esi = load_esi(file_path, convert=False)
    os.chdir(folder_name)
    for each in current_esi.samples:
        print(f'Currently unzip file {each}')
        with open(each, 'wb') as f:
            f.write(current_esi.samples[each])
    print(f'Unzip {os.path.basename(file_path)} successfully')


def load_esi(file_path, convert=True):
    with open(file_path, 'rb') as file:
        current_esi = pickle.load(file)
    current_samples = current_esi.samples
    name_dict = {os.path.splitext(i)[0]: i for i in current_samples}
    current_esi.name_dict = name_dict
    if convert:
        sound_files = {
            os.path.splitext(i)[0]:
            AudioSegment.from_file(BytesIO(current_samples[i]),
                                   format=os.path.splitext(i)[1][1:])
            for i in current_samples
        }
        current_esi.samples = sound_files
    return current_esi
