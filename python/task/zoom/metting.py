# zoom/meeting.py

from datetime import datetime


meeting_status = False
start_time = None


def start_meeting():
    global meeting_status
    global start_time

    if meeting_status:
        print("\nMeeting already started!")
        return

    meeting_status = True
    start_time = datetime.now()

    print("\n==============================")
    print("       MEETING STARTED")
    print("==============================")

    print("Meeting Start Time:",
          start_time.strftime("%d-%m-%Y %I:%M:%S %p"))


def end_meeting():
    global meeting_status
    global start_time

    if not meeting_status:
        print("\nNo meeting is currently running!")
        return

    end_time = datetime.now()

    print("\n==============================")
    print("        MEETING ENDED")
    print("==============================")

    print("Meeting Start Time:",
          start_time.strftime("%d-%m-%Y %I:%M:%S %p"))

    print("Meeting End Time:",
          end_time.strftime("%d-%m-%Y %I:%M:%S %p"))

    meeting_status = False
    start_time = None

    print("\nMeeting ended successfully!")