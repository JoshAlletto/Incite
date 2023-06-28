# Incite
## Running the proposal code steps:
STEP 1: Click on green code button
![Picture of Repo](Pictures\GitHub.png)
STEP 2: Click download zip, and then unzip the folder

STEP 3: Transfer this folder into your desktop by extracting the files and browsing into your desktop folder.

![Picture of Folder](Pictures\ExtractedFolder.png)

Now your new files should be able to be found when you look in your desktop files.

![Incite Folder](Pictures\InciteFolder.png)

STEP 4: If not installed already, download Anaconda

Link to install anaconda.com/download/ : ![Anaconda](Pictures\Conda.png)

Step 5: FOR WINDOWS USERS

search for anaconda using windows search bar

![Powershell terminal](Pictures\AnacondaPowershell.png)

use anaconda powershell prompt(will not work with regular anaconda prompt)

STEP 6: For MAC/LINUX open a terminal window 

(On MAC, terminal window can be opened from the utilities folder in your Applications )


STEP 7: Begin installing neccesary packages

In your terminal window, type the following commands one at a time and hit enter

    'conda install pip'

You will now begin pip installing all packages(press enter after each line)

    'pip install PyPDF2'

    'pip install PdfReader'

    'pip install textract'

    'pip install openpyxl'

    'pip install pdfplumber'

STEP 7: Create a folder inside of your new incite folder named PDF FILES that will hold all the proposal PDFS (as shown in picture below) 

![Folder of PDFS](Pictures\PDFS.png)

STEP 8: Download zip file of PDFs from Peernet and transfer them into this folder

STEP 9: Download the latest excel template from box and put it in the Incite folder. Call this sheet"template"

For mac, your folder should now look like this:

![Folder picture for Max/Linux](Pictures\MacFolder.png)

STEP 10: Running your code in your terminal(scroll down for LINUX/MAC)

Step 11(windows users): Within your anaconda powershell prompt window open, locate to your code so that we can run the script.  Enter the following commands line by line until you reach the desired location

    'conda activate proposals'

    'cd Desktop'

    'cd Incite'

    'ls'
you should now be here 

![Location in terminal](Pictures\TerminalLocation.png)

now enter in the following command 

    'python do_the_thing.py'

Now everything should have run correctly and you are done!
You can view your completed excel sheet in the updated incite file.

Step 11(Mac/Linux): Within your regular terminal, activate the neccesary packages above by locating to your folder as shown above and running the python code.







