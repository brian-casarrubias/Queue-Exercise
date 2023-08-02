Design a food ordering system where your python program will run two threads,

Place Order: This thread will be placing an order and inserting that into a queue. 
This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
Serve Order: This thread will server the order. All you need to do is pop the order 
out of the queue and print it. This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.
Use this video to get yourself familiar with multithreading in python

Pass following list as an argument to place order thread,

orders = ['pizza','samosa','pasta','biryani','burger']
This problem is a producer,consumer problem where place_order thread is producing orders 
whereas server_order thread is consuming the food orders. Use Queue class implemented in a video tutorial.
________________________________________________________________________________________________________________

1) started off with making a Queue class with all the necessary methods/helpful methods that will help me later on
2) created an instance of the 'Queue" class, I named it 'q'
3) I created a list with some foods
4) I created two methods, one is going to place orders(placeOrder()), in this case it is going to 'enqueue' so its going to be appending to the left
..here I used a for loop to iterate all the items in the list, and enqueue them all.
.. I also used the datetime module to display the date/time (just to know when the order has been placed)
.. the exercise said to place an order every 0.5 seconds so I used the time.sleep(0.5)

5) the second method (serveOrder()) is going to be serving orders, and in this case, the method would start 1 second after 
I have started the placeOrder() method. I calculated the time it took using the time.time() before starting the placeOrder()
and then after the server() order has been executed, and using subtraction I got the time it took, in my case
"Total time it took for t2 to start after t1 started:    1.0089824199676514s" 

*in the serveOrder() method I set a variable name is_running = True so i can be in a continuous while loop
*then i check if the deque is empty because if it is empty, and I try to pop something out I will get an error...
*so if in the case that its empty, i print out that its finished serving everyone, then it breaks out of the while loop
..if its not empty, i will use time.sleep(2) before popping out/ using the dequeue() method

