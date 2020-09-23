import profile
def myfunct():
    my_list = [
        1,5,4,3,2,6,11
    ]
    
    # my_list=str(my_list).strip("[|]|"or" ")
    print(my_list)
    print(len(my_list))
profile.run('myfunct()')