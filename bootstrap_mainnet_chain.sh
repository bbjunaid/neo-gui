#!/bin/sh
echo "Getting MainNet Chain"
#wget 'https://www.dropbox.com/s/wpg03j503y3hucq/Chain.zip?dl=1'
#wget 'https://drive.google.com/uc?export=download&confirm=1uIa&id=0Bwcc-DUGt9pjTnhVdW1QbHl4Wkk'
wget 'https://www.dropbox.com/s/jvhgetnlq8653ka/Chain.zip?dl=1'
echo 'Unzipping..'
unzip Chain.zip\?dl=1
#mkdir ./neo-gui/bin/Release/Chain
mv Chain ./neo-gui/bin/Release/
echo 'Cleaning up'
cd ./neo-gui/bin/Release
mkdir Chain
mv * Chain
