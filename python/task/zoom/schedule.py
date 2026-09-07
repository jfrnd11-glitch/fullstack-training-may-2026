from datetime import datetime

scheduled_meetings = []


def schedule_meeting():
    print("\n==============================")
    print("      SCHEDULE MEETING")
    print("==============================")

    title = input("Enter Meeting Title: ").strip()

    if title == "":
        print("Meeting title cannot be empty!")
        return

    while True:
        date_input = input("Enter Date (DD-MM-YYYY): ").strip()

        try:
            meeting_date = datetime.strptime(
                date_input,
                "%d-%m-%Y"
            )

            break

        except ValueError:
            print("Invalid date! Example: 15-08-2026")

    while True:
        time_input = input("Enter Time (HH:MM): ").strip()

        try:
            meeting_time = datetime.strptime(
                time_input,
                "%H:%M"
            )

            break

        except ValueError:
            print("Invalid time! Example: 14:30")

    meeting_datetime = datetime.combine(
        meeting_date.date(),
        meeting_time.time()
    )

    scheduled_meetings.append({
        "title": title,
        "datetime": meeting_datetime
    })

    print("\n================================")
    print("Meeting scheduled successfully!")
    print("================================")

    print("Meeting:", title)

    print(
        "Date:",
        meeting_datetime.strftime("%d-%m-%Y")
    )

    print(
        "Time:",
        meeting_datetime.strftime("%I:%M %p")
    )