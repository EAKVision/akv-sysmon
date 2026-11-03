import os
import json

class PredictiveEngine:
    def __init__(self):
        self.confidence_threshold = 95.0

    def forecast_virality(self, region, hook_score, trend_multiplier):
        """
        Predicts the performance ceiling of a staged reel based on multi-variable inputs.
        """
        print(f"🔮 [Predictive Engine] Calculating trajectory for region [{region}]...")
        
        # Algorithmic prediction formula
        base_projection = (hook_score * 0.6) + (trend_multiplier * 15.0)
        projected_score = min(round(base_projection, 2), 100.0)
        
        status = "CERTIFIED VIRAL WINNER 🚀" if projected_score >= self.confidence_threshold else "OPTIMIZATION REQUIRED ⚡"
        
        print(f"📊 [Predictive Engine] Projected Performance Score: {projected_score}/100 | Status: {status}")
        return {"projected_score": projected_score, "status": status}

if __name__ == '__main__':
    engine = PredictiveEngine()
    engine.forecast_virality("UAE", 96, 2.6)
