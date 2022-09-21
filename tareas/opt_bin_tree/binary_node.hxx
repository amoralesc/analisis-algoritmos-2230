#include "binary_node.h"

template <class T>
BinaryNode<T>::BinaryNode() {
    this->left = nullptr;
    this->right = nullptr;
}

template <class T>
BinaryNode<T>::BinaryNode(T value) {
    this->left = nullptr;
    this->right = nullptr;
    this->value = value;
}

template <class T>
BinaryNode<T>::~BinaryNode() {
    if (this->left != nullptr) {
        delete this->left;
        this->left = nullptr;
    }
    if (this->right != nullptr) {
        delete this->right;
        this->right = nullptr;
    }
}

template <class T>
T BinaryNode<T>::getValue() {
    return this->value;
}

template <class T>
void BinaryNode<T>::setValue(T value) {
    this->value = value;
}

template <class T>
BinaryNode<T>* BinaryNode<T>::getLeft() {
    return this->left;
}

template <class T>
BinaryNode<T>* BinaryNode<T>::getRight() {
    return this->right;
}

template <class T>
void BinaryNode<T>::setLeft(BinaryNode<T>* left) {
    this->left = left;
}

template <class T>
void BinaryNode<T>::setRight(BinaryNode<T>* right) {
    this->right = right;
}

template <class T>
bool BinaryNode<T>::isLeaf() {
    return (this->left == nullptr && this->right == nullptr);
}

template <class T>
unsigned long long BinaryNode<T>::height() {
    unsigned long long h;

    if (this->isLeaf()) {
        h = 0;
    } else {
        unsigned long long left_height = -1;
        unsigned long long right_height = -1;
        if (this->left != nullptr)
            left_height = (this->left)->height();
        if (this->right != nullptr)
            right_height = (this->right)->height();
        if (left_height > right_height)
            h = left_height + 1;
        else
            h = right_height + 1;
    }

    return h;
}

template <class T>
unsigned long long BinaryNode<T>::size() {
    unsigned long long s;

    if (this->isLeaf()) {
        s = 1;
    } else {
        unsigned long long left_size = 0;
        unsigned long long right_size = 0;
        if (this->left != nullptr)
            left_size = (this->left)->size();
        if (this->right != nullptr)
            right_size = (this->right)->size();
        s = left_size + right_size + 1;
    }

    return s;
}
