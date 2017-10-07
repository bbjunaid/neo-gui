# REKT PULSE 2017
#

from subprocess import call, PIPE, run, Popen
from time import sleep
import os
import sys

RESTART_CMD = os.getcwd()+'/scripts/commands/restart_sync'
NEO_RESTART_CMD = os.getcwd()+'/scripts/commands/neo_restart_sync'

def restart():
    print("!! Syncer Restart Command SEEN !!")
    sleep(2)
    sys_run(['sh', 'scripts/git_restart.sh'])
    print("!! RESTARTING !!")
    os.execv(sys.executable, [sys.executable] + sys.argv)

def neo_restart():
    print("KILLING NEO")
    result = sys_run(['sh', 'scripts/kill_neo.sh'])
    sleep(1)
    print("RESTARTING NEO")
    result = Popen(['sh', 'scripts/start_neo.sh'])
    pass

def check_commands():
    restart_needed = os.path.exists(RESTART_CMD)
    if restart_needed:
        restart()

    neo_restart_needed = os.path.exists(NEO_RESTART_CMD)
    if neo_restart_needed:
        neo_restart()


def sys_run(commands):
    result = run(commands, stdout=PIPE, stderr=PIPE)
    if result.stderr:
        print(result.stderr)
    return result

def sync(latest_hash):
    # we have to move the commands to external file as cygwin has issues
    # running git commands in python
    result = sys_run(['sh', 'scripts/git_test.sh'])
    retrieved_hash = result.stdout.strip()

    if retrieved_hash != latest_hash and latest_hash not in retrieved_hash:
        print("!! New version available !!")
        result = sys_run(['sh', 'scripts/git_pull.sh'])
        print("> Pull OK %s" % retrieved_hash)

        check_commands()

        # print("--> Restarting...")
        # restart()
    else:
        print("Latest OK [%s]" % retrieved_hash)

    return retrieved_hash

def main():
    result = sys_run(['sh', 'scripts/git_head.sh'])
    latest_hash  = result.stdout.strip()

    while True:
        latest_hash = sync(latest_hash)
        sleep(5)


if __name__ == '__main__':
    main()
    # check_commands()
    # test_restart()
    # neo_restart()
