#load in merge file
from sklearn.preprocessing import StandardScaler


def unique_id(pollutant_merge):
    #gives unique id
    pollutant_merge = pollutant_merge.copy()
    pollutant_merge['id'] = range(1, len(pollutant_merge) + 1)
    # moves 'id' column to the front
    cols = ['id'] + [col for col in pollutant_merge.columns if col != 'id']
    pollutant_merge = pollutant_merge[cols]
    return pollutant_merge

def missing_value(pollutant_merge):
    #drops rows with missing values
    pollutant_merge = pollutant_merge.copy()
    pollutant_merge - pollutant_merge.dropna()
    return pollutant_merge

def outliers(pollutant_merge):
    #drops outliers
    q1 = pollutant_merge['pm2.5'].quantile(0.25)
    q3 = pollutant_merge['pm2.5'].quantile(0.75)
    iqr = q3 - q1
    pollutant_merge = pollutant_merge[(pollutant_merge['pm2.5'] >= q1 - 1.5 * iqr) & (pollutant_merge['pm2.5'] <= q3 + 1.5 * iqr)]
    return pollutant_merge

def normalization(pollutant_merge):
    scaler = StandardScaler()
    merged[['pm2.5', 'temperature']] = scaler.fit_transform(merged[['pm2.5', 'temperature']])






