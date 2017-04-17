
--
By Aditya Daryanani 2017 
--

Application Architecture: This application follows the client server architecture where the client and server architecture are independent.

Client ---> GET request with required number of n-grams ------> Server
Client <---				JSON Response				    <------ Server


Dependencies:

Server Side:
Python 3.6 running in an Anaconda environment
Libraries:
collections, re, flask, nltk, flask_cors

Client Side:
js, html
Libraries:
d3 (Use the included d3.js)
d3.layout.cloud.js (Use the included d3.layout.cloud.js)

Instructions for Set Up and Demonstration:

SERVER:
1.) Make sure to start the server first and test using your browser
2.) To start the server execute the script server.py in the server folder
3.) Make sure the experimental file e.txt is still present in the same folder as the script and all 	the dependent libraries are installed in your system.
4.) The libraries are installed by default in the Anaconda enviromnent for Python 3.6
5.) Once the script starts the default ip address will be http://127.0.0.1:5000/ on OS X / Linux. 
6.) Your script will output ip address onto your console.
7.) If the IP address differs from the one above the client system code will need to be changed.
8.) Once the server is up and running type the IP address http://127.0.0.1:5000/ on the browser.
9.)	You should see the message "The server is up and running!" in the browser window.
10.)The server script is only using a small portion of the Text Data File because the processing for 	 the whole data file is too slow. So a smaller file called e.txt is used for demonstration.
11.)The file name can be changed on line 72 of the server code
12.)The number of n-grams are fixed on line 59 of the script at 10. This can be changed but for demonstration purposes it is fixed for now.

CLIENT:
1.) Once the server is up and running run "index.html" in the client directory. The browser I used was 	   chrome.
2.) There will be an option to select the number of n-grams and select start.
3.) The client will send a GET request to http://127.0.0.1:5000/GetNgrams/2 where 2 is the number of n-grams.
4.) The server will process the data file and return a JSON response of the format
	{
 		 "active directory": 8, 
 		 "assigned infrastructure": 11, 
  		 "communication skills": 9, 
  		 "e g": 9, 
  		 "equal opportunity": 13, 
	     "full time": 8, 
	     "infrastructure functions": 11, 
	     "must able": 11, 
	     "written verbal": 9, 
    }
    This response contains the n-gram phrase and its corresponsing frequency of occurence.
4.) The client application will use this to render a word cloud with the help of d3.js.    
5.) Click on start. Even though the file is small this will take a while to process and the page will not display anything for this period.
6.) Once the processing is done a word-cloud should appear.
7.) You can alter the parameters and you should get a different word-cloud.

