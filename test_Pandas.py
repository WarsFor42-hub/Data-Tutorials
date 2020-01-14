import pandas
import numpy

def import_txt_dataframe(PATH):
    dataframe = pandas.read_table(PATH, sep='\t', header=0)
    return dataframe

def main():
    df=import_txt_dataframe("heart.txt")
    df_limited=df.iloc[0:10,0:4].copy()
    print(df_limited)
    grouped_age=df_limited.loc[df['type_douleur']=="C",:].groupby('sexe')['age','pression']
    sum_age=grouped_age.agg(numpy.sum)
    print(sum_age)

if __name__=='__main__':
    main()


