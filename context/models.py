from context.domains import Dataset
import pandas as pd


class Model:
    dataset = Dataset()

    def new_model(self, fname) -> object:
        this = self.dataset
        this.context = './data/'
        this.fname = payload

        return pd.read_csv(f'{this.dname}{fname}', index_col=False)