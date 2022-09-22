#include "binary_node.h"

#include <queue>

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

template <class T>
long long BinaryNode<T>::find(T value) {
    return this->find(value, 0);
}

template <class T>
long long BinaryNode<T>::find(T value, long long depth) {
    if (value == this->value) {
        return depth;
    }
    // The binary tree is ordered, so we can use this to reduce the search space
    // If it's a leaf, we can't go further
    if (this->isLeaf()) {
        return -1;
    }
    // Search in the left and right subtrees
    if (value < this->value) {
        if (this->left != nullptr) {
            return (this->left)->find(value, depth + 1);
        }
    } else {
        if (this->right != nullptr) {
            return (this->right)->find(value, depth + 1);
        }
    }
    // If we get here, the value is not in the tree
    return -1;
}

template <class T>
std::vector<T> BinaryNode<T>::preOrder() {
    std::vector<T> v;
    this->preOrder(v);
    return v;
}

template <class T>
void BinaryNode<T>::preOrder(std::vector<T>& v) {
    v.push_back(this->value);
    if (this->left != nullptr)
        (this->left)->preOrder(v);
    if (this->right != nullptr)
        (this->right)->preOrder(v);
}

template <class T>
std::vector<T> BinaryNode<T>::inOrder() {
    std::vector<T> v;
    this->inOrder(v);
    return v;
}

template <class T>
void BinaryNode<T>::inOrder(std::vector<T>& v) {
    if (this->left != nullptr)
        (this->left)->inOrder(v);
    v.push_back(this->value);
    if (this->right != nullptr)
        (this->right)->inOrder(v);
}

template <class T>
std::vector<T> BinaryNode<T>::postOrder() {
    std::vector<T> v;
    this->postOrder(v);
    return v;
}

template <class T>
void BinaryNode<T>::postOrder(std::vector<T>& v) {
    if (this->left != nullptr)
        (this->left)->postOrder(v);
    if (this->right != nullptr)
        (this->right)->postOrder(v);
    v.push_back(this->value);
}

template <class T>
std::vector<T> BinaryNode<T>::levelOrder() {
    std::vector<T> v;
    this->levelOrder(v);
    return v;
}

template <class T>
void BinaryNode<T>::levelOrder(std::vector<T>& v) {
    std::queue<BinaryNode<T>*> q;
    q.push(this);
    while (!q.empty()) {
        BinaryNode<T>* n = q.front();
        q.pop();
        v.push_back(n->value);
        if (n->left != nullptr)
            q.push(n->left);
        if (n->right != nullptr)
            q.push(n->right);
    }
}
