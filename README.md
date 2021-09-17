# CanvasScript
A simple Python script to automatically upload the grades and feedbacks on Canvas.

Prepared by SHAHROKH SHAHI
Georgia Institute of Technology
College of Computing

----

Note 1: The script is intentionally kept simple enough for further developments and manual tweaks. Feel free to do the necessay changes, including OOP design and/or adding a GUI.

Note 2: The provided Excel file is a sample with some dummy names. You need to use the students names and ids from Canvas gradebook list.
----
### Instructions

#### The first time configuration

- Generate a token in the Canvas Account settings:
	Account -> settings -> Approved Integrations -> New Access Token

- Copy your access token into config.json

- Copy the course id into config.json 


#### For each time that you want upload grades/feedbacks

- Download the finalized Grading sheet (e.g. GradersSheet.xlsx) from the sharepoint into the same forder including a copy of the uploader script and config.json

- Do the necessary updates in config.json (exel_file, exel_sheet, and the assignment id)

- Before the next step, you may want to change Grade Posting Policy for the assignment to "Manually", if you don't want grades to be immediately visible to students when posted.

- Run gradeUploader.py
    python3 grade_uploader.py

- If you changed Grade Posting Policy to manual earlier, now you can click "Post grades" from Gradebook