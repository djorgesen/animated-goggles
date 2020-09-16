This is a simple django app designed to be run with the django development server. There would be many drastic changes 
for an app that was designed for users.

This is setup to be a simple django server that runs with docker-compose.
To run the server, from the root of the project run the command
`docker-compose up -d`
If you want to watch the server output you can leave of the `-d`.

The docker-compose command will start a simple django development web server which
will then have the gui available at `http://localhost:8000`
There is a home screen and 4 pages with inputs and an output.

In the app I've imported bootstrap for some simple styling and access to jquery which I'll use to fire off post requests 
asynchronously, as its a little easier than making forms that submit, though that is how I'd do it if I were making 
something more robust. 
I'm submitting these requests to the server just to show the answer performed in python though for all of these tasks 
it would be simple to create the functions in js. All the python code for getting the answers is in `pages/views.py`
