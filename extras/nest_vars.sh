#!/bin/bash

export NEST_INSTALL_DIR=/home/perser/workspace/nest-2.10.0/build
export PYTHONPATH=$NEST_INSTALL_DIR/lib/python2.7/site-packages:$PYTHONPATH
export PYTHONPATH=$NEST_INSTALL_DIR/lib64/python2.7/site-packages:$PYTHONPATH
export PATH=$NEST_INSTALL_DIR/bin:$PATH
