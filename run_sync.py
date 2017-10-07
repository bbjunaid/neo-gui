from subprocess import call, PIPE, run
from time import sleep
import os
import sys

RESTART_CMD = os.getcwd()+'/scripts/commands/restart_sync'

def restart():
    print("!! RESTARTING !!")
    sleep(2)
    sys_run['sh', 'scripts/git_restart.sh']
    os.execl(sys.executable, 'python', __file__, *sys.argv[1:])

def check_commands():
    restart_needed = os.path.exists(RESTART_CMD)
    if restart_needed:
        restart()


def sys_run(commands):
    return run(commands, stdout=PIPE, stderr=PIPE)

def sync(latest_hash):
    # we have to move the commands to external file as cygwin has issues
    # running git commands in python
    result = sys_run(['sh', 'scripts/git_test.sh'])
    retrieved_hash = result.stdout

    if retrieved_hash != latest_hash:
        print("!! New version available !!")
        result = sys_run(['sh', 'scripts/git_pull.sh'])
        print("> Pull OK ")

        check_commands()

        # print("--> Restarting...")
        # restart()
    else:
        print("Latest OK [%s]" % retrieved_hash)

    return retrieved_hash

def main():
    latest_hash = None

    while True:
        latest_hash = sync(latest_hash)
        sleep(5)
        print("Done")


if __name__ == '__main__':
    # main()
    check_commands()
