#!/bin/bash
echo "Project/Model: $1"
echo "Division/Data: $2"

echo "Copy a $1:dvc.yaml template to pipeline: pipelines/$1/$2"
cp pipelines/$1/template_dvc.yaml pipelines/$1/$2/dvc.yaml

echo "Run DVC pipeline: pipelines/$1/$2"
dvc exp run -R pipelines/$1/$2/dvc.yaml