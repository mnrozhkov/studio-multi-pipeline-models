import argparse
import pandas as pd
from .utils import load_params

parser = argparse.ArgumentParser()
parser.add_argument('--chunk', help='chunk of data')
parser.add_argument('--params', help='path to params.yaml')
args = parser.parse_args()


def main():
    params = load_params(args.params)
    process_data(params.raw_data, params.processed_data, args.chunk)


def process_data(data_dir: str, output_dir: str, chunk: str):
    df = pd.read_csv(f'{data_dir}/data.csv', header=None)
    for index, row in df.iterrows():
        if not any(chunk in str(cell) for cell in row):
            df.drop(index, inplace=True)
    df.to_csv(f'{output_dir}/data.csv', header=False, index=False)


if __name__ == '__main__':
    main()
