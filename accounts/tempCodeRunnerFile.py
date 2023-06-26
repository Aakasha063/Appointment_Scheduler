SCOPES = ['https://www.googleapis.com/auth/calendar']

    # Create the OAuth 2.0 flow
    flow = InstalledAppFlow.from_client_secrets_file(
        r'C:\Users\aakas\Documents\Python\Task1\user_management\file.json',  # Path to your client secrets JSON file
        scopes=SCOPES
    )

    # Run the OAuth 2.0 authorization flow
    credentials = flow.run_local_server(port=8000)