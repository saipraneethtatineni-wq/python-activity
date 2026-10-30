from dataclasses import dataclass

@dataclass
class BatchRecord:
    product_name: str
    batch_id: str
    produced: int
    defective: int
    threshold_pct: float

def analyze_quality_matrix(batches):
    total_produced = 0
    total_defective = 0
    flagged_batches = []
    matrix_results = []

    for b in batches:
        if b.produced <= 0 or b.defective < 0 or b.defective > b.produced:
            matrix_results.append({
                "product": b.product_name,
                "batch_id": b.batch_id,
                "produced": b.produced,
                "defective": b.defective,
                "defect_pct": None,
                "threshold_pct": b.threshold_pct,
                "status": "INVALID_DATA"
            })
            continue

        defect_pct = (b.defective / b.produced) * 100
        is_flagged = defect_pct > b.threshold_pct

        total_produced += b.produced
        total_defective += b.defective

        status = "FLAGGED" if is_flagged else "PASSED"
        
        result_entry = {
            "product": b.product_name,
            "batch_id": b.batch_id,
            "produced": b.produced,
            "defective": b.defective,
            "defect_pct": defect_pct,
            "threshold_pct": b.threshold_pct,
            "status": status
        }
        matrix_results.append(result_entry)

        if is_flagged:
            flagged_batches.append(result_entry)

    overall_defect_pct = (total_defective / total_produced * 100) if total_produced > 0 else 0.0

    print(f"{'PRODUCT':<16} {'BATCH ID':<10} {'PRODUCED':<10} {'DEFECTIVE':<10} {'DEFECT %':<10} {'LIMIT %':<10} {'STATUS':<10}")
    print("-" * 78)
    for r in matrix_results:
        defect_str = f"{r['defect_pct']:.2f}%" if r['defect_pct'] is not None else "N/A"
        print(f"{r['product']:<16} {r['batch_id']:<10} {r['produced']:<10} {r['defective']:<10} {defect_str:<10} {r['threshold_pct']:<10.2f} {r['status']:<10}")

    print("-" * 78)
    print(f"Total Produced Units: {total_produced}")
    print(f"Total Defective Units: {total_defective}")
    print(f"Plant Overall Defect Rate: {overall_defect_pct:.2f}%")
    print(f"Flagged Batches Count: {len(flagged_batches)}")
    
    if flagged_batches:
        print("\nACTION REQUIRED - Batches Exceeding Tolerance:")
        for fb in flagged_batches:
            excess = fb['defect_pct'] - fb['threshold_pct']
            print(f"- [{fb['batch_id']}] {fb['product']}: Defect Rate {fb['defect_pct']:.2f}% exceeds limit of {fb['threshold_pct']:.2f}% by +{excess:.2f}%")

if __name__ == "__main__":
    records = [
        BatchRecord("Piston Ring", "B101", 5000, 120, 2.0),
        BatchRecord("Piston Ring", "B102", 4800, 160, 2.0),
        BatchRecord("Spark Plug", "B201", 12000, 180, 1.2),
        BatchRecord("Spark Plug", "B202", 11500, 210, 1.2),
        BatchRecord("Brake Rotor", "B301", 2500, 95, 3.0),
        BatchRecord("Brake Rotor", "B302", 3000, 60, 3.0)
    ]
    analyze_quality_matrix(records)
