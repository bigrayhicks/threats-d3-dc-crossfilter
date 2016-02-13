# D3, DC, Crossfilter - Threats

This is deployed as a Flask web server using D3, DC and Crossfilter to generate the front-end
visualizations and MongoDB to store the back-end data.

I'll jot down a list of dependencies or make a dockerfile available for building a 
proper environment to run the application.

First, run 'python generate_events.py' to load MongoDB with a few thousand threat events. Then
you may run the application by running 'python app.py'. The web server runs via port 5000.

