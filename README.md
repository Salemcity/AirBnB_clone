AirBnB clone

DESCRIPTION OF THE PROJECT:

The goal of the project is to deploy on my server a simple copy of the AirBnB website.
I am not to implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.

DESCRIPTION OF THE COMMAND:

The console is a command interpreter to manage objects abstraction between objects and how they are stored.
The console will perform the following tasks:

Create a new object
Retrive an object from a file
Do operations on objects
Destroy an object
store and persist objects to a file (JSON file)

STORAGE
All the classes are handled by the Storage engine in the FileStorage Class.

The first piece is to manipulate a powerful storage system.
This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. 
This means: from the console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine

All the development and testing was runned over an operating system Ubuntu 20.04 LTS using programming language Python 3.8.3. 
The editors used were VI, VSCODE,Git

HOW TO START
git clone https://github.com/Salemcity/AirBnB_clone.git
change to the AirBnb directory and run the command:

 ./console.py 

HOW TO USE IT

Start the console in interactive mode:
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
(hbnb)
(hbnb) quit
$
in Non-interactive mode

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
EOF  all  count  create  destroy  help  quit  show  update
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
EOF  all  count  create  destroy  help  quit  show  update
(hbnb)
$
Authors

Adetibubo Salem Gbeminiyi - gemgbeminiyi@gmail.com

Wamalwa Christian Timbe - bobitlmr188221@spu.ac.ke

