# 0x00-MySQL_Advanced

This project dives deeper into MySQL, focusing on advanced concepts and techniques beyond the basics of database creation and simple queries.

## Learning Objectives
By the end of this project, you should be able to:

* Understand and apply advanced SQL concepts like subqueries, triggers, and stored procedures.
* Design and implement views for customized data representation.
* Create and utilize functions for code reusability and modularity.
* Manage transactions for data consistency and integrity.
* Implement indexing strategies for query optimization.

## Project Structure

The project is organized into a series of tasks, each focusing on a specific concept or technique:

* **0-uniq_users.sql:** Creates a table with a unique email constraint.
* **1-country_users.sql:** Adds an ENUM column with a default value.
* **2-fans.sql:** Sets up a many-to-many relationship between users and TV shows.
* **3-glam_rock.sql:** Inserts data into the tables, including TV shows and user preferences.
* **4-store.sql:** Retrieves TV shows watched by a specific user.
* **5-valid_email.sql:** Creates a trigger to prevent email changes.
* **6-suspicious_activities.sql:** Adds a trigger to reset emails when usernames are updated.
* **7-average_score.sql:** Creates a stored procedure to compute the average score for a student.
* **8-top_students.sql:** Creates a stored procedure to rank students based on their average score.
* **9-new_user.sql:** Creates a stored procedure to add a new correction for a student.
* **10-average_score_for_user.sql:** Creates a function to compute the average score for a student.
* **11-complex_query.sql:** Retrieves complex information using subqueries.
* **100-average_weighted_score.sql:** Computes a weighted average score for projects.
* **101-good_students.sql:** Creates a view to display good students based on specific criteria.

## Technologies Used

* MySQL

## Resources

* [MySQL Documentation](https://dev.mysql.com/doc/)
* [SQL Tutorial](https://www.w3schools.com/sql/)

This README provides a comprehensive overview of the 0x00-MySQL_Advanced project, outlining its objectives, structure, and the technologies involved. It serves as a guide for anyone interested in expanding their knowledge and skills in MySQL.