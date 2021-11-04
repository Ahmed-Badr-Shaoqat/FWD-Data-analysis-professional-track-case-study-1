import pandas as pd
import numpy as np
import matplotlib as plt

#Assessing Data

#Read csv files with ';' separator
red_df = pd.read_csv('winequality-red.csv', sep = ';')
white_df = pd.read_csv('winequality-white.csv', sep = ';')

#Answering quistions
#How many samples of red wine are there?
#How many samples of white wine are there?
#How many columns are in each dataset?
#Which features have missing values?

red_df.info()
white_df.info()

#How many duplicate rows are in the white wine dataset?
#Are duplicate rows in these datasets significant/ need to be dropped?

sum(white_df.duplicated())

#How many unique values of quality are in the red wine dataset?
#How many unique values of quality are in the white wine dataset?

len(red_df.quality.unique())
len(white_df.quality.unique())

#What is the mean density in the red wine dataset?

red_df.density.mean()

#_____________________________________________________________________________

#Appending Data

#Create color array for red dataframe
color_red = np.repeat("red",len(red_df))

#Create color array for white dataframe
color_white = np.repeat("white", len(white_df))

#Adding the color to each data frame
red_df['color'] = color_red
white_df['color'] = color_white

#Append dataframes
wine_df = red_df.append(white_df, ignore_index=True)

#View dataframe to check for success
wine_df.head()
wine_df.tail()

#Save new dataframe
wine_df.to_csv('winequality_edited.csv', index=False)

#_____________________________________________________________________________

#Appending Data (cont.)

red_df.rename(columns={'total_sulfur-dioxide':'total_sulfur_dioxide'},
inplace=True)
wine_df.to_csv('winequality_edited.csv', index=False)

#_____________________________________________________________________________

#Exploring with Visuals

#Histograms for Various Features
wine_df['fixed_acidity'].plot(kind='hist');
wine_df['total_sulfur_dioxide'].plot(kind='hist');
wine_df['pH'].plot(kind='hist');
wine_df['alcohol'].plot(kind='hist');

#Scatterplots of Quality Against Various Features
wine_df.plot(x='quality', y='volatile_acidity', kind='scatter');
wine_df.plot(x='quality', y='residual_sugar', kind='scatter');
wine_df.plot(x='quality', y='pH', kind='scatter');
wine_df.plot(x='quality', y='alcohol', kind='scatter');
    
#_____________________________________________________________________________

#Conclusions Using Groupby

#Find the mean quality of each wine type (red and white) with groupby
wine_df.groupby(['color']).mean()

#View the min, 25%, 50%, 75%, max pH values with Pandas describe
wine_df.describe()

#Bin edges that will be used to "cut" the data into groups
bin_edges = [2.27, 3.11, 3.21, 3.32, 4.01] # Fill in this list with five values you just found

#Labels for the four acidity level groups
bin_names = ['High', 'Moderately_High', 'Medium', 'Low'] # Name each acidity level category

#Creates acidity_levels column
df['acidity_levels'] = pd.cut(df['pH'], bin_edges, labels=bin_names)

#Checks for successful creation of this column
df.head()
#Find the mean quality of each acidity level with groupby

df.groupby(['acidity_levels']).mean()

#Save changes for the next section
df.to_csv('winequality_edited.csv', index=False)

#_____________________________________________________________________________

#Conclusions Using Query

#Get the median amount of alcohol content
wine_df['alcohol'].median()

#Select samples with alcohol content less than the median
low_alcohol = wine_df.query('alcohol < 10.3')

#Select samples with alcohol content greater than or equal to the median
high_alcohol = wine_df.query('alcohol >= 10.3')

#Ensure these queries included each sample exactly once
#Print(num_samples)
num_samples = wine_df.shape[0]
num_samples == low_alcohol['quality'].count() + high_alcohol['quality'].count() #Should be True

#Get mean quality rating for the low alcohol and high alcohol groups
low_alcohol.mean()
high_alcohol.mean()

#Do sweeter wines receive better ratings?
#Get the median amount of residual sugar
wine_df['residual_sugar'].median()

#Select samples with residual sugar less than the median
low_sugar = wine_df.query('residual_sugar < 3.0')

#Select samples with residual sugar greater than or equal to the median
high_sugar = wine_df.query('residual_sugar >= 3.0')

#Ensure these queries included each sample exactly once
num_samples == low_sugar['quality'].count() + high_sugar['quality'].count() #Should be True

#Get mean quality rating for the low sugar and high sugar groups
low_sugar.mean()
high_sugar.mean()

#_____________________________________________________________________________

