import pandas as pd


products = ["C","E","F","Q"]

# To convert to a series

product_cat = pd.Series(products)
print(product_cat)