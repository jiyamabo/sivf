# Description

A simple code base to automate processing students' grades. 

## Application

Mainly, the application takes numeric values from .csv files as raw input (e.g., 98.23, 75.74, 62.19, ..., 50.11, 17.95) and returns processed .csvs with correctly assigned letter grades (e.g., A+, B, C-, ..., D, F). 

The application has a niche use case and was built mainly for personal use; that is, users who have to manually trace which letter grade corresponds to which numeric grade per student, course, section, term, etc. Users at institutions with comprehensive enterprise solutions that automates data processing will mostly likely not find this useful.

## Grade scheme

Users may need to update the grading scheme, to match institutional specifications. Note, the code is not robust for grading schemes where final grades are not on a 100-point scale. 