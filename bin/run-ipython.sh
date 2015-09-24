#!/bin/bash 

echo " Launching iPython... see http://localhost:8888/"

ipython notebook --ip=* --pylab=inline --no-browser &
