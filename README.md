# esi_maker
 
This is a python module to make, load and unzip esi files.

ESI is a lightweight sound source file format that stores a folder of audio files into a single binary file, together with a setting file, where you can customize the mappings betweeen note names and audio file names.

ESI file stores the uncompressed data of each audio file in the folder you specify, and the information to unzip the audio files and the setting file.

ESI stands for `Easy Sampler Instrument`, which is used in [Easy Sampler](https://github.com/Rainbow-Dreamer/easy-sampler) as an audio samples sound source file format, together with SoundFonts and audio files.

For more details about ESI format, you can refer to the musicpy sampler module's wiki, [click here](https://github.com/Rainbow-Dreamer/musicpy/wiki/musicpy-sampler-module#more-about-esi-sound-module-format)

## Installation

## Usage
There are 3 functions in this python module, `make_esi`, `load_esi` and `unzip_esi`.
