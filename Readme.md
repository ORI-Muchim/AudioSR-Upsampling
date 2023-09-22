# AudioSR: Versatile Audio Super-resolution at Scale

[![arXiv](https://img.shields.io/badge/arXiv-2309.07314-brightgreen.svg?style=flat-square)](https://arxiv.org/abs/2309.07314)  [![githubio](https://img.shields.io/badge/GitHub.io-Audio_Samples-blue?logo=Github&style=flat-square)](https://audioldm.github.io/audiosr)

Pass your audio in, AudioSR will make it high fidelity! 

Work on all types of audio (e.g., music, speech, dog, raining, ...) & all sampling rates.

[Original Repo](https://github.com/haoheliu/versatile_audio_super_resolution)

---

## Table of Contents 
- [Installation](#installation)
- [Prepare_Datasets](#prepare_datasets)
- [Usage](#usage)

---

## Installation 
1. **Create an Anaconda environment:**

```sh
conda create -n audiosr python=3.9
```

2. **Activate the environment:**

```sh
conda activate audiosr
```

3. **Clone this repository to your local machine:**

```sh
git clone https://github.com/ORI-Muchim/audiosr_upsampling.git
```

4. **Navigate to the cloned directory:**

```sh
cd audiosr_upsampling
```

5. **Install the necessary dependencies:**

```sh
pip install -r requirements.txt
```

---

## Prepare_Datasets

Place the audio files as follows. 

.mp3 or .wav files are okay. 

You must write '[language code]' on the back of the speaker folder.

```
audiosr_upsampling
├────datasets
│       ├───speaker0
│       │   ├────1.mp3
│       │   └────2.mp3
│       ├───speaker1
│       │    ├───1.wav
│       │    └───1.wav
│       ├───speaker2
│       │   ├────1.wav
│       └───└────1.wav
├────audiosr
├────.gitignore
├────main.py
├────Readme.md
└────requirements.txt
```

This is just an example, and it's okay to add more speakers.

### When you put audio datasets in one folder, please unify all the extensions into one!

---

## Usage

```sh
python main.py
```
