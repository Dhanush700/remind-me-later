
# Remind-me-later API

This Django REST API allows users to set reminders with a message, date, time, and delivery type (SMS or Email).

## Features

- Create a reminder using POST API
- Fields: `date`, `time`, `message`, `reminder_type`
- Supports `SMS` and `Email` as reminder types

## Installation

```bash
git clone https://github.com/YourUsername/remind-me-later.git
cd remind-me-later
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
```

## API Endpoint

**POST** `/reminders/create/`

### Sample JSON:

```json
{
  "date": "2025-05-20",
  "time": "15:30:00",
  "message": "Call mom",
  "reminder_type": "SMS"
}
```

## Response

```json
{
  "id": 1,
  "date": "2025-05-20",
  "time": "15:30:00",
  "message": "Call mom",
  "reminder_type": "SMS"
}
```

## License

MIT
