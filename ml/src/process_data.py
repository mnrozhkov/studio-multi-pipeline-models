import argparse
import yaml
import pandas as pd


parser = argparse.ArgumentParser()
parser.add_argument('--chunk', help='chunk of data')
parser.add_argument('--params', help='path to params.yaml')
args = parser.parse_args()


def main():
    params = load_params(args.params)
    process_data(params['base']['data_dir'], args.chunk)


def process_data(data_dir: str, chunk: str):
    df = pd.read_csv(f'{data_dir}/raw/data.csv', header=None)
    for index, row in df.iterrows():
        if not any(chunk in str(cell) for cell in row):
            df.drop(index, inplace=True)
    df.to_csv(f'{data_dir}/processed/data.csv', header=False, index=False)


def load_params(filename: str):
    with open(filename, 'r') as f:
        params = yaml.safe_load(f)
        return params 


if __name__ == '__main__':
    main()
