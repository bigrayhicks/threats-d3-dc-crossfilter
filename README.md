# D3, DC, Crossfilter - Threats

This is deployed as a Flask web server using D3, DC and Crossfilter to generate the front-end
visualizations and MongoDB to store the back-end data.

I'll jot down a list of dependencies or make a dockerfile available for building a 
proper environment to run the application.

![Threats](/images/threats.gif)

## Running the Application

First, inject some threat documents into MongoDB by executing the following:

$ python generate_events.py

Next, run the Flask application as follows (and the web server runs via port 5000):

$ python app.py


