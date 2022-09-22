#pragma once

#include <vector>
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
        long long find(T value);
        std::vector<T> preOrder();
        std::vector<T> inOrder();
        std::vector<T> postOrder();
        std::vector<T> levelOrder();
    private:
        long long find(T value, long long depth);
        void preOrder(std::vector<T>& v);
        void inOrder(std::vector<T>& v);
        void postOrder(std::vector<T>& v);
        void levelOrder(std::vector<T>& v);
};

#include "binary_node.hxx"
