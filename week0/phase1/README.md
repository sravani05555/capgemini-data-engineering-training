# 🚀 Phase 1 – SQL to PySpark Transformation

## 📌 Objective
This phase helped me understand how real-world SQL queries can be translated into PySpark DataFrame operations. Instead of just writing queries, I focused on understanding how data behaves in a distributed environment.

## 💡 My Learning Approach
I approached this phase by first thinking in SQL and then converting each query step-by-step into PySpark. This helped me build a strong connection between traditional databases and big data processing.

## ✅ Key Learnings
- Translating SQL logic into PySpark transformations
- Using `select()` for column-level operations
- Applying conditions using `filter()`
- Performing aggregations using `groupBy()`
- Understanding how DataFrames act like tables but operate differently internally

## 🧠 What I Understood Differently
Unlike SQL, PySpark does not execute immediately. I learned how transformations are lazy and only execute when an action like `show()` is called. This was an important mindset shift for me.

## ⚠️ Challenges I Faced
- Initially struggled with PySpark syntax and function-based approach
- Mapping SQL conditions into PySpark filters
- Understanding aggregation behavior in `groupBy()`

## 🔧 How I Solved Them
- Practiced multiple variations of the same query
- Compared SQL vs PySpark side-by-side
- Focused on understanding logic instead of memorizing syntax

## 🛠 Tools Used
- DB-Fiddle → SQL practice
- Spark Playground → PySpark execution

## 📊 Outcome
By the end of this phase, I am confident in converting basic SQL queries into PySpark code and understanding how data transformations work in a distributed system.
