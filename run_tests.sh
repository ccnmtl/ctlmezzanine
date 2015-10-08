#!/usr/bin/env bash

TEMPLATEDIR=`pwd`
DIR=/tmp/testctlmezz

# install Mezzanine into an outer virtualenv
rm -rf $DIR
mkdir $DIR
virtualenv $DIR/outer-ve
$DIR/outer-ve/bin/pip install Mezzanine

# then use that to make a test application
cd $DIR
./outer-ve/bin/mezzanine-project \
    --template=$TEMPLATEDIR \
    testproject
cd testproject

# run our tests (finally!)
make
