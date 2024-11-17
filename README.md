# 🚀 Steps to Run the Project
1️⃣ Create a Virtual Environment (Optional but Recommended)
Run the following command to create a virtual environment:


# python3 -m venv venv
2️⃣ Activate the Virtual Environment
Activate the environment based on your OS:

Linux/macOS

# source venv/bin/activate
Windows

# .\venv\Scripts\activate
3️⃣ Check and Update Execution Policy (Windows Only)
If you're on Windows and face script execution issues:

Check Current Execution Policy

# Get-ExecutionPolicy
If the output is Restricted, follow the next step to bypass the restriction.
Temporarily Change Execution Policy
Run this command to allow script execution for the current session:


# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
Reactivate the Virtual Environment

# .\venv\Scripts\Activate
4️⃣ Install Dependencies
Install all required Python packages:


# pip install -r requirements.txt
5️⃣ Generate and Apply Migrations
Run the following commands to set up the database schema:


# python manage.py makemigrations
# python manage.py migrate


6️⃣ Run the Project
Start the development server using:


# python manage.py runserver
🔑 Steps to Access the Admin Panel


1️⃣ Create a Superuser
Run this command to create a superuser:


# python manage.py createsuperuser
Enter the required details like username, password, and email




2️⃣ Open the Admin Panel
Go to your browser and visit:

# http://127.0.0.1:8000/admin/

3️⃣ Login with Superuser Credentials
Enter the username and password you set earlier to access the admin dashboard.

🎉 You're All Set!
Now you can explore, manage, and extend the Swiggy Clone project as per your needs. Happy coding! 🚀






