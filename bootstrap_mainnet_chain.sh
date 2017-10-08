#!/bin/sh
echo "Getting MainNet Chain"
wget 'https://www.dropbox.com/s/wpg03j503y3hucq/Chain.zip?dl=1'
echo 'Unzipping..'
unzip Chain.zip\?dl=1
mkdir ./neo-gui/bin/Release/Chain
mv Chain ./neo-gui/bin/Release/
echo 'Cleaning up'
