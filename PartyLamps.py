#! /usr/bin/env python3
from math import log

nfl = 10  # number of lamps
cnt = 1   # counter
on  = []  #
off = [6] #

# Return only first nfl bits of p. Button A is ~ operation, so
# in that case mask will return the unsigned nfl-bit number.
def mask( p ): return p & (( 1 << nfl ) - 1 )

def sift():
    ''' ..01010101 '''
    n = 1
    for j in range( 1, int( log( nfl, 2 )) + 1 ):
        s = n << ( 1 << j )
        n |= s
    return n

odd  = mask( sift() )
even = mask( ~odd )

def sift3():
    """ ..001001001001001 """
    # let's keep it simple here
    n     = 1
    nbits = 0
    while nbits < nfl:
        n |= n << 3
        nbits += 3
    return n

odd3  = mask( sift3() )
even3 = mask( ~odd3 )

def Up( p ):
    ''' A: all '''
    return mask( ~p )

def Left( p ):
    ''' B: odd '''
    return ( ~p & odd )|( p & even )

def Ryte( p ):
    ''' C: even '''
    return Left( ~p )

def Down( p ):
    """ D: 3K + 1 """
    return ( ~p & odd3 )|( p & even3 )

def spit( p ):
    """ Hello World! """
    width = int( log( 2**nfl, 10 )) + 1
    print( '{0:d}'.format( p ).rjust( width, '0' ),
           '{0:b}'.format( p ).rjust( nfl, '0' ))

def bfs():
    """ boom """
    p = mask( -1 )
    ck = { p }
    pare = [ p ] 
    chil = []
    levl = 0
    while True:
        while pare:
            p = pare.pop()
            for mv in [ Up, Left, Ryte, Down ]:
                q = mv( p )
                if q not in ck:
                    ck.add( q )
                    chil.append( q )
        if not chil:
            print( 'End of tree reached!' )
            break
        levl += 1
        if levl == cnt: break
        pare, chil = chil, pare
    return chil

################################################################
def check_config( p ):
    """ Ck if lamps configuration fits the on and off states """
    # Ok we're assuming here 0-based indexing zo..
    for lamp in on:
        if p & ( 1 << lamp ) == 0: return False
    
    for lamp in off:
        if p & ( 1 << lamp ) != 0: return False

    return True

if __name__ == '__main__':

    print( 'nfl:', nfl )
    print( 'cnt:', cnt )
    print( 'on :', on  )
    print( 'off:', off )

    for p in filter( check_config, bfs() ): spit( p )

# log:
