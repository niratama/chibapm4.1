from fabric.api import *

def host_name():
    run('hostname')

def get_hosts():
    get('/etc/hosts')

def sudo_test():
    run('whoami')
    sudo('whoami')

