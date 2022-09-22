#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

#include "binary_node.h"

BinaryNode<std::string>* BuildOptTree(
  const std::vector<std::string>& T, 
  const std::vector<std::vector<unsigned long long>> B,
  unsigned long long i,
  unsigned long long j
  ) 
{
  if (i > j)
    return nullptr;

  unsigned long long k = B[i][j];
  BinaryNode<std::string>* node = new BinaryNode<std::string>(T[k]);

  if (i == j) {
    return node;
  }

  node->setLeft(BuildOptTree(T, B, i, k - 1));
  node->setRight(BuildOptTree(T, B, k + 1, j));

  return node;
}

BinaryNode<std::string>* BuildAVLTree(
  const std::vector<std::string>& T,
  unsigned long long i,
  unsigned long long j
  )
{
  if (i >= j)
    return nullptr;

  unsigned long long k = (i + j) / 2;
  BinaryNode<std::string>* node = new BinaryNode<std::string>(T[k]);

  node->setLeft(BuildAVLTree(T, i, k));
  node->setRight(BuildAVLTree(T, k + 1, j));

  return node;
}

void PrintTreeOrder(
  BinaryNode<std::string>* node,
  std::string order
  ) 
{
  if (node == nullptr)
    return;

  std::vector<std::string> v;
  if (order == "pre")
    v = node->preOrder();
  else if (order == "in")
    v = node->inOrder();
  else if (order == "post")
    v = node->postOrder();
  else if (order == "level")
    v = node->levelOrder();
  else
    return;

  for (unsigned long long i = 0; i < v.size(); i++) {
    std::cout << v[i];
    if (i < v.size() - 1)
      std::cout << " ";
  }
  std::cout << std::endl;
}

double BuildTree(
  const std::vector< std::string >& T,
  const std::vector< double >& P,
  const std::vector< double >& Q,
  BinaryNode<std::string>* &root_opt,
  BinaryNode<std::string>* &root_avl
  )
{
  std::vector< std::vector< double > > M( Q.size( ), std::vector< double >( Q.size( ), 0 ) );
  std::vector< std::vector< unsigned long long > > B( Q.size( ), std::vector< unsigned long long >( Q.size( ), 0 ) );

  // Base cases
  for( unsigned long long i = 0; i < Q.size( ); ++i )
  {
    std::cout << "Base case: " << ( i + 1 ) << "/" << P.size( ) << std::endl;
    M[ i ][ i ] = Q[ i ];
    B[ i ][ i ] = i;
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
          k = r - 1;
        }
      } // end for
      M[ i - 1 ][ j ] = q;
      B[ i - 2 ][ j - 1 ] = k;
    } // end for
  } // end for

  // Build Opt Tree
  root_opt = BuildOptTree(T, B, 0, T.size() - 1);
  // Build AVL Tree
  root_avl = BuildAVLTree(T, 0, T.size());

  return( M[ 1 ][ P.size( ) ] );
}

void LeastJumpsToFindMaxExperiment(
  BinaryNode<std::string>* root_opt,
  BinaryNode<std::string>* root_avl,
  std::string word
) {
  std::cout << "Least jumps to find the max word experiment" << std::endl;
  std::cout << "Word: " << word << std::endl;

  const long long opt = root_opt->find(word);
  const long long avl = root_avl->find(word);

  std::cout << "Optimal tree: " << opt << std::endl;
  std::cout << "AVL tree: " << avl << std::endl;

  if (opt < avl)
    std::cout << "Optimal tree is better" << std::endl;
  else if (opt > avl)
    std::cout << "AVL tree is better" << std::endl;
  else
    std::cout << "Both trees are the same" << std::endl;
}

int main( int argc, char** argv )
{
  std::vector< std::string > T;
  std::vector< double > P, Q;

  std::ifstream file( argv[ 1 ] );
  std::string line;
  Q.push_back( 1 );
  double nP = 0;

  std::string max_word;
  double times_max_word = 0;
  while( std::getline( file, line ) )
  {
    std::istringstream in_line( line );
    T.push_back( "" );
    P.push_back( 0 );
    Q.push_back( 1 );
    in_line >> T.back( ) >> P.back( );

    if (P.back() > times_max_word) {
      max_word = T.back();
      times_max_word = P.back();
    }

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

  BinaryNode<std::string>* root_opt;
  BinaryNode<std::string>* root_avl;
  double R = BuildTree(T, P, Q, root_opt, root_avl);
  std::cout << "R: " << R << std::endl << std::endl;

  LeastJumpsToFindMaxExperiment(root_opt, root_avl, max_word);

  return( EXIT_SUCCESS );
}

// eof - build_tree.cxx
