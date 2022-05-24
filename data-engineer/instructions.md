# Coding challenge Data Engineering Exercise - Python/SQL

Hello! If you are going through this document, we're likely chatting with you about a technical role at Pectus Finance. If so, congratulations 🎉 !

```
TIMEBOX:    2-4 hours max. We mean it! Set at timer and hard-stop at 4 hours ⏱
LANGUAGES:  Python, SQL
FRAMEWORKS: Jupyter
DATASETS: salary_data/**.csv
```

## Overview

This exercise is to evaluate real-world compensation data. This is **NOT** a test of how well you know [Jupyter](https://jupyter.org/)/Python/SQL, nor should you try to impress us with overly clever and obtuse analysis. If you want to impress us, use the time allotted to extract the maximum value from the data possible.

Submissions should be in the form of a [Jupyter notebook](https://jupyter.org/). However, you are free to write custom SQL queries or functions if that better fits your work style. Ideally, your solution would have some way to run locally and test the results so we can thoroughly analyze your efforts.

## Exercise

---

This exercise aims to analyze a data set containing several CSVs of compensation data submitted by individuals via Employee Survey tools. This data has not been modified in any way from the original source.

- Clean and format all [3 compensation data CSVs](/salary_datasets) to use a common set of fields/attributes/columns containing at least the following...
  - title
  - location
  - salary (base compensation) in $US dollars with cents
  - years experience
  - bonus
- Validate that you can perform the following analyses and export the results via [Jupyter notebook](https://jupyter.org/), a CSV or attach screenshots of the the output
  - **Compensation by Role**
    - Find the average compensation of roles where the role is some kind of technical professional
    - Visualize the relationship between compensation and role
  - **Compensation by Geographic Region**
    - Average, min, and max compensation per city/region
    - Visualize the relationship between city and salary/base compensation
  - **Compensation by Experience**
    - Visualize the relationship between cash compensation and other forms of compensation
  - Visualize One interesting query/facet of your choice (_average compensation by gender perhaps???_)

---

### Be sure to include the following in your submission

- a README.md with the following information
  - A few screenshots of the finished product. Show off that work! 📸
  - A short explanation of what you built
- How to run/test/demo (if applicable)
  - Any feedback/notes (i.e., if something was challenging, confusing, frustrating, etc.)
- Is anything else you'd like us to know about your submission
- a WISHLIST.md with what you would add/change if you had more time. #DreamBig #NeverSettle.
- Some form of lightweight technical documentation (code comments are fine)

## Submitting your exercise

- Please send your task solutions GitHub repository link to nishant@pectusfinance.com.
- If you have any questions related to this coding challenge, please write to Nishant /He/Him (nishant@pectusfinance.com)

Sit back and relax. We'll review your submission and get back to you within 72 hours 😃
