# Drachma Backend
#### BGE Treasurer app

**[Documentation Links](/docs/README.md)**

**[Frontend Repository](https://github.com/BetaGammaEpsilon-com/drachma-frontend)**

## Features
- :heavy_check_mark: Tracking of money for the entire Fraternity, member by member
- :heavy_check_mark: Transaction history for each member and the organization
- :heavy_check_mark: Automatic Treasurer Report compilation
- :heavy_check_mark: Automatic metrics on spending
- :heavy_check_mark: Endpoint testing in Postman
- Visualization production for these metrics
- Auto-update stored Google Drive file as a backup
- :heavy_check_mark: Extensive documentation for potential updates in the future
- Ability for users to upload receipts and update their own accounts, for review by the Treasurer
    - The Treasurer can also upload receipts
- :heavy_check_mark: Support for motion transaction tracking, motions can be selected for individual transactions
    - Visualizations for individual motions as well
- Estimated billing tracking
- Slack Integration

## MVP Priorities
1. Set up program structure
2. Database connections
3. Basic routing
4. Business logic in Backend
5. Bugfixing for 
6. Basic Frontend
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
- [Pandoc](https://pandoc.org/) (backend documentation)

### General
Issue tracking: Github Issues



