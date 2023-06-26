from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from datetime import datetime, timedelta

def calculate_end_time(start_time):
    start_time_str = start_time.strftime('%H:%M')  # Convert start_time to string
    start_datetime = datetime.strptime(start_time_str, '%H:%M')
    end_datetime = start_datetime + timedelta(minutes=45)
    end_time = end_datetime.strftime('%H:%M:%S')
    return end_time


def create_calendar_event(doctor, date, start_time, end_time, required_speciality):
    # Define the required scopes
    SCOPES = ['https://www.googleapis.com/auth/calendar']

    # Create the OAuth 2.0 flow
    flow = InstalledAppFlow.from_client_secrets_file(
        r'C:\Users\aakas\Documents\Python\Task1\user_management\file.json',  # Path to your client secrets JSON file
        scopes=SCOPES
    )

    # Run the OAuth 2.0 authorization flow
    credentials = flow.run_local_server(port=8080)
                
    # Build the service client using the obtained credentials
    service = build('calendar', 'v3', credentials=credentials)

    # Create the event
    event = {
    "summary": "Appointment with Dr. {}".format(doctor.user.get_full_name()),
    "location": "doctor.user.address_line1",
    "description": "required_speciality",
    "start": {
        "dateTime": "{}T{}".format(date, start_time),
        "timeZone": "Asia/Kolkata"
    },
    "end": {
        "dateTime": "{}T{}".format(date, end_time),
        "timeZone": "Asia/Kolkata"
    }
}
    # Insert the event into the calendar
    calendar_id = 'primary'
    event = service.events().insert(calendarId=calendar_id, body=event).execute()
    print('Event created: %s' % (event.get('htmlLink')))
