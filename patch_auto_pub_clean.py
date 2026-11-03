with open("akv_ecosystem_master.py", "r") as f:
    lines = f.readlines()

new_lines = []
inserted = False

for line in lines:
    new_lines.append(line)
    # Look for where option 9 completes its final print statement
    if "Autonomous closed-loop execution successfully deployed" in line and not inserted:
        # Get the indentation of the current line
        indent = line[:line.index("print")]
        new_lines.append(f"{indent}os.system('python3 akv_auto_publisher.py')\n")
        inserted = True

# Ensure os is imported
if not any("import os" in l for l in new_lines):
    new_lines.insert(0, "import os\n")

with open("akv_ecosystem_master.py", "w") as f:
    f.writelines(new_lines)

print("✅ Master controller successfully patched with clean indentation!")
