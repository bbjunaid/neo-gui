#!/bin/sh
echo "Getting Testnet Chain"
rm -rf ./neo-gui/bin/Debug/ChainTestNet
wget 'https://www.dropbox.com/s/qcicbuft05bcmj3/ChainTestNet.zip?dl=1'
echo 'Unzipping..'
unzip ChainTestNet.zip\?dl=1
mv ChainTestNet ./neo-gui/bin/Debug/
echo 'Cleaning up'
rm -rf ChainTestNet.zip?dl=1
