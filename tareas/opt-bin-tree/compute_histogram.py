import re, sys

buf = open( sys.argv[ 1 ], 'r' )
data = re.sub( '\n+', ' ', re.sub( ' +', ' ', re.sub( r"""[0-9%,.;@#?!&$\[\]\*\(\)\/\"\'\~\_\-]+\ *""", " ", buf.read( ), flags = re.VERBOSE ) ) ).lower( ).split( )
buf.close( )

histogram = {}
for d in data:
  if not d in histogram:
    histogram[ d ] = 1
  else:
    histogram[ d ] += 1
  # end if
# end for

for t in sorted( histogram ):
  print( t, histogram[ t ] )
# end for

# eof - compute_histogram.py
