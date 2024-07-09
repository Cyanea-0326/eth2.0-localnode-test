#!/bin/bash

cd docker || { echo "ディレクトリ docker が見つかりません"; exit 1; }
rm -rf geth/*
rm -rf prysm-beacon/*
rm -rf prysm-validator/*
