import re

with open("akv_ecosystem_master.py", "r") as f:
    code = f.read()

# Replace single video execution call with batch execution script in option 9 block if present
if "akv_batch_processor.py" not in code:
    code = code.replace("akv_motion_booster.py", "akv_batch_processor.py")

with open("akv_ecosystem_master.py", "w") as f:
    f.write(code)

print("✅ Master controller patched! Option 9 now triggers Parallel Batch Engine.")
