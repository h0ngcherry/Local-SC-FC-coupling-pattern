# A counterfactual explanation model for local SC-FC coupling patterns based on the DiCE framework
# import DiCE
import dice_ml
from dice_ml.utils import helpers
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

dataset = pd.read_csv('G:\\test_coupling.csv')

d = dice_ml.Data(dataframe=dataset, continuous_features=['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
                                                         'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
                                                         'nineteen'], outcome_name='label') # ,'nineteen', 'twenty', 'twentyone', 'twentytwo', 'twentythree', 'twentyfour', 'twentyfive'

target = dataset["label"]
# Split data into train and test
datasetX = dataset.drop("label", axis=1)
x_train, x_test, y_train, y_test = train_test_split(datasetX,
                                                    target,
                                                    test_size=0.2,
                                                    random_state=0,
                                                    stratify=target)

numerical = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
             "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
             "eighteen", "nineteen"] #, "nineteen", "twenty", "twentyone", "twentytwo", "twentythree", "twentyfour", "twentyfive"
categorical = x_train.columns.difference(numerical)

# We create the preprocessing pipelines for both numeric and categorical data.
numeric_transformer = Pipeline(steps=[
    ('scaler', StandardScaler())])

categorical_transformer = Pipeline(steps=[
    ('onehot', OneHotEncoder(handle_unknown='ignore'))])
transformations = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numerical),
        ('cat', categorical_transformer, categorical)])

clf = Pipeline(steps=[('preprocessor', transformations),
                      ('classifier', RandomForestClassifier())])
model = clf.fit(x_train, y_train)

backend = 'sklearn'
m = dice_ml.Model(model=model, backend=backend)

# initiate DiCE
exp_random = dice_ml.Dice(d, m, method="random")
indices_label_0 = y_test[y_test == 1].index
query_instances = x_test.loc[indices_label_0]

query_instances_with_index = query_instances.copy()
query_instances_with_index['index'] = query_instances_with_index.index
query_instances_with_index.to_csv('SC-FC.csv', index=False)

dice_exp_random = exp_random.generate_counterfactuals(query_instances, total_CFs=5, desired_class=0, verbose=False)

dice_exp_random.visualize_as_dataframe(show_only_changes=True)
for i, cf_example in enumerate(dice_exp_random.cf_examples_list):
    file_path = r'G:\counterfactuals_{}.csv'.format(i)
    cf_example.final_cfs_df.to_csv(file_path, index=False)

# # Save generated counterfactual examples to disk
#(1) dice_exp_random.cf_examples_list[0].final_cfs_df.to_csv(path_or_buf='counterfactuals0.csv', index=False)
#(2)for i, cf_example in enumerate(dice_exp_random.cf_examples_list):
#     file_path = r'G:\counterfactuals_{}.csv'.format(i)
#     cf_example.final_cfs_df.to_csv(file_path, index=False)




