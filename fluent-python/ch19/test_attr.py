class Class:
    def __delattr__(self, name):
        print('## delattr')
        super().__delattr__(name)

    def __getattr__(self, name):
        print('## getattr')
        return 'default'

    def __getattribute__(self, name):
        print('## getattribute')
        super().__getattribute__(name)

    def __setattr__(self, name, value):
        print('## setattr')
        super().__setattr__(name, value)


if __name__ == "__main__":
    c = Class()
    getattr(c, 'name')
    print("-----")
    c.name
    print("-----")
    c.data = 'test'
    print("-----")
    c.data
    print("-----")
    del c.data

