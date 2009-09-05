#!/bin/bash

./google_appengine/appcfg.py \
    upload_data --config_file=airport_loader.py \
    --filename=album_data.csv 
    --kind=Airport
    --url=http://localhost:8080/remote_api fg_nav_app/
