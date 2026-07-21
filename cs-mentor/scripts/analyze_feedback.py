# Feedback Analysis Script
# This script analyzes the feedback_log.md and provides actionable insights.

import os

def analyze_feedback(log_path):
    if not os.path.exists(log_path):
        return "No feedback log found."
    
    with open(log_path, 'r') as f:
        lines = f.readlines()
    
    # Simple analysis: Count sessions and summarize key feedback
    sessions = 0
    feedback_points = []
    
    for line in lines:
        if line.startswith('*'):
            feedback_points.append(line.strip())
            sessions += 1
            
    summary = f"Analyzed {sessions} sessions.\nKey Feedback Points:\n"
    for point in feedback_points:
        summary += f"- {point}\n"
        
    return summary

if __name__ == "__main__":
    log_path = "../references/feedback_log.md"
    print(analyze_feedback(log_path))
