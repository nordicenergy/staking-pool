# Nordic Energy Staking Pool

[![Netlify Status](https://api.netlify.com/api/v1/badges/7565685d-d830-481d-9775-a7ca3e994549/deploy-status)](https://app.netlify.com/sites/nordic-energy-staking-pool/deploys)

This repository contains the UI for Nordic Energy's Staking Pool, which was built in Django. It also contains the Solidity smart Contract that represents each staking pool and the Truffle code to deploy it.

## Requirements

* Python 3.5
* PIP 3.5
* Django 3.0.6
* MySQL, PSQL or SQLite
* API Key from Infura

Modify `settings.py` to complete the database settings, a `SECRET_KEY`, and the API Key for Infura. For the database you can use MySQL, PSQL or SQLite (among others). 

Enter the `nordic_energy_pool` folder and Use the following commands to install all the necessary libraries (we recommend you to use a virtual environment for this), create the migrations to generate the database tables and run these migrations.

```
 pip3 install -r requirements.txt
 python3 manage.py makemigrations
 python3 manage.py migrate
```

## Start the UI

Use the following command to run the UI:

```
 python3 manage.py runserver 0.0.0.0:8000
```

You can then open a browser and navigate to `http://localhost:8000`.


## Data

Data is coming from the smart contract and the database. You can use the real contract which is already configured in `settings.py` or deploy a new instance and configure it there. If you use Ropsten, change the Infura URL too. For the database, you can create some rewards in the table to have some testing data.
