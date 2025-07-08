#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:52:03 2024

@author: ijeong-yeon
"""

import bodhi_indicator as bd
import bodhi_PMF as pmf
import pandas as pd

"""
Evaluation
"""
# Specify the file path for the clean dataset
df = pd.read_excel('data/25-IOM-SD-1 - Clean Data.xlsx')

# Create indicators and provide additional details as needed (Evaluation)
def statistics(df, indicators):
    region = bd.Indicator(df, "Region", 0, ['1'], i_cal=None, i_type='count', description='Region distribution', period='endline', target = None, visual=False)
    region.add_var_order(['Al Rahmaniya', 'Kadugli'])
    indicators.append(region)
    
    age = bd.Indicator(df, "Age group", 0, ['3'], i_cal=None, i_type='count', description='Age group distribution', period='endline', target = None)
    age.add_var_order(["Under 18",
                       "18–24",
                       "25–34",
                       "35–44",
                       "45–59",
                       "60 and above"])
    indicators.append(age)
    
    gender = bd.Indicator(df, "Gender", 0, ['4'], i_cal=None, i_type='count', description='Gender distribution', period='endline', target = None)
    gender.add_var_order(['Female', 'Male'])
    indicators.append(gender)
    
    education = bd.Indicator(df, "Education", 0, ['5'], i_cal=None, i_type='count', description="Respondents' education", period='endline', target = None, visual=False)
    education.add_var_order(["No formal education",
                             "Some primary education",
                             "Completed primary education",
                             "Some secondary education",
                             "Completed secondary education",
                             "Post-secondary/technical/vocational training",
                             "University degree or higher"])
    indicators.append(education)
    
    job = bd.Indicator(df, "Occupation", 0, ['6-1', '6-2', '6-3', '6-4', '6-5', '6-6', '6-7', '6-8'], i_cal=None, i_type='count', description='What is your current occupation?', period='endline', target = None)
    job.add_breakdown({'2':'Gender'})
    job.add_label(["Farming/livestock",
                   "Small business/trade",
                   "Daily labor",
                   "Formal employment",
                   "No income",
                   "Student",
                   "Homemaker",
                   "Other"])
    indicators.append(job)
    
    relationship = bd.Indicator(df, "Relationship", 0, ['7'], i_cal=None, i_type='count', description="What is your relationship status?", period='endline', target = None, visual=False)
    relationship.add_var_order(["Currently married",
                                "Single (never married)",
                                "Divorced",
                                "Widowed",
                                "Prefer not to say",
                                "Other"])
    indicators.append(relationship)
    
    r_type = bd.Indicator(df, "Respondent Type", 0, ['9'], i_cal=None, i_type='count', description="What is your status in this community?", period='endline', target = None, visual=False)
    r_type.add_var_order(["Internally Displaced Person (IDP)",
                                "Returnee",
                                "Member of the Host Community"])
    indicators.append(r_type)
    
    disability = bd.Indicator(df, "Disability", 0, ['Disability'], i_cal=None, i_type='count', description='Disability status', period='endline', target = None)
    disability.add_var_order(['No Disability', 'Disability'])
    indicators.append(disability)
    
    # Relevance
    r_1 = bd.Indicator(df, "Involved_project", 0, ['16'], i_cal=None, i_type='count', description='Which project activities were you involved in?', period='endline', target = None, visual=False)
    r_1.add_breakdown({'4':'Gender', '3':'Age Group', "Disability":"Disability"})
    r_1.add_var_order(["Received livestock or agricultural support",
                       "Received transportation tools (e.g., donkey carts, wheelbarrows)",
                       "Received in-kind food assistance",
                       "Participated in livelihoods or business training",
                       "Received support to start or strengthen a small business",
                       "Received hygiene kits or participated in hygiene promotion activities",
                       "Benefited from improved access to clean water (e.g., boreholes, water points)",
                       "Used new or improved latrines/sanitation facilities",
                       "Attended explosive ordnance risk education sessions",
                       "Received health services or visited mobile health clinics",
                       "Participated in peacebuilding or social cohesion activities",
                       "Attended training on sewing, food processing, cheese-making, or blacksmithing/welding",
                       "Used or benefited from the new slaughterhouse built in the community",
                       "Other (please specify): ____________"])
    indicators.append(r_1)
    
    r_2 = bd.Indicator(df, "Top_project", 0, ['17-1'], i_cal=None, i_type='count', description="[Top1] Of the project activities you were involved in, which was most useful?", period='endline', target = None, visual=False)
    r_2.add_breakdown({'4':'Gender', '3':'Age Group', "Disability":"Disability"})
    r_2.add_var_order(["Received livestock or agricultural support",
                       "Received transportation tools (e.g., donkey carts, wheelbarrows)",
                       "Received in-kind food assistance",
                       "Participated in livelihoods or business training",
                       "Received support to start or strengthen a small business",
                       "Received hygiene kits or participated in hygiene promotion activities",
                       "Benefited from improved access to clean water (e.g., boreholes, water points)",
                       "Used new or improved latrines/sanitation facilities",
                       "Attended explosive ordnance risk education sessions",
                       "Received health services or visited mobile health clinics",
                       "Participated in peacebuilding or social cohesion activities",
                       "Other (please specify): ____________"])
    indicators.append(r_2)  
    
    r_3 = bd.Indicator(df, "Project_relevance", 0, ['18'], i_cal=None, i_type='count', description="Do you believe that project activities were relevant to the needs of you and your community?", period='endline', target = None, visual=False)
    r_3.add_breakdown({'4':'Gender', '3':'Age Group', "Disability":"Disability"})
    r_3.add_var_order(["Yes, completely",
                       "Mostly",
                       "Somewhat",
                       "Not really",
                       "Not at all"])
    indicators.append(r_3)  
    
    r_4 = bd.Indicator(df, "Women_1", 0, ['20'], i_cal=None, i_type='count', description="Do you feel the programme activities considered the specific needs of women and girls?", period='endline', target = None, visual=False)
    r_4.add_breakdown({'4':'Gender', '3':'Age Group', "Disability":"Disability"})
    r_4.add_var_order(["Yes, completely",
                       "Mostly",
                       "Somewhat",
                       "Not really",
                       "Not at all"])
    indicators.append(r_4)
    
    r_5 = bd.Indicator(df, "Women_2", 0, ['22'], i_cal=None, i_type='count', description="To your knowledge, did the programme offer any activities or support specifically targeted at women?", period='endline', target = None)
    r_5.add_breakdown({'4':'Gender', '3':'Age Group', "Disability":"Disability"})
    r_5.add_var_order(["Yes",
                       "No",
                       "Unsure"])
    indicators.append(r_5)
    
    r_6 = bd.Indicator(df, "Women_3", 0, ['24'], i_cal=None, i_type='count', description="As a result of the programme, do you feel that women in your community have become more confident or involved in community life?", period='endline', target = None, visual=False)
    r_6.add_breakdown({'4':'Gender', '3':'Age Group', "Disability":"Disability"})
    r_6.add_var_order(["Yes, significantly",
                       "Yes, somewhat",
                       "No change",
                       "Unsure"])
    indicators.append(r_6)
    
    r_7 = bd.Indicator(df, "Youth_1", 0, ['21'], i_cal=None, i_type='count', description="Do you feel the programme activities considered the specific needs of youth?", period='endline', target = None, visual=False)
    r_7.add_breakdown({'4':'Gender', '3':'Age Group', "Disability":"Disability"})
    r_7.add_var_order(["Yes, completely",
                       "Mostly",
                       "Somewhat",
                       "Not really",
                       "Not at all"])
    indicators.append(r_7)
    
    r_8 = bd.Indicator(df, "Youth_2", 0, ['23'], i_cal=None, i_type='count', description="To your knowledge, did the programme offer any activities or support specifically targeted at youth?", period='endline', target = None)
    r_8.add_breakdown({'4':'Gender', '3':'Age Group', "Disability":"Disability"})
    r_8.add_var_order(["Yes",
                       "No",
                       "Unsure"])
    indicators.append(r_8)
    
    r_9 = bd.Indicator(df, "Youth_3", 0, ['25'], i_cal=None, i_type='count', description="As a result of the programme, do you feel that youth in your community have become more confident or involved in community life?", period='endline', target = None, visual=False)
    r_9.add_breakdown({'4':'Gender', '3':'Age Group', "Disability":"Disability"})
    r_9.add_var_order(["Yes, significantly",
                       "Yes, somewhat",
                       "No change",
                       "Unsure"])
    indicators.append(r_9)
    
    # Effectiveness
    ef_1 = bd.Indicator(df, "Effect_WASH", 0, ['26'], i_cal=None, i_type='count', description="Did the programme help your community get better access to clean water, toilets. or hygiene products?", period='endline', target = None, visual=False)
    ef_1.add_breakdown({'4':'Gender', '3':'Age Group', "Disability":"Disability"})
    ef_1.add_var_order(["A lot",
                        "Somewhat",
                        "A little",
                        "Not at all",
                        "Unsure"])
    indicators.append(ef_1)
    
    ef_2 = bd.Indicator(df, "Effect_health", 0, ['27'], i_cal=None, i_type='count', description="Did the programme help your community get better access to health care, clinics, or medicine?", period='endline', target = None, visual=False)
    ef_2.add_breakdown({'4':'Gender', '3':'Age Group', "Disability":"Disability"})
    ef_2.add_var_order(["A lot",
                        "Somewhat",
                        "A little",
                        "Not at all",
                        "Unsure"])
    indicators.append(ef_2)
    
    ef_3 = bd.Indicator(df, "Effect_food", 0, ['28'], i_cal=None, i_type='count', description="Did the programme help your household get enough food or support with food needs?", period='endline', target = None, visual=False)
    ef_3.add_breakdown({'4':'Gender', '3':'Age Group', "Disability":"Disability"})
    ef_3.add_var_order(["A lot",
                        "Somewhat",
                        "A little",
                        "Not at all",
                        "Unsure"])
    indicators.append(ef_3)
    
    ef_4 = bd.Indicator(df, "Effect_money", 0, ['29'], i_cal=None, i_type='count', description="Did the programme help your household earn money or get support for work or small business?", period='endline', target = None, visual=False)
    ef_4.add_breakdown({'4':'Gender', '3':'Age Group', "Disability":"Disability"})
    ef_4.add_var_order(["A lot",
                        "Somewhat",
                        "A little",
                        "Not at all",
                        "Unsure"])
    indicators.append(ef_4)
    
    ef_5 = bd.Indicator(df, "Effect_risk", 0, ['36'], i_cal=None, i_type='count', description="Did you participate in any risk education or awareness activities related to explosive ordnance?", period='endline', target = None)
    ef_5.add_breakdown({'4':'Gender', '3':'Age Group', "Disability":"Disability"})
    ef_5.add_var_order(["Yes",
                        "No",
                        "Unsure"])
    indicators.append(ef_5)
    
    ef_6 = bd.Indicator(df, "Effect_risk2", 0, ['37'], i_cal=None, i_type='count', description="Do you now feel more confident in identifying and avoiding dangerous items as a result?", period='endline', target = None, visual=False)
    ef_6.add_breakdown({'4':'Gender', '3':'Age Group', "Disability":"Disability"})
    ef_6.add_var_order(["Very confident",
                        "Somewhat confident",
                        "Not confident",
                        "Unsure"])
    indicators.append(ef_6)
    
    ef_7 = bd.Indicator(df, "Effect_peace", 0, ['30'], i_cal=None, i_type='count', description="To what extent did the programme support peacebuilding and cooperation among community members?", period='endline', target = None, visual=False)
    ef_7.add_breakdown({'4':'Gender', '3':'Age Group', "Disability":"Disability"})
    ef_7.add_var_order(["A lot",
                        "Somewhat",
                        "A little",
                        "Not at all",
                        "Unsure"])
    indicators.append(ef_7)
    
    ef_8 = bd.Indicator(df, "Effect_security", 0, ['33'], i_cal=None, i_type='count', description="Do you feel that your sense of personal safety and human security has improved as a result of the programme?", period='endline', target = None, visual=False)
    ef_8.add_breakdown({'4':'Gender', '3':'Age Group', "Disability":"Disability"})
    ef_8.add_var_order(["Yes, greatly",
                        "Yes, somewhat",
                        "No change",
                        "No, it has worsened"])
    indicators.append(ef_8)
    
    ef_9 = bd.Indicator(df, "Effect_meeting", 0, ['34'], i_cal=None, i_type='count', description="Have you participated in any community meetings or planning sessions supported by the programme?", period='endline', target = None)
    ef_9.add_breakdown({'4':'Gender', '3':'Age Group', "Disability":"Disability"})
    ef_9.add_var_order(["Yes",
                        "No",
                        "Unsure"])
    indicators.append(ef_9)
    
    ef_10 = bd.Indicator(df, "Effect_factors", 0, ['38'], i_cal=None, i_type='count', description="Did any external factors (other than those in the past two years)\naffect your ability to participate in project activities?", period='endline', target = None)
    ef_10.add_breakdown({'4':'Gender', '3':'Age Group', "Disability":"Disability"})
    ef_10.add_var_order(["Yes",
                        "No",
                        "Unsure"])
    indicators.append(ef_10)
    
    ef_11 = bd.Indicator(df, "Effect_livelihood", 0, ['39'], i_cal=None, i_type='count', description="Has the programme helped you or your household find more chances to earn money or improve your livelihood (like jobs, training, or starting a business)?", period='endline', target = None, visual=False)
    ef_11.add_breakdown({'4':'Gender', '3':'Age Group', "Disability":"Disability"})
    ef_11.add_var_order(["Completely",
                        "A lot",
                        "Somewhat",
                        "A little",
                        "Not at all"])
    indicators.append(ef_11)
    
    ef_12 = bd.Indicator(df, "Effect_other", 0, ['40'], i_cal=None, i_type='count', description="Has the programme helped you or your household get better access to services or support, like clean water, health care, or tools to meet your own needs?", period='endline', target = None, visual=False)
    ef_12.add_breakdown({'4':'Gender', '3':'Age Group', "Disability":"Disability"})
    ef_12.add_var_order(["Completely",
                        "A lot",
                        "Somewhat",
                        "A little",
                        "Not at all"])
    indicators.append(ef_12)
    
    # Efficiency
    ec_2 = bd.Indicator(df, "Efc_timely", 0, ['41'], i_cal=None, i_type='count', description="Were the support or services you received from the programme (e.g., water, health, livelihoods, EORE) provided when your household needed them most?", period='endline', target = None, visual=False)
    ec_2.add_breakdown({'4':'Gender', '3':'Age Group', "Disability":"Disability"})
    ec_2.add_var_order(["Yes, always on time",
                        "Sometimes delayed",
                        "Often delayed",
                        "I did not receive any support"])
    indicators.append(ec_2)
    
    ec_3 = bd.Indicator(df, "Efc_timely2", 0, ['42'], i_cal=None, i_type='count', description="How would you rate the timeliness of the programme’s activities in your community?", period='endline', target = None)
    ec_3.add_breakdown({'4':'Gender', '3':'Age Group', "Disability":"Disability"})
    ec_3.add_var_order(["Very timely",
                        "Mostly timely",
                        "Frequently delayed",
                        "Not sure"])
    indicators.append(ec_3)
    
    ec_4 = bd.Indicator(df, "Efc_enough", 0, ['43'], i_cal=None, i_type='count', description="In your opinion, were the items or services (e.g., hygiene kits, training, tools, food) provided in sufficient quantities to meet your household’s or community’s needs?", period='endline', target = None, visual=False)
    ec_4.add_breakdown({'4':'Gender', '3':'Age Group', "Disability":"Disability"})
    ec_4.add_var_order(["Yes, fully",
                        "Partially",
                        "No, not at all",
                        "Not applicable"])
    indicators.append(ec_4)
    
    ec_5 = bd.Indicator(df, "Efc_delayed", 0, ['44'], i_cal=None, i_type='count', description="Were any of the workshops, meetings, or training sessions promised by the programme delayed or not conducted as expected?", period='endline', target = None, visual=False)
    ec_5.add_breakdown({'4':'Gender', '3':'Age Group', "Disability":"Disability"})
    ec_5.add_var_order(["Yes, some were delayed",
                        "No, they occurred as planned",
                        "Not sure",
                        "I did not attend any"])
    indicators.append(ec_5)
    
    ec_6 = bd.Indicator(df, "Efc_informed", 0, ['45'], i_cal=None, i_type='count', description="Were you ever informed about changes or delays in planned activities or support?", period='endline', target = None, visual=False)
    ec_6.add_breakdown({'4':'Gender', '3':'Age Group', "Disability":"Disability"})
    ec_6.add_var_order(["Yes, regularly",
                        "Sometimes",
                        "No, never",
                        "Not applicable"])
    indicators.append(ec_6)
    
    # Impact
    im_1 = bd.Indicator(df, "Imp_wellbeing", 0, ['46'], i_cal=None, i_type='count', description="Do you think the programme has made a lasting positive difference in your life or your household’s well-being?", period='endline', target = None, visual=False)
    im_1.add_breakdown({'4':'Gender', '3':'Age Group', "Disability":"Disability"})
    im_1.add_var_order(["Yes, a significant difference",
                        "Yes, a small difference",
                        "No noticeable difference",
                        "Negative impact",
                        "Not sure"])
    indicators.append(im_1)
    
    im_3 = bd.Indicator(df, "Imp_income", 0, ['54'], i_cal=None, i_type='count', description="Have you (or a member of your household) seen an increase in income as a result of the programme?", period='endline', target = None)
    im_3.add_breakdown({'4':'Gender', '3':'Age Group', "Disability":"Disability"})
    im_3.add_var_order(["Yes",
                        "No",
                        "Unsure"])
    indicators.append(im_3)
    
    im_4 = bd.Indicator(df, "Imp_cohesion", 0, ['47'], i_cal=None, i_type='count', description="Do you think the programme has contributed to greater peace, safety, or social cohesion in your community?", period='endline', target = None, visual=False)
    im_4.add_breakdown({'4':'Gender', '3':'Age Group', "Disability":"Disability"})
    im_4.add_var_order(["Yes, a significant difference",
                        "Yes, a small difference",
                        "No noticeable difference",
                        "Negative impact",
                        "Not sure"])
    indicators.append(im_4)
    
    im_5 = bd.Indicator(df, "Imp_handling", 0, ['48'], i_cal=None, i_type='count', description="Has your household become better at handling problems like conflicts, rising prices, or sickness because of the programme?", period='endline', target = None, visual=False)
    im_5.add_breakdown({'4':'Gender', '3':'Age Group', "Disability":"Disability"})
    im_5.add_var_order(["Much better",
                        "A little better",
                        "No change",
                        "A little worse",
                        "A lot worse"])
    indicators.append(im_5)
    
    im_6 = bd.Indicator(df, "Imp_confident", 0, ['50'], i_cal=None, i_type='count', description="Do you feel more confident in supporting your family during hard times because of the programme’s support?", period='endline', target = None, visual=False)
    im_6.add_breakdown({'4':'Gender', '3':'Age Group', "Disability":"Disability"})
    im_6.add_var_order(["Much more able",
                        "A little more able",
                        "No change",
                        "A little less able",
                        "A lot less able"])
    indicators.append(im_6)
    
    im_7 = bd.Indicator(df, "Imp_components", 0, ['52'], i_cal=None, i_type='count', description="Were all the components of the programme (e.g., livelihoods, WASH, health, EORE, peacebuilding) helpful in achieving its goals?", period='endline', target = None, visual=False)
    im_7.add_breakdown({'4':'Gender', '3':'Age Group', "Disability":"Disability"})
    im_7.add_var_order(["Yes, all were helpful",
                        "Some were helpful, others less so",
                        "No, most were not effective",
                        "Not sure"])
    indicators.append(im_7)
    
    im_8 = bd.Indicator(df, "Imp_existing_group", 0, ['51'], i_cal=None, i_type='count', description="Did the programme use or build on existing local groups, peacebuilding efforts, or community knowledge?", period='endline', target = None, visual=False)
    im_8.add_breakdown({'4':'Gender', '3':'Age Group', "Disability":"Disability"})
    im_8.add_var_order(["Yes, strongly",
                        "Yes, somewhat",
                        "No",
                        "Not sure"])
    indicators.append(im_8)
    
    im_9 = bd.Indicator(df, "Imp_project", 0, ['53'], i_cal=None, i_type='count', description="Which parts of the programme made the most difference in your life? (Select all that apply)", period='endline', target = None, visual=False)
    im_9.add_breakdown({'4':'Gender', '3':'Age Group', "Disability":"Disability"})
    im_9.add_var_order(["Livelihoods support",
                        "Clean water or sanitation",
                        "Health services",
                        "Explosive ordnance risk education",
                        "Peacebuilding/social cohesion activities",
                        "None",
                        "Other (please specify): ____________"])
    indicators.append(im_9)
    
    im_10 = bd.Indicator(df, "Imp_unintended", 0, ['49'], i_cal=None, i_type='count', description="Have you or others in your community experienced any unintended consequences from the programme? (e.g., increased tension, unequal support, new risks)", period='endline', target = None, visual=False)
    im_10.add_breakdown({'4':'Gender', '3':'Age Group', "Disability":"Disability"})
    im_10.add_var_order(["Yes, positive (Please Specify______)",
                        "Yes, negative (Please Specify______)",
                        "No",
                        "Not sure"])
    indicators.append(im_10)
    
    # Sustainable
    sus_1 = bd.Indicator(df, "Sus_1", 0, ['56'], i_cal=None, i_type='count', description="Do you think the benefits or changes brought by the programme will continue in your community, even after the programme ends?", period='endline', target = None, visual=False)
    sus_1.add_breakdown({'4':'Gender', '3':'Age Group', "Disability":"Disability"})
    sus_1.add_var_order(["Yes, definitely",
                         "Yes, somewhat",
                         "No",
                         "Not sure"])
    indicators.append(sus_1)
    
    sus_2 = bd.Indicator(df, "Sus_2", 0, ['57'], i_cal=None, i_type='count', description="To your knowledge, are there any community groups, committees, or local leaders\nwho are continuing activities started under the programme?", period='endline', target = None)
    sus_2.add_breakdown({'4':'Gender', '3':'Age Group', "Disability":"Disability"})
    sus_2.add_var_order(["Yes",
                         "No",
                         "Not sure"])
    indicators.append(sus_2)
    
    sus_3 = bd.Indicator(df, "Sus_3", 0, ['58'], i_cal=None, i_type='count', description="Were you or other community members given\ntraining or support to continue activities after the programme ends?", period='endline', target = None)
    sus_3.add_breakdown({'4':'Gender', '3':'Age Group', "Disability":"Disability"})
    sus_3.add_var_order(["Yes",
                         "No",
                         "Not sure"])
    indicators.append(sus_3)
    
    sus_4 = bd.Indicator(df, "Sus_4", 0, ['59'], i_cal=None, i_type='count', description="Do you feel your community now has better knowledge or tools to solve problems without outside help?", period='endline', target = None, visual=False)
    sus_4.add_breakdown({'4':'Gender', '3':'Age Group', "Disability":"Disability"})
    sus_4.add_var_order(["Yes, very confident",
                         "Somewhat confident",
                         "No, still dependent on external help",
                         "Not sure"])
    indicators.append(sus_4)
    
    return indicators
    
    
# Create indicators for several statistical tests such as OLS, ANOVA, T-test and Chi2
def statistical_indicators(df, indicators):
    income = bd.Indicator(df, "Income", 0, ['55'], i_cal=None, i_type='count', description='How much has your income increased?', s_test = 'stats', s_group = {'4':'Gender', '3':'Age Group', "Disability":"Disability"})
    indicators.append(income)
    return indicators

# Create the PMF class ('Project Title', 'Evaluation')
heglig = pmf.PerformanceManagementFramework('Heglig', 'Evaluation')

indicators = []
indicators = statistics(df, indicators)
indicators = statistical_indicators(df, indicators)
heglig.add_indicators(indicators)

file_path1 = 'data/Heglig Statistics.xlsx' # File path to save the statistics (including breakdown data)
file_path2 = 'data/Heglig Test Results.xlsx'  # File path to save the chi2 test results
folder = 'visuals/' # File path for saving visuals
heglig.PMF_generation(file_path1, file_path2, folder) # Run the PMF