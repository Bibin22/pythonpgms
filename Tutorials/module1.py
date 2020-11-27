
     #import module method 1

#import if_sample
#if_sample.check(10)       #  function call method 1
#numb = int(input("Enter a number"))
#if_sample.check(numb)    #   function call method 1.1
#check2 = if_sample.check
#check2(numb)             #   function call method 3

     # import module method 2

#from if_sample import check
#check(10)   #  function call method 1
#check2 = check  #   function call method 2
#check2(10)

    # import module method 3 (Renaming Module)

#import if_sample as ifs
#ifs.check(10)  #  function call method 1
#check2 = ifs.check  #  function call method 2
#check2(10)

    # import module method 4 (Renaming Function)

from if_sample import check as ch
# ch(10) #  function call method 1
#ch2 = ch #  function call method 2
#ch2(10)