from datetime import datetime


# Record important game events
def audit_log(event, result):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("audit_log.txt", "a") as file:
        file.write(timestamp + " | " + event + " | " + result + "\n")