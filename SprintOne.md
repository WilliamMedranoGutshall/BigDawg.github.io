 	The first enhancement started with the final project from IT 145. In this class I created an authentication system for zoo application. The user was given the opportunity to enter a username and password, and these credentials were matched against a file list. The passwords were stored and compared in MD5, message digest, hash form for more security. The user was limited to three failed logins before the program was exited and if they authenticated correctly, they were given access to a file based on their role. I chose this project because it was one of my early projects and I thought is was a great opportunity to show the evolution of my programming skills and mastering of best practices and the SDLC, software development lifecycle. I was given the message digest hashing algorithm that was used for storing and checking passwords, and at this point in my education, I had very little knowledge of hashing or using algorithms to perform functions. I have since studied the process of hashing and practices using more complex algorithms. 
	I chose to convert this program from Java into Python for my first enhancement. Our computer science education exposed us to a wide variety of related topics, and I have learned multiple languages including Java, Python, C++, HTML5, CSS, SAS, and SQL. I feel as if my eportfolio having a similar application developed in both Java and Python would be a great way to display my versatility. I also believe that Python was a better choice for this application since the end goal is to lead into creating a database based application that will allow credentials to be maintained externally to the program code and thus making it more usable for an end user.  This program also allowed me to display my improved code architecture skills and utilize software development best practices for a better designed application. Two of the weak points of my first application were that it was difficult to follow because it wasn’t broken down into separate methods and I had way too many variables. My enhancement removed variables by using lists instead of names such as zooKeeperOne, zooKeeperTwo, and zooKeeperThree. This is a smart design choice because not only does it reduce variables, it makes it much simpler to add additional users. Additions only require adding the username, password, and job title to the correct list and adding one to the number of staff variable. This is all located at the top of the program and clearly indicated by comments. The hashing that was performed by additional code provided in my previous project is performed utilizing a hashing library. The ability to replace an entire algorithm with an import command and library call drastically decreases the amount of code and makes it much simpler to work with. Instead of just displaying a print line depending on the job title, I customized a menu page. Each type of job has its own menu that is called based on the value of the job title list, and the username is passed into the method to be used for personalization. Currently this menu only allows the user to display their job tasks or log out; however, I have created a good foundation to make this feature easy to expand on. I also created some additional job titles to make the application more realistic to an application that would be used. This enhancement completed everything that it was supposed to accomplish and added additional features that wasn’t in the original Java application. I have also begun to work on the second enhancement by adding some input limitations, such as limiting the length of a username to ten characters. If a job title is not recognized in the if/elif loops that call the appropriate menu, then there is a default else statement to warn the user to contact their administrator because they system couldn’t resolve their current position. These limitations as well as adding error handling will be important for hardening my application for good application level security. The hashing algorithm used to store the passwords provides an extra layer of defense because it is harder to steal than it would be if it was just in plain text. I will continue to expand on this in my next enhancement. My design plan for the first and second enhancements hasn’t changed; however, I will be changing my plan for the third enhancement. I ran into issues trying to implement a database using the Eclipse IDE, therefore I will be switching to using Python scripts in Codio to implement and utilize the no-SQL database MongoDB. This change has already been approved. 
	The biggest challenge I faced was working with the MD5 hashing. When I did the original project, I was provided this hashing algorithm and just had to use what I was given. Since I was re-writing this application in Python, I had to figure out how to implement it without it being given to me. As I did some research, I realized that Python has a hashing library available to use. I wasn’t familiar with using it, so I created a Python script in Codio to import the library, convert a given string, and display the output. To verify that it was functioning correctly, I created a test program in Python, copied the output into the program as a variable and used the program to test if the values were the same. This program wouldn’t initially run and was returning a “Non-ASCII character” error. I learned that there are different ways to digest and display the hashing output and to make it functional for my program I had to use the hexdigest() function. I experimented with different ways to implement and use the hexdigest output and ended up saving the output of the hexdigest to a variable and then comparing it to stored value which worked. This was the first time that I truly got some hands-on experience with hashing and I learned more about it working on this application than I have in my previous classes. 
	I also got some good practice working with Python methods. When I look back on my original program, my code was hard to follow and had a lot of variables that weren’t necessary. One of my goals of this enhancement was to write an application that was easy to follow, easy to maintain and easy to expand. My previous Python projects were also lacking good use of methods to complete repeatable functions. For this application I used a separate method for each function, such as checking usernames, checking passwords, and staff menus that were dependent on their job title. I got practice sending and receiving information from these methods, including receiving more than one variable back from the method which I had never done before. I learned some new techniques for working with methods and got practice using good design methodology to create a better version of my previous work. 