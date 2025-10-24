# Hotel Reservation Django Project

A minimal Django project skeleton for a hotel reservation system with admin and customer features.  

---

## Features

### Admin
- Login / Logout
- Create / Update Rooms
- List / Approve / Cancel Reservations

### Customer
- Login / Logout
- View Available Rooms
- Make Reservations
- Notifications
- Reservation History

### Database
- Default: SQLite for local development
- Optional: PostgreSQL (Supabase or other hosted database) for production

---

## Prerequisites

- Python 3.10+  
- pip  
- Optional: PostgreSQL server (if using Postgres instead of SQLite)

---

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/anderson895/te-whare-runanga
cd te-whare-runanga


python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
