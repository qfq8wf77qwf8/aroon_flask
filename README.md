
# What is required?

- This server runs on flask. So you need to have python installed (most machine already has python installed)
- All installation is managed by `pip`. This comes with most system pythons.

# Installaion Instructions

- requirement.txt has all the dependency of this mini webserver. To install them, run `pip install -r requirement.txt`


# Running the webserver

- Go to the root directory of the package and run the following:
- `export FLASK_APP=index.py`
- `export FLASK_DEBUG=1`
- `flask run`
- Visit http://127.0.0.1:5000/ and you should see "Not Found" error (this is OK)

# Where is the page located at?

- The ABC page is at http://127.0.0.1:5000/abc/offer/1/
- The /1/ can be changed to /2/ /3/ /4/ to explore different offers.

# Editing your changes:

- The main areas for you to change are:
  - templates/abc_index.html (this is the index.html)
  - static/sharktank/ABC/css/* (css files)
  - static/sharktank/ABC/js/* (js files)
  - static/sharktank/ABC/img/* (img files)

- Everytime you make a change, if you ran `export FLASK_DEBUG=1` your change will appear automatically.

# Note:

- Different offer has different images. Some images are non transparent while others are a lot uglier. This is what we have so far.

# Have fun editing!




