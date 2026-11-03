with open("akv_ecosystem_master.py", "r") as f:
    code = f.read()

# Update the verification filename prefix to match elite_boosted_
code = code.replace("elite_motion_", "elite_boosted_")

with open("akv_ecosystem_master.py", "w") as f:
    f.write(code)

print("✅ Option 9 verification step aligned with parallel batch output naming!")
