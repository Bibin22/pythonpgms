def check_scope():
    def do_local():
        name = "do local"

    def do_non_local():
        nonlocal name
        name = "do non local"
    def do_global():
        name = "do global"

    name = "check scope"
    #print(name)
    do_non_local()
    print(name)

check_scope()


""" ivide output ' do non local ' aanu eee ' do non local ' vannad 'def do_non_local enna functionil ninu aaanu
     normaly eee pgm run cheythal 'def check_scop() ' functionil koduthekuna name = 'check scope' aanu print cheyandath
     ennal 'def do_non_local' enna functionil name ine 'nonlocal'(its a keyword') aayi define cheyunu 
     athukond 'do_non_local()' call cheyumbol 'def_check_scope' enna funcionil koduthekunaa name ="check scope" enna value
    'def do_non_local' enna functionile name = "do non local" enna value aayi marukayum ath print aavukayum cheyunu
    NB: CHECK PROGRAMS check_scope2.py check_scope3.py
    
    """
