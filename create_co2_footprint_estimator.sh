#!/bin/bash
pip install -r requirements.txt
pip install transformers datasets flask
mkdir app
python3 ./train_footprint_model.py --tasks_list_file daily_tasks.txt
cd app
python3 ./carbon_footprint_app.py
