## Linked Lists

Linked lists are fundamental data structures used to organize data in a sequential manner. Unlike arrays, linked lists use nodes that contain data and a reference to the next node in the sequence, allowing for efficient insertion and deletion operations.

#### Linked Lists Types

1. Singly Linked List
   A singly linked list is a type of linked list where each node points to the next node in the sequence. It consists of nodes where each node has two components:

Data: The value stored in the node.
Next: A reference to the next node in the sequence.

2. Doubly Linked List
   A doubly linked list is a type of linked list where each node points to both its previous and next nodes. This allows traversal in both directions (forward and backward).

Data: The value stored in the node.
Next: A reference to the next node in the sequence.
Prev: A reference to the previous node in the sequence.

3. Circular Linked List
   A circular linked list is a variation where the last node points back to the first node, creating a circular structure. This can be implemented in both singly and doubly linked lists.

### Real-Time Examples of Linked Lists

1. Web Browser Navigation (Doubly Linked List):

When you click the back button in a browser, it uses the previous pointer to show the last visited page, and the next pointer for the forward button.

2. Music Playlist (Circular Linked List):

A music player playing songs in a loop mode uses a circular linked list where the last song points back to the first song.

3. Undo Functionality in Text Editors (Doubly Linked List):

Pressing 'Ctrl + Z' in a text editor uses the previous pointer to revert to the last state, and 'Ctrl + Y' uses the next pointer to redo changes.
