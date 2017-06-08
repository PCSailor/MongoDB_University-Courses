# Homework 1.1
Download Handouts:  hw1-1__m101j_m101p_5258458de2d4233537765336.zip
Install MongoDB on your computer and run it on the standard port.

Download the HW1-1 from the Download Handout link and uncompress it.

Use mongorestore to restore the dump into your running mongod. Do this by opening a terminal window (mac) or cmd window (windows) and navigating to the directory so that you are in the parent directory of the dump directory (if you used the default extraction method, it should be hw1/). Now type:

mongorestore dump

Note you will need to have your path setup correctly to find mongorestore.

Next, go into the Mongo shell, perform a findOne on the collection called hw1 in the database m101. That will return one document. Please provide the value corresponding to the "answer" key from the document returned.

hint: if you got back a document that looks like { "_id": 1234, "answer": 2468 }, you would put in 2468 (with no spaces) for your answer. This is not the correct number; you should get a different number.


# Homework 1.2
Download Handouts:  hw1-2.py
Get PyMongo installed on your computer. To prove it's installed, run the program:

python hw1-2.py

Note that you will need to get MongoDB installed and the homework dataset imported from the previous homework (or download from the attached handout material) before attempting this problem.

This program will print a numeric answer. Please put just the 4-digit number into the box below (no spaces).


# Homework 1.3
Download Handouts:  hw1-3.py
We are now going to test that you have bottle installed correctly and can run a bottle-based project. Download the handout and run it as follows:

python hw1-3.py

It requires that:

    bottle be installed correctly
    your mongodb to be running
    you have run mongorestore properly

From a different terminal window type the following from the command line: curl http://localhost:8080/hw1/50

Alternatively, you can put the url above into your web browser.

Type the two-digit answer into the box below (no spaces).