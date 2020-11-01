## SECTION 1 : PROJECT TITLE
## Laptop Recommendation System

<img src="SystemCode\laptopbackendv40\pages/read1.jpg"
     style="float: left; margin-right: 0px;" />

---

## SECTION 2 : EXECUTIVE SUMMARY / PAPER ABSTRACT

The computer has been the 21st century and work and learning inseparable, closely related tools. The requirement of replacing the computer is long-term, because of the iteration of the hardware, the iteration of computer products, and the complexity of software, the requirement of computer configuration is also improving. We chose an application scenario to think about, that is, freshmen buy computers. But can students choose their laptops correctly? As we know, computer configuration is mainly CPU, graphics card, hard disk, and then some features such as screen, keyboard, interface, design, and so on. But computers at the same price often have different priorities, and how to make decisions that are more in line with their needs after budgeting is a difficult problem for those who have little knowledge of computers. There is also a problem, even people familiar with computers, it is difficult to identify their needs and make smarter decisions.


We want to solve this problem, so we plan to build a computer-based recommendation system. We crawled the computer notebook data from the http://www.zol.com.cn, cleaned and deleted the data, and SQLitE3 established the computer information database. We used vue.js + vuetify.js UI for the front end design.


We use vue.js as a page building framework, and adopt a vuetify.js UI framework, save time for page structure design and UI design, fast implementation of a simple multi-page APP. Including language switching, questionnaire filling, output, and other functions... (currently used locally in vue.js app), parse rule files using a self-developed rule engine (python). txt) Build a rule base from user preference settings to laptop configuration. Backstage uses Flask framework to build interfaces, Using python post method to resolve user preference data sent back by the front end, And derived preference information by the rule engine, Get the laptop recommended configuration list. After matching through a background SQL - based matching system, Returns the details of several computers with the highest matching score to the front end in JSON format.

Our team works very happily on this project and hopes that the project can be used and feedback by users. This project can become more international, if we can find a more standardized notebook computer shopping site, enrich the database, Maybe we can identify the differences in more goods and recommend them to users more accurately.

---

## SECTION 3 : CREDITS / PROJECT CONTRIBUTION

| Official Full Name  | Student ID (MTech Applicable)  | Work Items (Who Did What) | Email (Optional) |
| :------------ |:---------------:| :-----| :-----|
| Chen Jiajun | A0215519E | UI Design, Front-end Development, Documentation | chenjiajun@u.nus.edu |
| Li Yuan | A0215499R | Responsible for Back-end, Database (Flask and SQLite3) and the Rule-based model making | e0535589@u.nus.edu |
| Wang Ding | A0216421U | Data Clawing, Market Research, Control the product design, Video Documentation/Presentation | e0539414@u.nus.edu |
| Zuo Zhen           | A0215464H | Rule Engine Development and build core code of backend | e0535554@u.nus.edu |

---

## SECTION 4 : VIDEO OF SYSTEM MODELLING & USE CASE DEMO

<img src="SystemCode\laptopbackendv40\pages/read2.jpg"
     style="float: left; margin-right: 0px;" />

---

## SECTION 5 : USER GUIDE

### [ 1 ] Environment Requirement (pip command)

> pip install pandas
>
> pip install flask_cor
>
> pip install flask
>
> pip install numpy
>
> pip install pysqlite3

If you encounter error or warning when execute"pip install pysqlite3",you can install the sqlite3 accroding following step

- go this page https://www.sqlite.org/download.html , and downloads
- download sqlite-tools-win32-*.zip and sqlite-dll-win32-*.zip
- Create the folder C:\sqlite, and decompress the above two compressed files in this folder to get sqlite3.def, sqlite3.dll and sqlite3.exe files
- Add C: \sqlite to the path environment variable. Finally, at the command prompt, use the 'sqlite3' command to display the following results

Congratulation! The environment configuration done!

### [ 2 ] Run the systems on local machine

> python laptopbackendv4.py

Then, click into the 'pages' folder, view 'index.html' in your browser. And begin to choose your laptop!

---
## SECTION 6 : PROJECT REPORT / PAPER

**CONTENTS:**

- 1 EXECUTIVE SUMMARY
- 2 PROBLEM DESCRIPTION
	- 2.1 PROJECT OBJECTIVE
- 3 KNOWLEDGE MODELING
  - 3.1 KNOWLEDGE IDENTIFICATION
  - 3.2 KNOWLEDGE SPECIFICATION
  - 3.3 KNOWLEDGE ACQUISITION
- 4 SOLUTION OUTLINE
  - 4.1 SYSTEM ARCHITECTURE
  - 4.2 PROJECT SCOPE
  - 4.3 SYSTEM'S FEATURES
  - 4.4 FUTURE IMPROVEMENTS
- Appendix 1: Project Proposal
- Appendix 2: Commercial value
- Appendix 3: Installation and User Guide
- Appendix 4: Use Case
- Appendix 5: Mapped System Functionalities against the knowledge
- Appendix 6: Rule Engine
- Appendix 7: Individual Report – Chen Jiajun
- Appendix 8: Individual Report – Li Yuan
- Appendix 9: Individual Report – Wang Ding
- Appendix 10: Individual Report – Zuo Zhen

---
## SECTION 7 : MISCELLANEOUS

### ZOLlaptop30fixed.csv
* Data base
* Insights derived, which were subsequently used in our system

### Rule.txt

- The rule file for the self-made rule engine

---


