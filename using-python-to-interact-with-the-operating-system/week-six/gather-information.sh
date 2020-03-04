#!/bin/bash

line="-------------------------------------------------------------------"

echo "Starting time at: $(date)"; echo $line

echo "UPTIME"; uptime; echo $line

echo "FREE"; free; echo $line

echo "WHO"; who; echo $line

echo "Finshing at: $(date)"