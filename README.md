Project Setup
=============

On Linux:
=========
`yum install leveldb-devel`

On Windows:
===========

To build and run locally, you need to clone and build https://github.com/neo-project/leveldb first, 
then copy `libleveldb.dll` to the working directory (i.e. /bin/Debug, /bin/Release)

Note: When building, the project file settings must be changed from static library (lib) to dynamic linked library (dll).

# Testnet:
https://neoscan-testnet.io/

# Mainnet:
https://neotracker.io/


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
