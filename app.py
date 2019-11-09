import pandas as pd


specs = "data/specs.csv"
test = "data/test.csv"
train = "data/train.csv"
labels = "data/train_labels.csv"

train_df = pd.read_csv(train, nrows=10)
test_df = pd.read_csv(test, nrows=10)
specs_df = pd.read_csv(specs, nrows=100)
labels_df = pd.read_csv(labels, nrows=100)
labels_df2 = pd.read_csv(labels)

# number of installation ID's
len(labels_df2.installation_id.unique())
labels_df2.groupby(by=['installation_id'])[['accuracy', 'accuracy_group']].mean()
labels_df.head()

train_df=pd.read_csv(train)
install_type = train_df.groupby(by=['installation_id', 'type'])
play_attempts = install_type['event_id'].count()
train_df1 = pd.merge(train_df, play_attempts, on=['installation_id', 'type'])
pd.merge(train_df1, labels_df, on=['installation_id', 'game_session'])
print(train_df1.head())
