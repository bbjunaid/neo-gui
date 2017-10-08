Project Setup
=============
# Main Chain, Testnet Chain, leveldb.dll:
Bootstrap Testnet chain
`./bootstrap_testnet_chain.sh`

Bootstrap Mainnet chain
`./bootstrap_mainnet_chain.sh`

Or manually download at:
https://www.dropbox.com/sh/gbrggfzojqjdltf/AABBDto9RD6PdtuYXFqRhPK0a?dl=0

# Testnet:
https://neoscan-testnet.io/

# Mainnet:
https://neotracker.io/

Installation
=====
1. Create VM in  3 regions  ( Korea, US East, Germany )
  - 120 GB SSD
  - 2 CPU
  - 16 GB of RAM
2. Open Internet Explorer
3. Set Internet options and Enable
  - Java Applet
  - Scripting
  - Downloads
4. Restart Internet Explorer
5. Download Google Chrome
6. Install Cygwin 
  - wget
  - openssh
  - git
  - curl
  - unzip
7. Install your SSH pub/priv key
7b. Test with `ssh -T git@github.com`
8. git clone this repo

If you get permissioning issues make sure:
- `chmod +x neo-gui.exe`
- `chmod +x libleveldb.dll`

9. Download ChainTestNet.zip from Dropbox
10. Unzip ChainTestNet.zip into
  - gui_test/Debug
  - for production we'll have bin/Debug
11. Verify  constants.json  as rpx: false




Syncer
=====

Install:
- cygwin
- cygwin git, wget, curl, python


`python run_sync.py`

Commands
===
`./restart_sync.sh`
All syncers will restart themselves once.
`./stop_restart_sync.sh`
Stop sending the restart signal everytime you push.

TODO
===
- restart neo-gui binary
- run a manual clicker version for RPX

TROUBLESHOOTING
===
- if ./git_head.sh shows no hash, try dos2unix git_head.sh

