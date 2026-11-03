with open("akv_ecosystem_master.py", "r") as f:
    code = f.read()

# Add auto-publisher execution call to Option 9 if present
if "akv_auto_publisher.py" not in code:
    code = code.replace("print(\"\\n✅ [COMPLETE] Autonomous closed-loop execution successfully deployed!\")",
                         "import os; os.system('python3 akv_auto_publisher.py')\n    print(\"\\n✅ [COMPLETE] Autonomous closed-loop execution successfully deployed!\")")

with open("akv_ecosystem_master.py", "w") as f:
    f.write(code)

print("✅ Master controller updated! Option 9 now auto-triggers the publisher daemon.")
