def get_base_fare(distance):
    if distance <= 100:
        return 50.0
    elif distance <= 500:
        return 50.0 + (distance - 100) * 0.80
    elif distance <= 1000:
        return 370.0 + (distance - 500) * 0.60
    else:
        return 670.0 + (distance - 1000) * 0.40

def calculate_passenger_fare(class_base_fare, res_fee, age):
    if age < 5:
        return 0.0, 0.0, "Infant (100% Off, No Fee)"
    elif age <= 12:
        fare = (class_base_fare * 0.50) + res_fee
        return fare, res_fee, "Child (50% Off)"
    elif age >= 60:
        fare = (class_base_fare * 0.60) + res_fee
        return fare, res_fee, "Senior (40% Off)"
    else:
        fare = class_base_fare + res_fee
        return fare, res_fee, "General (Full)"

def compute_cancellation(total_fare, num_passengers, hours):
    if hours > 48:
        flat_deduction = 30.0 * num_passengers
        percentage_deduction = 0.20 * total_fare
        penalty = max(flat_deduction, percentage_deduction)
    elif hours >= 12:
        penalty = 0.25 * total_fare
    elif hours >= 4:
        penalty = 0.50 * total_fare
    else:
        penalty = total_fare
    
    penalty = min(penalty, total_fare)
    refund = total_fare - penalty
    return penalty, refund

def main():
    class_multipliers = {"GEN": 1.0, "SL": 1.2, "3A": 1.8, "2A": 2.5, "1A": 3.5}
    reservation_fees = {"GEN": 15.0, "SL": 20.0, "3A": 40.0, "2A": 50.0, "1A": 60.0}

    distance = float(input().strip())
    travel_class = input().strip().upper()

    if travel_class not in class_multipliers:
        return

    base_dist_fare = get_base_fare(distance)
    class_base_fare = base_dist_fare * class_multipliers[travel_class]
    res_fee = reservation_fees[travel_class]

    num_passengers = int(input().strip())
    passengers = []
    total_fare = 0.0

    for _ in range(num_passengers):
        line = input().strip().split(",")
        name = line[0].strip()
        age = int(line[1].strip())
        fare, fee_applied, category = calculate_passenger_fare(class_base_fare, res_fee, age)
        total_fare += fare
        passengers.append((name, age, category, fare))

    is_cancellation = input().strip().lower()
    cancel_hours = None
    if is_cancellation in ("yes", "y"):
        cancel_hours = float(input().strip())

    print(f"Journey Distance: {distance:.2f} km")
    print(f"Travel Class: {travel_class}")
    print(f"Class Base Fare: ${class_base_fare:.2f}")
    print(f"Reservation Fee: ${res_fee:.2f}")
    print("--------------------------------------------------")
    for name, age, cat, fare in passengers:
        print(f"Passenger: {name:15} | Age: {age:2} | Category: {cat:22} | Fare: ${fare:.2f}")
    print("--------------------------------------------------")
    print(f"Total Booking Amount: ${total_fare:.2f}")

    if cancel_hours is not None:
        penalty, refund = compute_cancellation(total_fare, num_passengers, cancel_hours)
        print("--------------------------------------------------")
        print(f"Cancellation Time: {cancel_hours:.1f} hours before departure")
        print(f"Cancellation Charges: ${penalty:.2f}")
        print(f"Net Refund Amount: ${refund:.2f}")

if __name__ == "__main__":
    main()
