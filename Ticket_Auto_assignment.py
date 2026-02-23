from datetime import datetime

# =================================================
# STEP 1: GET SHIFT ENGINEERS
# =================================================
def get_shift_engineers():
    return {
        "morning": ["Shiva", "Anil", "Uday"],
        "afternoon": ["Ajay", "Rahul", "Jayanth"],
        "night": ["Vamshi", "Kiran"]
    }


# =================================================
# STEP 2: DETECT CURRENT SHIFT
# =================================================
def detect_current_shift():
    current_hour = datetime.now().hour

    if 6 <= current_hour < 14:
        return "morning"
    elif 14 <= current_hour < 22:
        return "afternoon"
    else:
        return "night"


# =================================================
# STEP 3: GENERATE INCIDENT TICKETS
# =================================================
def generate_tickets(count=4, start_inc=54321):
    tickets = []
    for i in range(count):
        inc_number = f"INC{start_inc + i:09d}"
        tickets.append({
            "number": inc_number,
            "status": "new",
            "priority": "High" if i % 2 == 0 else "Low"
        })
    return tickets


# =================================================
# STEP 4: AUTO ASSIGN TICKETS (ROUND ROBIN)
# =================================================
def assign_tickets(tickets, engineers):
    print(" Ticket Assignment Started:\n")

    eng_index = 0
    for ticket in tickets:
        if ticket["status"] == "new":
            assigned_to = engineers[eng_index]
            ticket["assigned_to"] = assigned_to

            print(f"{ticket['number']} assigned to {assigned_to}")
            print(f"Notification: {ticket['number']} assigned to {assigned_to}\n")

            eng_index += 1
            if eng_index == len(engineers):
                eng_index = 0


# =================================================
# STEP 5: HIGH PRIORITY ALERTS
# =================================================
def check_high_priority(tickets):
    print(" High Priority Ticket Check:")
    for ticket in tickets:
        if ticket["priority"] == "High" and ticket["status"] == "new":
            print(f" ALERT: {ticket['number']} is HIGH priority!")


# =================================================
# STEP 6: SLA MONITORING
# =================================================
def sla_monitoring(sla_times):
    print("\n SLA Monitoring:")
    for time in sla_times:
        if time > 3:
            print(" SLA BREACH WARNING! Escalating ticket.")
            break
        else:
            print(f"SLA time remaining: {time} hours.")


# =================================================
# STEP 7: PROCESS VALID TICKETS
# =================================================
def process_ticket_numbers(ticket_numbers):
    print("\n Processing Ticket Numbers:")
    for t in ticket_numbers:
        if t is None:
            continue
        print(f"Processing ticket: {t}")


# =================================================
# MAIN PROGRAM (LIKE SERVICENOW FLOW)
# =================================================
def main():
    print("\n================ SERVICE TICKET AUTOMATION DEMO ================\n")

    shift_engineers = get_shift_engineers()
    current_shift = detect_current_shift()
    print(f"Current shift detected: {current_shift}\n")

    tickets = generate_tickets()
    engineers = shift_engineers[current_shift]

    assign_tickets(tickets, engineers)
    check_high_priority(tickets)

    sla_monitoring([10, 8, 2, 15])
    process_ticket_numbers(
        ["INC000054678", None, "INC000054679", None, "INC000054680"]
    )

    print("\n Automation completed successfully.")
    print("===============================================================\n")


# =================================================
# RUN PROGRAM
# =================================================
main()
