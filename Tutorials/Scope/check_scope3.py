def check_scope():
    def do_local():

        name = "do local"

    def do_non_local():

        name = "do non local"

    def do_global():
        global name
        name = "do global"

    name = "check scope"

    print(name)

check_scope()
