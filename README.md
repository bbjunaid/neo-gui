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
`git commit -am 'restart'`
`git push origin master`

This will cause the syncers to restart their own processes
