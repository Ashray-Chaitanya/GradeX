# GradeX Student Portal

This project uses HTML, CSS & JS for frontend and Flask (Python) for backend.
The Database management is done via MySQL (SQL).

How to test:
1. Create a database in MySQL Workbench.
2. Create 2 tables, one with student USNs and marks, and another with names and USNs.
3. Change the MySQL parameters in simple.py to match your database and table names.
4. Run your MySQL server.
5. Run `simple.py` using the command `python3 simple.py`
6. Navigate to `localhost:8000` on your browser.
7. Use the credentials **user<digits of USN without leading 0>** and password **bit<digits of USN without leading 0>** to login as that user.
8. Check out the features!
