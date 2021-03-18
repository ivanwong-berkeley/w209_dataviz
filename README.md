W209 DataViz - Dashboard Ivan Wong

To Run:
- Create a virtual environment with python >=3.7
- Install Dependencies: 
  - With PIP: `pip install -r requirement.txt`
  - With Anaconda: `conda install --file requirements.txt`

- Run the web app with
  `python ./run.py`

For the ischool server:
- cd ~
- mv w209 w209.original
- git clone git@github.com:ivanwong-berkeley/w209_dataviz.git w209
- /usr/local/bin/virtualenv w209
- cd w209
- source bin/activate
- pip install `cat requirements.txt`
- touch start.wsgi

Whenever you make a change, touch start.wsgi to force the server to reload
