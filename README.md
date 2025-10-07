Simple Backend Order

Overview:
The program is designed so that it feeds in mock results, using an array, which can also be replaced with a 
API feeding information or database, with the use of a function.

It then generates data to populate the data, including the use of a array to catch reciept of all orders,
a hash map to allow easy searching through the data
and a deque for the data to be processed and manipulated if needed
(at this moment the data is not manipulated or edited)

The data is then sorted, first with accessing the hash map to find the information required, such as quantity
then sorted to offer a high to low in terms of quantity of an item

This is then outputted at the end of the program

Techniques used:
Making use of algorithms is important, in both time used and computational memory. The memory was chosen in order
to make the program as efficient as possible, and not being java with its heap memory management.
Hash maps are also used in order to access memory.
As the program is not asynchronous, memory management isnt as important as well as due to the constraints not expected
to handle thousands of data entries.