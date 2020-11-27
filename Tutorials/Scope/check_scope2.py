def check_scope():
    def do_local():
        nonlocal name
        name = "do local"

    def do_non_local():
        name = "do non local"
    def do_global():
        name = "do global"
    name = "check scope"
    #print(name)
    do_local()
    print(name)
    do_non_local()
    print(name)
    do_global()
    print(name)


check_scope()