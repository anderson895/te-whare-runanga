
# Hotel Reservation Django Project (PosgreSQL)

Minimal Django skeleton implementing:
- Admin: Login, Create/Update Room, List/Approve/Cancel Reservations, Logout
- Customer: Login, View Available Rooms, Make Reservation, Notifications, Reservation history, Logout
- Database: SQLite (default Django DB for local)

How to run:
1. Create a virtualenv and install requirements: `pip install -r requirements.txt`
2. Run migrations: `python manage.py migrate`
3. Create superuser: `python manage.py createsuperuser`
4. Run server: `python manage.py runserver`

# pip install -r .\requirements.txt


# python .\manage.py migrate

# python .\manage.py runserver