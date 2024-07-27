import pandas as pd

def analyze_demographic_data():
    df = pd.read_csv('adult.data.csv')

    race_counts = df['race'].value_counts()

    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    percentage_bachelors = round(df['education'].value_counts(normalize=True)['Bachelors'] * 100, 1)

    advanced_education = df[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')]
    percentage_advanced_high_earners = round(advanced_education['salary'].value_counts(normalize=True)['>50K'] * 100, 1)

    no_advanced_education = df[~((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate'))]
    percentage_no_advanced_high_earners = round(no_advanced_education['salary'].value_counts(normalize=True)['>50K'] * 100, 1)

    min_hours = df['hours-per-week'].min()

    min_hours_high_earners = df[(df['hours-per-week'] == min_hours) & (df['salary'] == '>50K')]
    percentage_min_hours_high_earners = round(min_hours_high_earners.shape[0] / df[df['hours-per-week'] == min_hours].shape[0] * 100, 1)

    country_high_earners = df[df['salary'] == '>50K']['native-country'].value_counts(normalize=True)
    highest_earning_country = country_high_earners.idxmax()
    highest_earning_country_percentage = round(country_high_earners.max() * 100, 1)

    india_high_earners = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]
    most_popular_occupation = india_high_earners['occupation'].value_counts().idxmax()

    return {
        'race_counts': race_counts,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'percentage_advanced_high_earners': percentage_advanced_high_earners,
        'percentage_no_advanced_high_earners': percentage_no_advanced_high_earners,
        'min_hours': min_hours,
        'percentage_min_hours_high_earners': percentage_min_hours_high_earners,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'most_popular_occupation': most_popular_occupation
    }

print(analyze_demographic_data())
