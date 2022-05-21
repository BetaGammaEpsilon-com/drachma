# Drachma
#### BGE treasurer app

## User setup
TODO

## Developer setup
#### Backend
1. Clone this repository, and go into the cloned directory
2. [Install Anaconda](https://www.anaconda.com/)
3. Set up virtual environment: 

&nbsp;&nbsp;&nbsp;&nbsp;```conda create -n drachma python=3.9```

4. Switch into virtual environment: 

&nbsp;&nbsp;&nbsp;&nbsp;```conda activate drachma```

5. Install necessary packages:

&nbsp;&nbsp;&nbsp;&nbsp;```conda install -r requirements.txt```

6. Set up the program databases and tables:

&nbsp;&nbsp;&nbsp;&nbsp;```python setup.py```

7. Run the program:

&nbsp;&nbsp;&nbsp;&nbsp;```python run.py```

#### Frontend
TODO

## Features
- Tracking of money for the entire Fraternity, member by member
- Transaction history for each member and the organization
- Automatic Treasurer Report compilation
- Automatic metrics on spending
- Visualization production for these metrics
- Auto-update stored Google Drive file as a backup
- Extensive documentation for potential updates in the future
- Ability for users to upload receipts and update their own accounts, for review by the Treasurer
    - The Treasurer can also upload receipts
- Support for motion transaction tracking, motions can be selected for individual transactions
    - Visualizations for individual motions as well
- Estimated billing tracking
- Slack Integration

## Priorities
1. Set up program structure
2. Database connections
3. Basic routing
    - Endpoint testing in Postman
4. Set up data models, decide formats to pass between frontend and backend
5. Business logic in Backend
6. Basic Frontend/Backend connections
7. Polish Frontend
8. Additional features (fancy things eg. Slack integration)
9. Abstract, prepare for eventual expansion
10. Finalize documentation

## Current Technology Planning

### Backend
Python 3.9 or greater

Modules:
- [Flask](https://flask.palletsprojects.com/en/2.1.x/) (routing)
- [SQLite3](https://www.sqlite.org/index.html) (database)
- [Pandas](https://pandas.pydata.org/) (when extracting from DB)
- [Matplotlib](https://matplotlib.org/) and [Seaborn](https://seaborn.pydata.org/) (data visualization)
- TODO: Report compilation
- [Pandoc](https://pandoc.org/) (backend documentation)

### Frontend
TODO

- Look into Python frontend libraries
- React
- Go ?

### General
Issue tracking: Github Issues



