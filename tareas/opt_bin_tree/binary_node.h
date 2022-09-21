#pragma once

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
        unsigned long long height();
        unsigned long long size();
};

#include "binary_node.hxx"
