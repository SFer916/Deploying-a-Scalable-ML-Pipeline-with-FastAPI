# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This model was developed in November of 2024. This model's version is 1.0. The data was pulled in 1996 by Barry Becker, and is a subset of data from the 1994 census that was to be used to predict whether income exceeded $50,000 per year. 

Data source citation:
Kohavi, R. (1996). Census Income [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5GP7S.

## Intended Use
The intended users are scholars to learn more about machine learning.

## Evaluation Data
Testing split data is used, utilizing the train_test_split method.

## Training Data
Training split data is used, utilizing the train_test_split method.

## Metrics
_Please include the metrics used and your model's performance on those metrics._

train_model.py:
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872

slice_output.txt:
workclass: ?, Count: 389
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
workclass: Federal-gov, Count: 191
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
workclass: Local-gov, Count: 387
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
workclass: Private, Count: 4,578
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
workclass: Self-emp-inc, Count: 212
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
workclass: Self-emp-not-inc, Count: 498
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
workclass: State-gov, Count: 254
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
workclass: Without-pay, Count: 4
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
education: 10th, Count: 183
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
education: 11th, Count: 225
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
education: 12th, Count: 98
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
education: 1st-4th, Count: 23
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
education: 5th-6th, Count: 62
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
education: 7th-8th, Count: 141
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
education: 9th, Count: 115
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
education: Assoc-acdm, Count: 198
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
education: Assoc-voc, Count: 273
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
education: Bachelors, Count: 1,053
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
education: Doctorate, Count: 77
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
education: HS-grad, Count: 2,085
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
education: Masters, Count: 369
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
education: Preschool, Count: 10
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
education: Prof-school, Count: 116
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
education: Some-college, Count: 1,485
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
marital-status: Divorced, Count: 920
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
marital-status: Married-AF-spouse, Count: 4
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
marital-status: Married-civ-spouse, Count: 2,950
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
marital-status: Married-spouse-absent, Count: 96
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
marital-status: Never-married, Count: 2,126
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
marital-status: Separated, Count: 209
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
marital-status: Widowed, Count: 208
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
occupation: ?, Count: 389
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
occupation: Adm-clerical, Count: 726
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
occupation: Armed-Forces, Count: 3
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
occupation: Craft-repair, Count: 821
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
occupation: Exec-managerial, Count: 838
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
occupation: Farming-fishing, Count: 193
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
occupation: Handlers-cleaners, Count: 273
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
occupation: Machine-op-inspct, Count: 378
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
occupation: Other-service, Count: 667
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
occupation: Priv-house-serv, Count: 26
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
occupation: Prof-specialty, Count: 828
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
occupation: Protective-serv, Count: 136
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
occupation: Sales, Count: 729
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
occupation: Tech-support, Count: 189
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
occupation: Transport-moving, Count: 317
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
relationship: Husband, Count: 2,590
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
relationship: Not-in-family, Count: 1,702
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
relationship: Other-relative, Count: 178
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
relationship: Own-child, Count: 1,019
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
relationship: Unmarried, Count: 702
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
relationship: Wife, Count: 322
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
race: Amer-Indian-Eskimo, Count: 71
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
race: Asian-Pac-Islander, Count: 193
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
race: Black, Count: 599
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
race: Other, Count: 55
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
race: White, Count: 5,595
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
sex: Female, Count: 2,126
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
sex: Male, Count: 4,387
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
native-country: ?, Count: 125
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
native-country: Cambodia, Count: 3
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
native-country: Canada, Count: 22
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
native-country: China, Count: 18
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
native-country: Columbia, Count: 6
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
native-country: Cuba, Count: 19
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
native-country: Dominican-Republic, Count: 8
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
native-country: Ecuador, Count: 5
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
native-country: El-Salvador, Count: 20
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
native-country: England, Count: 14
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
native-country: France, Count: 5
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
native-country: Germany, Count: 32
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
native-country: Greece, Count: 7
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
native-country: Guatemala, Count: 13
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
native-country: Haiti, Count: 6
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
native-country: Honduras, Count: 4
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
native-country: Hong, Count: 8
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
native-country: Hungary, Count: 3
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
native-country: India, Count: 21
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
native-country: Iran, Count: 12
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
native-country: Ireland, Count: 5
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
native-country: Italy, Count: 14
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
native-country: Jamaica, Count: 13
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
native-country: Japan, Count: 11
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
native-country: Laos, Count: 4
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
native-country: Mexico, Count: 114
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
native-country: Nicaragua, Count: 7
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
native-country: Peru, Count: 5
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
native-country: Philippines, Count: 35
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
native-country: Poland, Count: 14
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
native-country: Portugal, Count: 6
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
native-country: Puerto-Rico, Count: 22
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
native-country: Scotland, Count: 3
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
native-country: South, Count: 13
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
native-country: Taiwan, Count: 11
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
native-country: Thailand, Count: 5
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
native-country: Trinadad&Tobago, Count: 3
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
native-country: United-States, Count: 5,870
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
native-country: Vietnam, Count: 5
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
native-country: Yugoslavia, Count: 2
Precision: 0.7519 | Recall: 0.6289 | F1: 0.6849
workclass: ?, Count: 389
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
workclass: Federal-gov, Count: 191
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
workclass: Local-gov, Count: 387
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
workclass: Private, Count: 4,578
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
workclass: Self-emp-inc, Count: 212
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
workclass: Self-emp-not-inc, Count: 498
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
workclass: State-gov, Count: 254
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
workclass: Without-pay, Count: 4
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
education: 10th, Count: 183
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
education: 11th, Count: 225
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
education: 12th, Count: 98
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
education: 1st-4th, Count: 23
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
education: 5th-6th, Count: 62
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
education: 7th-8th, Count: 141
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
education: 9th, Count: 115
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
education: Assoc-acdm, Count: 198
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
education: Assoc-voc, Count: 273
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
education: Bachelors, Count: 1,053
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
education: Doctorate, Count: 77
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
education: HS-grad, Count: 2,085
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
education: Masters, Count: 369
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
education: Preschool, Count: 10
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
education: Prof-school, Count: 116
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
education: Some-college, Count: 1,485
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
marital-status: Divorced, Count: 920
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
marital-status: Married-AF-spouse, Count: 4
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
marital-status: Married-civ-spouse, Count: 2,950
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
marital-status: Married-spouse-absent, Count: 96
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
marital-status: Never-married, Count: 2,126
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
marital-status: Separated, Count: 209
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
marital-status: Widowed, Count: 208
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
occupation: ?, Count: 389
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
occupation: Adm-clerical, Count: 726
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
occupation: Armed-Forces, Count: 3
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
occupation: Craft-repair, Count: 821
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
occupation: Exec-managerial, Count: 838
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
occupation: Farming-fishing, Count: 193
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
occupation: Handlers-cleaners, Count: 273
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
occupation: Machine-op-inspct, Count: 378
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
occupation: Other-service, Count: 667
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
occupation: Priv-house-serv, Count: 26
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
occupation: Prof-specialty, Count: 828
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
occupation: Protective-serv, Count: 136
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
occupation: Sales, Count: 729
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
occupation: Tech-support, Count: 189
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
occupation: Transport-moving, Count: 317
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
relationship: Husband, Count: 2,590
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
relationship: Not-in-family, Count: 1,702
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
relationship: Other-relative, Count: 178
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
relationship: Own-child, Count: 1,019
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
relationship: Unmarried, Count: 702
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
relationship: Wife, Count: 322
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
race: Amer-Indian-Eskimo, Count: 71
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
race: Asian-Pac-Islander, Count: 193
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
race: Black, Count: 599
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
race: Other, Count: 55
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
race: White, Count: 5,595
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
sex: Female, Count: 2,126
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
sex: Male, Count: 4,387
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
native-country: ?, Count: 125
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
native-country: Cambodia, Count: 3
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
native-country: Canada, Count: 22
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
native-country: China, Count: 18
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
native-country: Columbia, Count: 6
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
native-country: Cuba, Count: 19
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
native-country: Dominican-Republic, Count: 8
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
native-country: Ecuador, Count: 5
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
native-country: El-Salvador, Count: 20
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
native-country: England, Count: 14
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
native-country: France, Count: 5
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
native-country: Germany, Count: 32
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
native-country: Greece, Count: 7
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
native-country: Guatemala, Count: 13
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
native-country: Haiti, Count: 6
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
native-country: Honduras, Count: 4
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
native-country: Hong, Count: 8
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
native-country: Hungary, Count: 3
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
native-country: India, Count: 21
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
native-country: Iran, Count: 12
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
native-country: Ireland, Count: 5
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
native-country: Italy, Count: 14
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
native-country: Jamaica, Count: 13
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
native-country: Japan, Count: 11
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
native-country: Laos, Count: 4
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
native-country: Mexico, Count: 114
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
native-country: Nicaragua, Count: 7
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
native-country: Peru, Count: 5
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
native-country: Philippines, Count: 35
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
native-country: Poland, Count: 14
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
native-country: Portugal, Count: 6
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
native-country: Puerto-Rico, Count: 22
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
native-country: Scotland, Count: 3
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
native-country: South, Count: 13
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
native-country: Taiwan, Count: 11
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
native-country: Thailand, Count: 5
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
native-country: Trinadad&Tobago, Count: 3
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
native-country: United-States, Count: 5,870
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
native-country: Vietnam, Count: 5
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
native-country: Yugoslavia, Count: 2
Precision: 0.7470 | Recall: 0.6353 | F1: 0.6866
workclass: ?, Count: 389
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
workclass: Federal-gov, Count: 191
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
workclass: Local-gov, Count: 387
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
workclass: Private, Count: 4,578
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
workclass: Self-emp-inc, Count: 212
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
workclass: Self-emp-not-inc, Count: 498
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
workclass: State-gov, Count: 254
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
workclass: Without-pay, Count: 4
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
education: 10th, Count: 183
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
education: 11th, Count: 225
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
education: 12th, Count: 98
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
education: 1st-4th, Count: 23
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
education: 5th-6th, Count: 62
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
education: 7th-8th, Count: 141
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
education: 9th, Count: 115
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
education: Assoc-acdm, Count: 198
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
education: Assoc-voc, Count: 273
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
education: Bachelors, Count: 1,053
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
education: Doctorate, Count: 77
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
education: HS-grad, Count: 2,085
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
education: Masters, Count: 369
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
education: Preschool, Count: 10
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
education: Prof-school, Count: 116
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
education: Some-college, Count: 1,485
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
marital-status: Divorced, Count: 920
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
marital-status: Married-AF-spouse, Count: 4
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
marital-status: Married-civ-spouse, Count: 2,950
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
marital-status: Married-spouse-absent, Count: 96
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
marital-status: Never-married, Count: 2,126
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
marital-status: Separated, Count: 209
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
marital-status: Widowed, Count: 208
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
occupation: ?, Count: 389
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
occupation: Adm-clerical, Count: 726
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
occupation: Armed-Forces, Count: 3
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
occupation: Craft-repair, Count: 821
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
occupation: Exec-managerial, Count: 838
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
occupation: Farming-fishing, Count: 193
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
occupation: Handlers-cleaners, Count: 273
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
occupation: Machine-op-inspct, Count: 378
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
occupation: Other-service, Count: 667
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
occupation: Priv-house-serv, Count: 26
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
occupation: Prof-specialty, Count: 828
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
occupation: Protective-serv, Count: 136
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
occupation: Sales, Count: 729
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
occupation: Tech-support, Count: 189
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
occupation: Transport-moving, Count: 317
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
relationship: Husband, Count: 2,590
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
relationship: Not-in-family, Count: 1,702
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
relationship: Other-relative, Count: 178
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
relationship: Own-child, Count: 1,019
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
relationship: Unmarried, Count: 702
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
relationship: Wife, Count: 322
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
race: Amer-Indian-Eskimo, Count: 71
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
race: Asian-Pac-Islander, Count: 193
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
race: Black, Count: 599
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
race: Other, Count: 55
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
race: White, Count: 5,595
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
sex: Female, Count: 2,126
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
sex: Male, Count: 4,387
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
native-country: ?, Count: 125
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
native-country: Cambodia, Count: 3
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
native-country: Canada, Count: 22
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
native-country: China, Count: 18
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
native-country: Columbia, Count: 6
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
native-country: Cuba, Count: 19
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
native-country: Dominican-Republic, Count: 8
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
native-country: Ecuador, Count: 5
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
native-country: El-Salvador, Count: 20
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
native-country: England, Count: 14
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
native-country: France, Count: 5
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
native-country: Germany, Count: 32
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
native-country: Greece, Count: 7
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
native-country: Guatemala, Count: 13
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
native-country: Haiti, Count: 6
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
native-country: Honduras, Count: 4
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
native-country: Hong, Count: 8
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
native-country: Hungary, Count: 3
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
native-country: India, Count: 21
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
native-country: Iran, Count: 12
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
native-country: Ireland, Count: 5
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
native-country: Italy, Count: 14
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
native-country: Jamaica, Count: 13
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
native-country: Japan, Count: 11
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
native-country: Laos, Count: 4
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
native-country: Mexico, Count: 114
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
native-country: Nicaragua, Count: 7
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
native-country: Peru, Count: 5
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
native-country: Philippines, Count: 35
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
native-country: Poland, Count: 14
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
native-country: Portugal, Count: 6
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
native-country: Puerto-Rico, Count: 22
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
native-country: Scotland, Count: 3
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
native-country: South, Count: 13
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
native-country: Taiwan, Count: 11
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
native-country: Thailand, Count: 5
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
native-country: Trinadad&Tobago, Count: 3
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
native-country: United-States, Count: 5,870
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
native-country: Vietnam, Count: 5
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872
native-country: Yugoslavia, Count: 2
Precision: 0.7432 | Recall: 0.6391 | F1: 0.6872


## Ethical Considerations

There are no immediate ethical considerations with this dataset.

## Caveats and Recommendations

There are missing values in the dataset for the work class and occupation variables which could skew data in these areas. There may also be a lack of representation in some fields in the occupation variable.
