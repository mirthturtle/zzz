# zzz – sleep computer

Feeling tired? Why not stay up and hack together a machine to help you experience [lucid dreams](https://en.wikipedia.org/wiki/Lucid_dream).

![zzz in operation](https://github.com/mirthturtle/zzz/blob/main/bedside.jpg "zzz in operation")

Wear a trigger-style mouse on your finger during sleep to play sounds with small hand movements. Hearing these sounds in a dream can alert you to your state and make the dream more interactive.

## Equipment

You will need:
- [Raspberry Pi](https://www.raspberrypi.com/) w/ wireless capability
- An ergonomic handheld trigger mouse
- Speaker or headphones

## Setup

Clone the repo to your Pi. Install Python:
```
sudo apt update
sudo apt install python3 python3-pip
```
Install dependencies:
```
pip3 install pygame evdev
```
Depending on your Pi OS version you may need to add `--break-system-packages` here; this is fine if your Pi will be a dedicated `zzz` machine and you don't care about your Python environment; otherwise, create a virtual environment.

Put sounds in the `sound` directory and link them to your desired buttons in `zzz.py`.

## Running

Run with: `sh run.sh`.

