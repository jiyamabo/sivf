# Description

A simple code base to automate processing students' grades. Initially, I built this for temporary/personal use - pending when institutional funding provides an enterprise solution.

## Use case

Mainly, the application takes numeric values from .csv files as raw input (e.g., 98.23, 75.74, 62.19, ..., 50.11, 17.95) and returns processed .csvs with correctly assigned letter grades (e.g., A+, B, C-, ..., D, F). 

The application has a niche use case. That is, users (e.g., faculty) who have to manually trace which letter grade corresponds to which numeric grade per student, course, section, term, etc. Research from several fields with strong empirical support indicate that such manual processes have a high probability to create errors (e.g., cognitive psychology, HCI). Users at educational institutions with solutions that completely automate data processing will mostly likely not find this useful.

Depending on the user, adopting the code base may include the following steps:

- Create a "data" directory. I suggest using a directory structure similar to the one below:

.
├── processed
│   └── winter-2026
│       └── finals
│           └── bus-239b
└── raw
    └── winter-2026
        └── finals
            ├── bus-111a
            ├── bus-111e
            └── bus-239b


- Create new modules in the "processing" directory. The objective is to ensure each module is customised to process data exported from external applications (e.g., LMS), as data fields from such applications may differ from the default.
- Update `main.py` to include filename(s) for the newly created module.
- Update `run.sh` to run at preferred intervals (optional).

## Final notes

1. **Grading scheme**: Users may need to update the grading scheme, to match institutional specifications. 
2. **Grading scale**: The code base is not robust for final grades not on a 100-point scale. 