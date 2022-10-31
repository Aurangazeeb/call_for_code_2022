#!/bin/bash
pip install transformers datasets
mkdir app
python3 ./train_footprint_model.py --tasks_list_file daily_tasks.txt
cd app
python3 ./carbon_footprint_app.py