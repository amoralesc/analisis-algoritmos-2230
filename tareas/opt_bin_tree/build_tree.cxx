#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

#include "binary_node.h"

double BuildTree(
  const std::vector< std::string >& T,
  const std::vector< double >& P,
  const std::vector< double >& Q,
  BinaryNode<unsigned long long>* root
  )
{
  std::vector< std::vector< double > > M( Q.size( ), std::vector< double >( Q.size( ), 0 ) );
  std::vector< std::vector< unsigned long long > > B( Q.size( ), std::vector< unsigned long long >( Q.size( ), 0 ) );

  // Base cases
  for( unsigned long long i = 0; i < Q.size( ); ++i )
  {
    std::cout << "Base case: " << ( i + 1 ) << "/" << P.size( ) << std::endl;
    M[ i ][ i ] = Q[ i ];
  } // end for
  
  // Recursive cases
  for( unsigned long long i = P.size( ); i > 1; --i )
  {
    std::cout << "Row: " << ( i + 1 ) << "/" << P.size( ) << std::endl;
    for( unsigned long long j = i; j < Q.size( ); ++j )
    {
      double w = Q[ i - 1 ];
      for( unsigned long long l = i; l <= j; ++l )
        w += P[ l - 1 ] + Q[ l ];
      double q;
      unsigned long long k;
      for( unsigned long long r = i; r <= j; ++ r )
      {
        double v  = M[ i - 1 ][ r - 1 ] + M[ r ][ j ] + w;
        if( r == i || v < q ) {
          q = v;
          k = r;
        }
      } // end for
      M[ i - 1 ][ j ] = q;
      B[ i - 1 ][ j ] = k;
    } // end for
  } // end for

  // Backtracking
  

  return( M[ 0 ][ P.size( ) ] );
}

int main( int argc, char** argv )
{
  std::vector< std::string > T;
  std::vector< double > P, Q;

  std::ifstream file( argv[ 1 ] );
  std::string line;
  Q.push_back( 1 );
  double nP = 0;
  while( std::getline( file, line ) )
  {
    std::istringstream in_line( line );
    T.push_back( "" );
    P.push_back( 0 );
    Q.push_back( 1 );
    in_line >> T.back( ) >> P.back( );
    nP += P.back( );
  } // end while

  double pP = 0.8 / nP;
  double pQ = 0.2 / double( Q.size( ) );

  for( unsigned i = 0; i < P.size( ); ++i )
  {
    P[ i ] *= pP;
    Q[ i ] *= pQ;
  } // end for
  Q[ P.size( ) ] *= pQ;

  BinaryNode<unsigned long long>* root;
  double R = BuildTree( T, P, Q, root );
  std::cout << R << std::endl;

  return( EXIT_SUCCESS );
}

// eof - build_tree.cxx
