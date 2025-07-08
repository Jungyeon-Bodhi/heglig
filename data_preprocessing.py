#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 11:18:51 2024

@author: Bodhi Global Analysis (Jungyeon Lee)
"""

"""
Please define the parameters for data preprocessing pipeline
"""
import bodhi_data_preprocessing as dp

project_name = "IOM - Final External Evaluation"

file_type = 'xlsx' 
# Original data format: xlsx, xls, csv

file_path = "Data/25-IOM-SD-1 - Raw Data"
# Original data location and name (excluding file extension): "Data/(name)"

file_path_others = "Data/25-IOM-SD-1 - Open-End.xlsx"
# Specify the path and name of the Excel sheet where the values from the open-ended columns will be saved (New file)
# For example: "Data/(project name) others.xlsx"

enumerator_name = '60'
respondent_name = None
# Original column name for respondents' names (for anonymisation and duplicate removal)

identifiers = [enumerator_name, '1', '2', '3', '4','5','7','10','11','12','13','14','15','_uuid']
# Identifiers for detecting duplicates (list, do not remove respondent_name)
# Recommendation: At least three identifiers

dates = [] 
# Remove the dates on which the pilot test was conducted from the data
# for example ['2024-07-18', '2024-07-22', '2024-07-23']

cols_new = ['1', '1-o', '2', '3', '4', '5', '6a', '6-1', '6-2', '6-3', '6-4', '6-5', '6-6', '6-7', '6-8', '6-o',
 '7', '8', '9', '9-o', '10', '11', '12', '13', '14', '15', '16', '16-o', '17', '17-1', '17-2', '17-3',
 '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '32-o',
 '33', '34', '35', '36', '37', '38', '38-o', '39', '40', '41', '42', '43', '44', '45', '46', '47',
 '48', '49', '49-n', '49-p', '50', '51', '52', '53', '53-o', '54', '55', '56', '57', '58','59',
 '60', 'omit1', 'omit2', '_id', '_uuid', '_submission_time', '_validation_status', '_notes', '_status', '_submitted_by', '__version__', '_tags', '_index']
# Specify new column names for data analysis (ensure they match the exact order of the existing columns)

list_del_cols = ['6a', '17', 'omit1','omit2','_id','_uuid','_submission_time','_validation_status',
 '_notes','_status','_submitted_by','__version__', '_tags','_index']
# Specify the columns to be excluded from the data analysis

miss_col = ['1','3','4','5','7','10','11','12','13','14','15']
# Specify all columns that apply to all respondents for missing value detection

open_cols = ['1-o', '2', '6-o','9-o','16-o','32-o','38-o','49-n','49-p','53-o',]
# Specify the open-ended columns (which will be saved in a separate Excel sheet and removed from the data frame)

age_col = None
# If we don't have age group in this dataset, please specify the age columns (as str)

diss_cols = ['10','11','12','13','14','15']
# If we have WG-SS questions in the dataset, please specify the columns (as list [])


"""
Run the pipeline for data preprocessing
del_type = 0 or 1
-> 0: Remove all missing values from the columns where missing values are detected
-> 1: First, remove columns where missing values make up 10% or more of the total data points
      Then, remove all remaining missing values from the columns where they are detected
"""

heglig = dp.Preprocessing(project_name, file_path, file_path_others, list_del_cols, dates, miss_col, respondent_name, enumerator_name, identifiers, open_cols, cols_new, age_col, diss_cols, del_type = 0, file_type=file_type)
heglig.processing()
