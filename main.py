from database import create_table
from tracker import add_application, view_applications, update_status

create_table()

while True:
    print("\n1. Add Application")
    print("2. View Applications")
    print("3. Update Status")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        company = input("Company: ")
        role = input("Role: ")
        status = input("Status: ")
        date = input("Date: ")
        link = input("Link: ")

        add_application(company, role, status, date, link)

    elif choice == "2":
        view_applications()

    elif choice == "3":
        app_id = int(input("Enter ID: "))
        status = input("New Status: ")

        update_status(app_id, status)

    elif choice == "4":
        break

    else:
        print("Invalid choice")