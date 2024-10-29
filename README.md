# zzz – sleep computer

Feeling tired? Why not stay up and hack together a machine to help you experience [lucid dreams](https://en.wikipedia.org/wiki/Lucid_dream).

Wear a trigger-style mouse on your finger during sleep to play sounds with small hand movements. Hearing these sounds in a dream can alert you to your state and make the dream more interactive.

## Equipment

You will need:
- [Raspberry Pi](https://www.raspberrypi.com/) w/ wireless capability
- An ergonomic handheld trigger mouse
- Speaker or headphones

## Setup

Install dependencies:
```
sudo apt update
sudo apt install python3 python3-pip
pip3 install pygame --break-system-packages
pip3 install evdev --break-system-packages
```

Find some sounds you like and put them in the `sound` directory. Link them at the top of `zzz.py`.

## Running

Run with: `python3 zzz.py`

