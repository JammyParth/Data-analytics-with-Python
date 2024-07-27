import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data():
    df = pd.read_csv('medical_examination.csv')
    return df

def add_overweight(df):
    df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2) > 25
    df['overweight'] = df['overweight'].astype(int)
    return df

def normalize_data(df):
    df['cholesterol'] = df['cholesterol'] - 1
    df['gluc'] = df['gluc'] - 1
    return df

def draw_cat_plot(df):
    df_cat = pd.melt(df, value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'], id_vars='cardio')
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    fig = sns.catplot(x='variable', hue='value', col='cardio', data=df_cat, kind='count')
    return fig

def clean_data(df):
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & 
                 (df['height'] >= df['height'].quantile(0.025)) & 
                 (df['height'] <= df['height'].quantile(0.975)) & 
                 (df['weight'] >= df['weight'].quantile(0.025)) & 
                 (df['weight'] <= df['weight'].quantile(0.975))]
    return df_heat

def draw_heat_map(df):
    corr = df.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', cmap='coolwarm', ax=ax)
    return fig

df = load_data()
df = add_overweight(df)
df = normalize_data(df)
fig = draw_cat_plot(df)
df_heat = clean_data(df)
fig = draw_heat_map(df_heat)
