def simple_coroutine(): #
    print('-> coroutine started')
    x = yield#
    print('-> coroutine received:', x)


