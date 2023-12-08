#!/usr/bin/python3
"""
Delete out of date archives
"""
from datetime import datetime
from fabric.api import local, run, put, sudo, env, lcd


env.hosts = ['100.25.145.4', '52.91.152.172']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'
# env.keep_versions = 2


def do_clean(number=0):
    """
    cleans old archives from local and remote
    """
    number = int(number)
    if number == 0:
        number = 1

    with lcd("versions"):
        # local("ls -lt | tail -n +{} | rev | cut -f1 -d' ' | rev | \
        # xargs -d '\n' rm".format(number + 1))
        local("find . -maxdepth 1 -type f -printf '%T@ %p\n' | sort -n | \
                tail -n +{} | cut -f2- -d' ' | \
                xargs rm -rf".format(number + 1))

    run("ls -lt /data/web_static/releases/ | tail -n +{} | \
    xargs rm -rf".format(
        number + 1))


"""def do_clean(number=0):
    try:
        number = int(number)
        if number < 0:
            raise ValueError("Number cannot be negative")
    except ValueError:
        print("Invalid number. Provide a non negative integer")
        return False
    local_clean(number)
    remote_clean(number)


def local_clean(number):

    Delete unnecessary arhives from local

    with lcd("versions"):
        local("ls -lt | tail -n +{} | xargs rm -rf".format(number + 1))


def remote_clean(number):

    deletes unnecessary archives from remote

    with lcd("/tmp"):
        local("ls -lt | tail -n +{} | xargs rm -rf".format(number + 1))

    run("ls -lt /data/web_static/releases/ | tail -n +{} |
    xargs rm -rf".format(
        number + 1))


if __name__ == "__main__":
    do_clean(env.keep_versions)"""
