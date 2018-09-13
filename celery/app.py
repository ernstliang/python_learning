from task import add

def run():
    ret = add.delay(5, 9)
    print('ret: ', ret.get())
    print('ready: ', ret.ready())

if __name__ == '__main__':
    run()