#!/bin/bash

sudo apt install git cmake libjpeg-dev build-essential screen -y
cd ~
git clone https://github.com/jacksonliam/mjpg-streamer.git
cd mjpg-streamer/mjpg-streamer-experimental
make
sudo make install

