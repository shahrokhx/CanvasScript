'''
A simple script to upload grades and comments to Canvas
Developed by Shahrokh Shahi
CSE6140-Fall2020
School of Computational Science and Engineering
Georgia Tech

Note:
- Before running the script, double-check and update the information in config.json if needed 
(the assignment id, excel_file_name, etc.) 

'''

import csv
import json
import requests
import argparse
import xlrd


HOST = "gatech.instructure.com"
base_url = 'https://{}/api/v1/courses'.format(HOST)

json_config = "config.json"
with open(json_config) as json_data_file:
    configuration = json.load(json_data_file)
    access_token  = configuration['access_token']
    course_id     = configuration['course_id']  
    assignment_id = configuration['assignment_id']
    excel_file    = configuration['excel_file']
    excel_sheet   = configuration['excel_sheet']

xlsx_workbook  = xlrd.open_workbook(excel_file) 
xlsx_sheet = xlsx_workbook.sheet_by_name(excel_sheet)
# count from left to right, starting from zero
# A B C D E F G H I 
# 0 1 2 3 4 5 6 7 8
#   ^ ^       ^ ^
all_grades = []
for row_idx in range(2, xlsx_sheet.nrows):
    name    = xlsx_sheet.cell(row_idx, 1).value
    id      = xlsx_sheet.cell(row_idx, 2).value
    grade   = xlsx_sheet.cell(row_idx, 6).value
    comment = xlsx_sheet.cell(row_idx, 7).value
	
    if id == '':
        id = 0
        comment = 'Audit'
    else:
        id = int(id)

    all_grades.append((name,id,grade,comment))



url = '{}/{}/assignments/{}'.format(base_url, course_id, assignment_id)
header = {'Authorization': 'Bearer ' + access_token}


def assign_grade_for_assignment(base_url, header, user_id, grade, comment, verbose=False):
    # Use the Canvas API to assign a grade for an assignment
    # PUT /api/v1/courses/:course_id/assignments/:assignment_id/submissions/:user_id

    # Request Parameters:
    # comment[text_comment]		string	Add a textual comment to the submission.
    # submission[posted_grade]		string	Assign a score to the submission, updating both the "score" and "grade" fields on the submission record. This parameter can be passed in a few different formats:
    
    url = '{}/submissions/{}'.format(base_url, user_id)
    if verbose:
       print('url: ' + url)

    payload = {'submission[posted_grade]': grade}
    if comment:
        payload.update({'comment[text_comment]': comment})

    r = requests.put(url, headers=header, data=payload)

    if verbose:
        print('result of put assign_grade_for_assignment:', r.text)
    if r.status_code == requests.codes.ok:
        page_response = r.json()
        return True
    return False


counter = 1
for name, user_id, grade, comment in all_grades:
    print ("NUMBER = ", counter)
    # print (name, user_id, grade, comment)   
       
    # uploading grades
    if True:
        if assign_grade_for_assignment(url, header, user_id, grade, comment, False):
            print('Successfully uploaded grade for \'{}\''.format(name))
        else:
            print('Failed to upload grade for \'{}\''.format(name))
            print (name, user_id, grade, comment) 

    print ("-----------------------------------------------") 
    counter += 1
    
    