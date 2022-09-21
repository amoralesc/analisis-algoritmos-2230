import re, sys

def BuildTree( T, P, Q ):
  M = [ [ 0 for j in range( len( Q ) ) ] for i in range( len( Q ) ) ]

  # Base cases
  for i in range( len( Q ) ):
    print( 'Base case: ' + str( i + 1 ) + '/' + str( len( P ) ) )
    M[ i ][ i ] = Q[ i ]
  # end for

  # Recursive cases
  for i in range( len( P ), 0, -1 ):
    print( 'Row: ' + str( i + 1 ) + '/' + str( len( P ) ) )
    for j in range( i, len( Q ) ):
      q = None
      for r in range( i, j + 1 ):
        v  = M[ i - 1 ][ r - 1 ] + M[ r ][ j ] + Q[ i - 1 ]
        for l in range( i, j + 1 ):
          v += P[ l - 1 ] + Q[ l ]
        # end for
        if q is None or v < q:
          q = v
        # end if
      # end for
      M[ i - 1 ][ j ] = q
    # end for
  # end for

  return M[ 0 ][ len( P ) ]
# end def

buf = open( sys.argv[ 1 ], 'r' )
T = []
Q = [ 1 ]
P = []
nP = 0
for line in buf.readlines( ):
  tokens = line.split( )
  T += [ tokens[ 0 ] ]
  Q += [ float( 1 ) ]
  P += [ float( tokens[ 1 ] ) ]
  nP += float( tokens[ 1 ] )
# end for
buf.close( )

pP = 0.8 / nP
pQ = 0.2 / float( len( Q ) )

Q = [ v * pQ for v in Q ]
P = [ v * pP for v in P ]

# Build tree
R = BuildTree( T, P, Q )
print( R )

#R = BuildTree( [ 'a', 'b', 'c', 'd', 'e' ], [ 0.15, 0.1, 0.05, 0.1, 0.2 ], [ 0.05, 0.1, 0.05, 0.05, 0.05, 0.1 ] )
#print( R )

# eof - build_tree.py
