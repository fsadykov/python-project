# Marvel Scripting Assessment
#company-projects 

Write a script that will:
	1. Display the request header in a terminal window for  [link](https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png) 
	2. Save the header information into a text file named header.txt
	3. Upload the linked image from step 1, header.txt file, and your script to an S3 bucket


## How to use the script? 
Before using the script you will need to set up your environment variables. You can put your environment variables inside `~/.bashr` or  just run export command to set environment variable for current session
```
export ACCESS_KEY="Your AWS Access Key"
export SECRET_KEY="Your AWS Secret Key"
```

After you set your environment variables you will need to install some libraries to run script.
```
pip install -r requirements.txt
```

After you have installed all libraries your are ready to run the script 
```
python request-header-upload/upload-header.py
```