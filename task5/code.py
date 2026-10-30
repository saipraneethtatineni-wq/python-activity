import math

def calculate_event_finances():
    venue_cost = float(input())
    equipment_cost = float(input())
    catering_per_person = float(input())
    transport_per_person = float(input())
    certificate_per_person = float(input())
    sponsorship = float(input())
    registration_fee = float(input())
    expected_participants = int(input())

    fixed_cost = venue_cost + equipment_cost
    variable_cost_per_person = catering_per_person + transport_per_person + certificate_per_person
    total_cost = fixed_cost + (variable_cost_per_person * expected_participants)

    sponsorship_shortfall = max(0.0, total_cost - sponsorship)
    participant_contributions = registration_fee * expected_participants
    total_income = sponsorship + participant_contributions
    net_balance = total_income - total_cost

    contribution_margin = registration_fee - variable_cost_per_person
    uncovered_fixed_cost = fixed_cost - sponsorship

    if uncovered_fixed_cost <= 0:
        if contribution_margin >= 0:
            break_even_participants = 0
        else:
            break_even_participants = "Impossible (Variable costs exceed registration fee)"
    else:
        if contribution_margin <= 0:
            break_even_participants = "Impossible (Registration fee does not cover variable costs)"
        else:
            break_even_participants = math.ceil(uncovered_fixed_cost / contribution_margin)

    print(f"Total Event Cost: {total_cost:.2f}")
    print(f"Sponsorship Shortfall: {sponsorship_shortfall:.2f}")
    print(f"Participant Contributions: {participant_contributions:.2f}")
    print(f"Net Balance: {net_balance:.2f}")
    print(f"Minimum Registrations for Break-even: {break_even_participants}")

if __name__ == "__main__":
    calculate_event_finances()
