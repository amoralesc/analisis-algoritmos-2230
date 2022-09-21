#pragma once

#include <list>

using namespace std;

template <class T>
class BinaryNode {
    protected:
        T value;
        BinaryNode<T>* left;
        BinaryNode<T>* right;
    public:
        BinaryNode();
        BinaryNode(T value);
        ~BinaryNode();
        T getValue();
        void setValue(T value);
        BinaryNode<T>* getLeft();
        BinaryNode<T>* getRight();
        void setLeft(BinaryNode<T>* left);
        void setRight(BinaryNode<T>* right);
        bool isLeaf();
        int height();
        int size();
        //void preOrden(list<T> &datos);
        //void inOrden(list<T> &datos);
        //void posOrden(list<T> &datos);
        //void nivelOrden(list<T> &datos);
};

#include "binary_node.hxx"
