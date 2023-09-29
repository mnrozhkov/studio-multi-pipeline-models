
# Install 

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

# Run (`type_a` project)

```
dvc exp run -R pipelines/type_a/x
dvc exp run -R pipelines/type_a/y
dvc exp run -R pipelines/type_a/z

```

# Run (`type_b` project)

`run.sh` script copies `dvc.yaml` template for a target division, and then runs a DVC pipeline.
 
```
./run.sh $PROJECT $DATA 
```
Arguments:
- $PROJECT: `type_b`
- $DATA (division): [x, y, z]