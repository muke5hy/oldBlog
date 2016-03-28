Title: Python interview Questions and Answer with links. 
Date: 2015-11-20 13:36:12.000000000 +05:30
Slug: python-interview-questions-and-answer-with-links.
Authors: Mukesh
Modified: 
Category: interview
Tags: python, interview
Status: draft
Summary: 

##Few of the interview questions for python developers
A really good discussion on the topic 
https://redd.it/1knw7z

1. Talk to me about the GIL. How does it impact concurrency in Python? What kinds of applications does it impact more than others?
2. How does Python's garbage collection work?
	Garbage collection has two type. 
	1. ## Automatic Garbage Collection of Cycles:
		Ptyhon schedules garbage collection based upon a threshold of object allocations and object deallocations. When the number of allocations minus the number of deallocations are greater than the threshold number, the garbage collector is run. One can inspect the threshold for new objects (objects in Python known as generation 0 objects) by loading the gc module and asking for garbage collection thresholds: 

		```python	
			import gc
			print "Garbage collection thresholds: %r" % gc.get_threshold()

		```
		`Garbage collection thresholds: (700, 10, 10)`

		Here we can see that the default threshold on the above system is 700. This means when the number of allocations vs. the number of deallocations is greater than 700 the automatic garbage collector will run. 
		Automatic Garbage collection does not works if Device is running out of memory. In such a situation application should handle it manually 
	2. ## Manual Garbage Collection 
		The garbage collection can be invoked manually in the following way:
		```python
			import gc
			gc.collect()
		```
		gc.collect() returns the number of objects it has collected and deallocated. You can print this information in the following way: 
3. What is the difference between range and xrange? How has this changed over time?
4. Here's a function. Optimize it for me.
5. How do you iterate over a list and pull element indices at the same time?
6. I'm getting a maximum recursion depth error for a function. What does this mean? How can I mitigate the problem?
7. How do you enforce ordering for a dictionary-style object?
8. How does Python's list.sort work at a high level? Is it stable? What's the runtime?
9. What's the difference between a list, dictionary, and array in Python?
10. What does this list comprehension do?
11. Here's a class hierarchy with some methods defined. When I call this function, what gets printed?
12. What is monkeypatching? How can you do it in Python?
13. What are some caveats to pickling? Marshaling?
14. How many ways can you append or concatenate strings? Which of these ways is fastest? Easiest to read?
15. Print me the full pathname of every file in this directory tree.
16. What's wrong with this function?
17. What's your preferred editor? (vim, of course - anything else and they fail.)

18. Do arguments in Python get passed by reference or by value?
19. Why are functions considered first class objects in Python?
20. What tools do you use for linting, debugging and profiling?
21. Give an example of filter and reduce over an iterable object
22. Implement the linux whereis command that locates the binary, source, and manual page files for a command.
23. What are list and dict comprehensions?
24. What do we mean when we say that a certain Lambda expression forms a closure?
25. What is the difference between list and tuple?
26. What will be the output of the following code?

###Few excersise before you go for interview

1. You have list 100 words, sort them. 
	* What if the list is in million
	* How will you search/find a particular word. 
2. 