#!/bin/bash

for file in *.HTM; do
    name=$(basename "$file" .HTM)
    echo mv "$file" "$name.html"
done