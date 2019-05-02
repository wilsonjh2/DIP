#!/bin/bash

echo "Image name: $1"
python classify.py --model snake.model --labelbin mlb.pickle \--image examples/$1
