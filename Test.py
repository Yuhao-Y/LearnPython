if True:
    x = "hello"
    print(x,end=''); #不换行输出
    print("world")

    '''
    python variable. python have 4 type of variable: Numbers, String, List, Tuple, Dictionary
    '''
    a=b=c=1;
    a,b,c=1,2,'abcdefg'; # 0 and -1 are present the last and the last but one value in the string,
    list = [1,2,'a',3,'b']
    tuple = (1,2,3,4) # tuple is similar with list,just like a read-only list. Tuple could not be assignment value twice.
    dictionary = {2:100,'a':1000,'b':'c'};# dictionary is store i key-valye, and only could get value by key.
    print(a);
    print(c[-2:-1]);
    print(list);
    print(tuple);
    print(dictionary[2]); # the 2 in the [] is not means the index, otherwise, it means the key store in the dictionary
    print(hex(a)); # function hex( int x ): transform x to the hexdecimal