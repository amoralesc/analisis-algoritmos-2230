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
int BinaryNode<T>::height() {
    int valt;

    if (this->isLeaf()) {
        valt = 0;
      } else {
        int valt_left = -1;
        int valt_right = -1;
        if (this->left != nullptr)
            valt_left = (this->left)->height();
        if (this->right != nullptr)
            valt_right = (this->right)->height();
        if (valt_left > valt_right)
            valt = valt_left + 1;
        else
            valt = valt_right + 1;
    }

    return valt;
}

template <class T>
int BinaryNode<T>::size() {
    int tam;

    if (this->esHoja()) {
        tam = 1;
    } else {
        int tam_left = 0;
        int tam_right = 0;
        if (this->left != nullptr)
            tam_left = (this->left)->size();
        if (this->right != nullptr)
            tam_right = (this->right)->size();

        tam = tam_left + tam_right + 1;
    }

    return tam;
}
