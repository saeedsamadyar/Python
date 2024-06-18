from mitre_attack import ATTCK

# Define suspicious activities observed in server logs
suspicious_activities = {
    "unusual_login_attempts": True,
    "lateral_movement_detected": True,
    "persistence_mechanism_found": False
}

# Function to filter techniques based on suspicious activities
def filter_techniques(activities):
  techniques = ATTCK.enterprise.techniques.all
  filtered_techniques = []
  for technique in techniques:
    # Check if technique description mentions relevant activities
    if any(activity in technique.description for activity in activities.keys() if activities[activity]):
      filtered_techniques.append(technique)
  return filtered_techniques

# Call the function with suspicious activities
filtered_techniques = filter_techniques(suspicious_activities)

# Print potentially relevant MITRE ATT&CK techniques
if filtered_techniques:
  print("Potentially Relevant MITRE ATT&CK Techniques:")
  for technique in filtered_techniques:
    print(f"- {technique.name} ({technique.id})")
else:
  print("No matching techniques found based on provided activities.")

