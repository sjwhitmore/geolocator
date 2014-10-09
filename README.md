# Geolocator

This should get the location of a visitor to a site and store it in an SQL database.  The Google API is used to find a visitor's location from their IP address and JQuery is used to submit this information (if the user clicks the "store in the server" link at the bottom of the page).

If this link is clicked, the function on line 31 in index.html will submit the information to the Flask server, calling the function get_location on line 44 in geolocator.py.  On success, the words "Successfully stored!" should be displayed at the bottom of the page.

To use locally, clone this repository and in the root directory, start the Flask server with the command
```python 
> python geolocator.py
```

You will need to first initialize the database by starting a Python shell in the directory and issuing the following commands:
```python
>>> from geolocator import init_db
>>> init_db
```