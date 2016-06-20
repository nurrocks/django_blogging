from fabric.api import local


def hello():
    print("Hello world!")

def nur():
    print('haha')
    local('ls -al')
