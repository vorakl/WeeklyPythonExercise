def read_n(fn, N=3):
    ''' Rean N lines at once from a text file
    '''
    with open(fn, "rt") as file:
        res = ''
        for i, s in enumerate(file, 1):
            res = ''.join( (res, s) )
            # check if we read N lines
            if not i%N:
                yield res
                res = ''
        else:
            # check if we exited, but haven't read all N lines 
            # and haven't yielded them yet
            if res != '':
                yield res
