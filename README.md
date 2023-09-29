
# Install 

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

# Run 

```
dvc exp run -R pipelines/type_a/X
dvc exp run -R pipelines/type_a/Y
dvc exp run -R pipelines/type_a/Z

```