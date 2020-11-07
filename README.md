# Auto-Patcher-v.3
Stops Services. Copies Files from SRC to DST. Starts Services

I am in the process of teaching myself Python.
This code has come a long way in the last couple of weeks.
This is the final version of my first attempt at creating a Python Program.

This project probably will not work for most people, but I believe the code will be helpful for new people looking to learn how to do some basic Automation in Python.

The program contains a pretty basic copyloop()
This function will go through a specified folder in the source directory (which happens to be where the program is ran from) and it will take the files from that folder and copy them to a specified target folder.

One issue I ran into is if you are trying to copy contents within a folder that have other folders with content in them this basic copy function does not work.
In this project I only had this issue with one folder and that is the WebPortal folder.
If you scroll down through the code near the end you will see the WebPortal has its own set of code it uses.

I am going to be honest this took me a long time to figure out and I did a lot of searching on the web. I am not really 100% sure why it works.
The other part that I don't understand is you cannot use it for the other folders and I think its due to the tuple, but again I don't understand it well enough right now to know why.

Next we have the basic stop and start services.
I created a servicesList of all the services we would stop and start and later on in the program I would use a function I created to stop each service by looping through the list.

The final function I created was just a colourText function. It allowed you to use the function to type in any text you wanted and then add the colour you wanted the text to be.
After looking at the orignal code compared to this I don't really think I saved myself a whole lot of trouble, but oh well.

If you are interested in seeing the other two iterations of this Auto Patcher please check out my gist: https://gist.github.com/chuckcoggins/
