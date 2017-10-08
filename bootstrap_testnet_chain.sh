#!/bin/sh
echo "Getting Testnet Chain"
wget 'https://www.dropbox.com/sh/gbrggfzojqjdltf/AABzUkaacmhyTRSwsMxFEMCla/ChainTestNet.zip?dl=1'
echo 'Unzipping..'
unzip ChainTestNet.zip\?dl=1
mv ChainTestNet ./neo-gui/gui_test/Debug/
echo 'Cleaning up'
rm -rf ChainTestNet.zip?dl=1
