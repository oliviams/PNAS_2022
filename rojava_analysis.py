import pandas as pd
from config import * # contains path

locations = ['Raqqa', 'Al-Bukamal', 'Deir-ez-Zor', 'Hajin', 'Al-Tabqa', 'Shadadah', 'Bahguz', 'Sosa', 'Shafa', 'Al-Bab', 'Al-Mayadin', 'Al-Hassakeh', 'Basira']

# patterns = ['aaa', 'aaaab', 'aaab', 'aaabaaabaab', 'aaabab', 'aaabb', 'aaabb', 'aab', 'aabab',
#             'aababab', 'aababab', 'aabb', 'aabbb', 'aabbbb', 'abab', 'abababb', 'ababb', 'abb',
#             'abbb', 'abbbabbbabb', 'abbbb', 'bbb']

# Inlcuding all permutations of each pattern
patterns_extended = ['abab','baba', 'aaa','bbb','ababb','babba','abbab','bbaba','babab','abb','bab','bba','aab','aba','baa',
                     'aaab','aaba','abaa','baaa','aaaab','aaaba','aabaa','abaaa','baaaa','aabab','ababa','babaa','abaab',
                     'baaba','aaabab','aababa','ababaa','babaaa','abaaab','baaaba','abababb','bababba','ababbab','babbaba',
                     'abbabab','bbababa','bababab','aabb','abba','bbaa','baab','aaabb','aabba','abbaa','bbaaa','baaab',
                     'aabbbb','abbbba','bbbbaa','bbbaab','bbaabb','baabbb','aabbb','abbba','bbbaa','bbaab','baabb','abbb',
                     'bbba','bbab','babb','aababab','abababa','bababaa','ababaab','babaaba','abaabab','baababa','abbbb',
                     'bbbba','bbbab','bbabb','babbb','abababb','bababba','ababbab','babbaba','abbabab','bbababa','bababab',
                     'abbbabbbabb','bbbabbbabba','bbabbbabbab','babbbabbabb','abbbabbabbb','bbbabbabbba','bbabbabbbab',
                     'babbabbbabb','abbabbbabbb','bbabbbabbba','babbbabbbab','abbbabbbabb','aababab','abababa','bababaa',
                     'ababaab','babaaba','abaabab','baababa','aaabaaabaab','aabaaabaaba','abaaabaabaa','baaabaabaaa',
                     'aaabaabaaab','aabaabaaaba','abaabaaabaa','baabaaabaaa','aabaaabaaab','abaaabaaaba','baaabaaabaa',
                     'aaabb','aabba','abbaa','bbaaa','baaab']

# Actors in ACLED dataset associated with Kurdish and ISIS forces
kurdish_list = ['QSD: Syrian Democratic Forces', 'Global Coalition Against Daesh',
                'YPG: Peoples Democratic Forces - Anti-Terror Unit', 'YPG: Peoples Protection Units - Special Task Forces',
                'YPG: Peoples Protection Units', 'YPG: Peoples Protection Units - Anti-Terror Unit',
                'YPG: Peoples Protection Units - Hezen Komandoz', 'YPJ: Women\'s Protection Units',
                'YPS: Civil Protection Units', 'YRK: Eastern Kurdistan Units', 'TAK: Kurdistan Freedom Hawks',
                'PKK-YJA STAR: Kurdistan Workers Party-YJA STAR', 'PKK: Kurdistan Workers Party']

isis_list = ['Islamic State (Syria)', 'Islamic State (Iraq)']

patterns_length = []
for pattern in patterns_extended:
    patterns_length.append(len(pattern))

# Creating file per quarter for each location containing occurrences of each pattern
for location in locations:
    for year in ['2017', '2018', '2019']:
        for quarter in ['Q1', 'Q2', 'Q3', 'Q4']:
            try:
                filepath = path + location +'/' + location + '_' + quarter + '_' + year + '.csv'
                file = pd.read_csv(filepath, sep=',')
                actions_list = file['actor1'].to_list()
                new_list = []
                for i in range(len(actions_list)):
                    if actions_list[i] in kurdish_list:
                        new_list.append('a')
                    elif actions_list[i] in isis_list:
                        new_list.append('b')
                actions_string = ''.join([str(elem) for elem in new_list])

                count = []
                for pattern in patterns_extended:
                    count.append(actions_string.count(pattern))
                df = pd.DataFrame({'Pattern': patterns_extended, 'Count': count, 'Length': patterns_length})
                df['Proportion'] = (df.Count * df.Length) / len(actions_string)
                df = df[['Pattern', 'Count', 'Proportion']]
                df = df.sort_values(by=['Proportion'], ascending=False)
                df.to_csv(location + '_' + quarter + '_' + year + '_extended.csv')
            except:
                pass