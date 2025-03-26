# 🚀 AI Driven - Customer spending suggestions and feedback

## 📌 Table of Contents
- [Introduction](#introduction)
- [Demo](#demo)
- [Inspiration](#inspiration)
- [What It Does](#what-it-does)
- [How We Built It](#how-we-built-it)
- [Challenges We Faced](#challenges-we-faced)
- [How to Run](#how-to-run)
- [Tech Stack](#tech-stack)
- [Team](#team)

---

## 🎯 Introduction

We want to create an AI based solution for banking customer spending suggestions and feedback, focusing on subscriptions and discretionary spending to help save costs.

## 🎥 Demo
🔗 [Live Demo](#) (if applicable)  
📹 [Video Demo](#) (if applicable)  
🖼️ Screenshots:

![Screenshot 1](link-to-image)

## 💡 Inspiration
Empowering customers with AI-driven insights to take control of their spending, optimize subscriptions, and achieve smarter financial savings effortlessly.

## ⚙️ What It Does
This code analyzes a user's transactions, detects recurring subscriptions, and provides personalized suggestions to save money. It flags high spending categories and encourages users to review and cancel unnecessary subscriptions. Let me know if you'd like enhancements, such as integrating AI-powered spending predictions or automated alerts. 🚀

Find any bugs and rewrite all the code to fix the bugs. Do not add any new comments. If there are no bugs, reply that you reviewed the code and found no bugs.

## 🛠️ How We Built It
This code primarily utilizes Python and the pandas library for data analysis.

**Technologies & Libraries Used**

**Python** – A general-purpose programming language used for data processing and analysis.

**pandas** – A powerful Python library for data manipulation, primarily used here for:

DataFrames to store and manage transaction data.
Grouping & Aggregation to compute category-wise spending and detect recurring transactions.
Tools
Python Interpreter (CPython, PyPy, or Anaconda) – Required to execute the script.
Command Line (Terminal/Command Prompt) – Used to run the script.
pip – Python package manager to install dependencies (pandas).

Text Editor/IDE (VS Code, PyCharm, Jupyter Notebook) – Useful for writing and debugging the script.

## 🚧 Challenges We Faced
**Identifying Subscriptions Accurately**

Challenge: Subscription descriptions vary widely across banks and providers. A simple keyword search (NETFLIX|SPOTIFY|HULU) may not capture all subscriptions.

Solution: Used case-insensitive str.contains() for broader detection but acknowledged the need for a more dynamic approach, such as integrating a financial API or machine learning-based categorization.

**Handling Missing or Inconsistent Data**

Challenge: Real-world transaction data often has missing values (NaN) or inconsistent category labels.

Solution: Used na=False in str.contains() to prevent errors and ensured spending categories were properly grouped before analysis.

**Determining "High Spending" Categories**

Challenge: Defining what qualifies as high spending is subjective—just comparing with the mean might not be ideal. Some necessary expenses (e.g., rent) will always be high.

Solution: Used mean spending as a simple benchmark but acknowledged the need for customized thresholds based on user preferences or historical trends.

## 🏃 How to Run
1. Clone the repository  
   ```sh
   git clone https://github.com/your-repo.git](https://github.com/ewfx/aidhp-digital-alchemists.git
   ```
2. Install dependencies  
   ```sh
   pip install pandas
   ```
3. Run the project  
   ```sh
   python banking_ai_savings.py
   ```

## 🏗️ Tech Stack
- 🔹 Backend: Python

## 👥 Team
- **Aditya Akkinapragada** - [GitHub](#) | [LinkedIn](#)
- **Lokesh Sajjan** - [GitHub](#) | [LinkedIn](#)
- **Praveen Patil** - [GitHub](#) | [LinkedIn](#)
- **Suresh Gembali** - [GitHub](#) | [LinkedIn](#)
  
