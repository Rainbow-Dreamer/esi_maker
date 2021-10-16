# esi_maker
 
This is a python module to make, load and unzip esi files.

ESI is a lightweight sound source file format that stores a folder of audio files into a single binary file, together with a setting file, where you can customize the mappings betweeen note names and audio file names.

ESI file stores the uncompressed data of each audio file in the folder you specify, and the information to unzip the audio files with their original file names and data and the setting file.

ESI stands for `Easy Sampler Instrument`, which is used in [Easy Sampler](https://github.com/Rainbow-Dreamer/easy-sampler) as an audio samples sound source file format, together with SoundFonts and audio files.

For more details about ESI format, you can refer to the musicpy sampler module's wiki, [click here](https://github.com/Rainbow-Dreamer/musicpy/wiki/musicpy-sampler-module#more-about-esi-sound-module-format)

## Installation
Download the source codes and then run `python setup.py install` in cmd/terminal in the source codes folder.

## Importing
```python
import esi_maker as es
```

## Usage
There are 3 functions in this python module, `make_esi`, `load_esi` and `unzip_esi`.
```python
make_esi(file_path,
         name='untitled',
         settings=None,
         info=None,
         asfile=True)

# file_path: the directory of folder than contains all of the audio files you want to include in the esi file

# name: the name of the esi file

# settings: the settings of the esi file, could be a string or a file path of a text file

# info: other information you want to include in the esi file, author information for example

# asfile: if set to True, then read settings as a file path of a text file, otherwise read as a string

# this function will make an esi file at the path that the parameter `name` specified, the file extension of the esi file is esi


load_esi(file_path, convert=True)

# file_path: the file path of the esi file you want to load

# convert: if set to True, the audio files in the esi file will be converted to pydub AudioSegment instances from binary data


unzip_esi(file_path, folder_name=None)

# file_path: the file path of the esi file you want to unzip the audio files

# folder_name: the path of the folder you want to unzip the audio files to
```
