from subprocess import call, PIPE, run
from time import sleep
import os
import sys

def restart():
    os.execl(sys.executable, 'python', __file__, *sys.argv[1:])

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
    main()
