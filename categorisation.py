import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

strategies = ['TFT', 'TF2T', 'COP', 'DEF', 'HTFT', 'ALT',
              '2TFT', 'BU', 'CCD', 'CCCD', 'DDC', 'DES',
              'FBF', 'HL', 'WL', 'UC', 'UD']

strat_cat = {'TFT': ['-', '-', '-', 'abab', '-', 'abab', '-', 'aabb', 'abab', 'abab', 'aabb', 'aabb', '-', 'abab', '-', '-', 'aabb'],
             'TF2T': ['-', '-', '-', 'abab', '-', 'aaa', '-', 'aaabb', 'aaa', 'aaa', 'aab', 'aaabb', '-', 'aaa', '-', '-', 'abab'],
             'COP': ['-', '-', '-', 'aaa', '-', 'aaa', '-', 'aaa', 'aaa', 'aaa', 'aaa', 'aaa', '-', 'aaa', '-', '-', 'aaa'],
             'DEF': ['abab', 'abab', 'bbb', 'abab', 'abab', 'abb', 'abab', 'bbb', 'abbb', 'abbbb', 'ababb', 'abb', 'abab/bb', 'bbb', 'abab', 'bbb', 'abab'],
             'HTFT': ['-', '-', '-', 'abab', '-', 'abb', '-', 'aabbbb', 'abbb', 'abbb', 'ababb', 'abb', '-', 'aaab', '-', '-', 'abab'],
             'ALT': ['abab', 'bbb', 'bbb', 'aab', 'aab', 'abab', 'aab', 'abab', 'babab', 'abb', 'aababab', 'abab', 'abab', 'abab', 'bbb', 'abab', 'abab'],
             '2TFT': ['-', '-', '-', 'abab', '-', 'abb', '-', 'aabbb', 'abb', 'abb', 'ababb', 'abb', '-', 'abb', '-', '-', 'abab'],
             'BU': ['abab', 'ababb', 'bbb', 'aaa', 'babaaa', 'abab', 'aabab', 'abab', 'abb', 'abbb', 'aab', 'abab', 'baba/babb', 'abab', 'bbb', 'bbb', 'aaa'],
             'CCD': ['abab', 'bbb', 'bbb', 'aaab', 'aaab', 'aabab', 'aab', 'aab', 'abab', 'abababb', 'aab', 'aab', 'abab', 'abab', 'bbb', 'abab', 'aaab'],
             'CCCD': ['abab', 'bbb', 'bbb', 'aaaab', 'aaab', 'aab', 'aab', 'aaab', 'abababa', 'abab', 'aaabaaabaab', 'aaab', 'abab', 'aab', 'bbb', 'abab', 'aaab'],
             'DDC': ['abab', 'abb', 'bbb', 'aabab', 'aabab', 'abababb', 'aabab', 'abb', 'abb', 'abbbabbbabb', 'abab', 'aabb', 'baba/babb', 'abb', 'bbb', 'bbb', 'aabb'],
             'DES': ['abab', 'ababb', 'bbb', 'aab', 'aab', 'abab', 'aab', 'abab', 'abb', 'abbb', 'abab', 'abab', 'baba/babb', 'abab', 'bbb', 'bbb', 'abab'],
             'FBF': ['-', '-', '-', 'aab', '-', 'abab', '-', 'aabb', 'abab', 'abab', 'aab', 'aab/aabb', '-', 'abab', '-', '-', '-'],
             'HL': ['abab', 'bbb', 'bbb', 'aaa', 'aaab', 'abab', 'aab', 'aaa', 'abab', 'abb', 'aab', 'aaa', 'abab', 'abab', 'bbb', 'abab', 'bbb'],
             'WL': ['-', '-', '-', 'abab', '-', 'aaa', '-', 'aaa', 'aaa', 'aaa', 'aaa', 'aaa', '-', 'aaa', '-', '-', 'abab/aaa'],
             'UC': ['-', '-', '-', 'aaa', '-', 'abab', '-', 'aaa', 'abab', 'abab', 'aaa', 'aaa', '-', 'abab', '-', '-', 'aaa'],
             'UD': ['abab', 'abab', 'bbb', 'abab', 'abab', 'abab', 'abab', 'bbb', 'abbb', 'abbb', 'abab', 'abab', 'baba/bab', 'bbb', 'abab/bbb', 'bbb', 'abab']}

strat_df = pd.DataFrame(strat_cat)
strat_df.index = strategies

for col in strat_df:
    for i, row_value in strat_df[col].iteritems():
        if row_value == '-':
            pass
        else:
            strat_df[col][i] = row_value.count('a')/len(row_value)

strat_df = strat_df.replace('-', np.nan)
strat_np = strat_df.to_numpy()
axis_labels = strategies

plt.figure(figsize=(12, 9))
sns.heatmap(strat_np, cmap='coolwarm', xticklabels=strategies, yticklabels=strategies)
plt.show()
