#!/bin/bash

# stop uwsgi process
/bin/ps -ef |grep uwsgi | grep -v grep | awk '{ print $2 }' | xargs kill -9
