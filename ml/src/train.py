import argparse
import yaml
from io import StringIO
import pandas as pd


parser = argparse.ArgumentParser()
parser.add_argument('--type', help='model type')
parser.add_argument('--chunk', help='chunk of data')
parser.add_argument('--params', help='path to params.yaml')
args = parser.parse_args()


def main():
    params = load_params(args.params)
    train(params['base']['data_dir'], params['base']['model_dir'], args.type, args.chunk)


def train(processed_data: str, model_dir: str, model_type: str, chunk: str):
    model = StringIO()
    df = pd.read_csv(f'{processed_data}/processed/data.csv', header=None)
    for _, row in df.iterrows():
        for cell in row:
            model.write(cell)
    with open(f'{model_dir}/{model_type}_{chunk}.file', 'w') as f:
        f.write(model.getvalue())


def load_params(filename: str):
    with open(filename, 'r') as f:
        params = yaml.safe_load(f)
        return params 



if __name__ == '__main__':
    main()
