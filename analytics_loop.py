import json
import os
import random

MATRIX_FILE = "analytics_matrix.json"

DEFAULT_MATRIX = {
    "UAE": {"weight": 1.0, "total_runs": 0, "avg_engagement": 0.0},
    "KSA": {"weight": 1.0, "total_runs": 0, "avg_engagement": 0.0},
    "US":  {"weight": 1.0, "total_runs": 0, "avg_engagement": 0.0}
}

def load_matrix():
    if not os.path.exists(MATRIX_FILE):
        save_matrix(DEFAULT_MATRIX)
        return DEFAULT_MATRIX
    with open(MATRIX_FILE, "r") as f:
        return json.load(f)

def save_matrix(data):
    with open(MATRIX_FILE, "w") as f:
        json.dump(data, f, indent=2)

def update_scores(region, engagement_score):
    matrix = load_matrix()
    if region in matrix:
        runs = matrix[region]["total_runs"] + 1
        prev_avg = matrix[region]["avg_engagement"]
        new_avg = prev_avg + ((engagement_score - prev_avg) / runs)
        
        matrix[region]["total_runs"] = runs
        matrix[region]["avg_engagement"] = round(new_avg, 2)
        matrix[region]["weight"] = round(1.0 + (new_avg / 100.0), 2)
        save_matrix(matrix)
        print(f"📈 [Analytics] Updated {region}: Avg Score = {matrix[region]['avg_engagement']}, Weight = {matrix[region]['weight']}")

def get_prioritized_region():
    matrix = load_matrix()
    regions = list(matrix.keys())
    weights = [matrix[r]["weight"] for r in regions]
    chosen = random.choices(regions, weights=weights, k=1)[0]
    return chosen, matrix[chosen]

if __name__ == "__main__":
    print("--- Testing Analytics Feedback Loop ---")
    update_scores("UAE", 85.5)
    update_scores("KSA", 92.0)
    update_scores("US", 78.0)
    selected, stats = get_prioritized_region()
    print(f"🎯 Weighted Pick for Next Cycle: {selected} ({stats})")
