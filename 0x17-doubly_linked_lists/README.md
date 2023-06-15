
ubly Linked Lists in C

This repository contains a simple implementation of doubly linked lists in the C programming language.

## What is a Doubly Linked List?

A doubly linked list is a data structure consisting of a collection of nodes, where each node contains a value and two pointers: one pointing to the previous node and one pointing to the next node. This allows for efficient traversal in both directions.

## Implementation Details

The doubly linked list implementation provided here includes the following operations:

- **Insertion**: Add a new node at the beginning or end of the list.
- **Deletion**: Remove a node from the list.
- **Traversal**: Traverse the list forward or backward, printing the node values.

The code is written in pure C and can be easily integrated into any C project.

## Usage

To use the doubly linked list implementation, follow these steps:

1. Include the `doubly_linked_list.h` header file in your C program.
2. Initialize a new doubly linked list using the `initializeList()` function.
3. Perform desired operations such as insertion, deletion, or traversal using the provided functions.
4. Finally, free the allocated memory using the `freeList()` function when you're done with the list.

## Example

Here's a simple example that demonstrates the usage of the doubly linked list implementation:

```c
#include <stdio.h>
#include "doubly_linked_list.h"

int main() {
    // Initialize a new list
    List* myList = initializeList();

    // Insert nodes
    insertAtBeginning(myList, 5);
    insertAtEnd(myList, 10);

    // Print list values
    printf("List values: ");
    traverseForward(myList);

    // Delete a node
    deleteNode(myList, 5);

    // Print list values after deletion
    printf("List values after deletion: ");
    traverseForward(myList);

    // Free memory
    freeList(myList);

    return 0;
}
```

## Contributing

Contributions to this repository are welcome. If you find any issues or want to add new features, please create a pull request.

