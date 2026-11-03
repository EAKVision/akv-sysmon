import os

class BioLinksGenerator:
    def __init__(self):
        # Target path matching your domain subfolder: /p/aagtatkuav
        self.output_dir = "staged_output/p/aagtatkuav"
        os.makedirs(self.output_dir, exist_ok=True)
        self.output_file = os.path.join(self.output_dir, "index.html")

    def generate_hub(self):
        html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Amr Khedr (Elite AKV) | Hub</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background: #0b0f19; color: #ffffff; display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 100vh; margin: 0; padding: 20px; }
        .card { background: #161f33; border: 1px solid #233252; padding: 30px; border-radius: 16px; width: 100%; max-width: 400px; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
        h1 { margin-bottom: 5px; font-size: 1.6rem; }
        p { color: #94a3b8; font-size: 0.95rem; margin-bottom: 25px; }
        .btn { display: block; background: #2563eb; color: #fff; text-decoration: none; padding: 14px 20px; border-radius: 10px; margin-bottom: 12px; font-weight: 600; transition: background 0.2s; }
        .btn:hover { background: #1d4ed8; }
    </style>
</head>
<body>
    <div class="card">
        <h1>Amr Khedr (Elite AKV)</h1>
        <p>Global Systems • High Performance • Scaling</p>
        <a href="https://instagram.com/amrkhedrrr" class="btn">Instagram Profile</a>
        <a href="https://github.com/EAKVision" class="btn">GitHub Core Repos</a>
        <a href="mailto:contact@eakv.ebdaey.com" class="btn">Direct Contact / Inquiries</a>
    </div>
</body>
</html>"""
        with open(self.output_file, 'w') as f:
            f.write(html_content)
        print(f"✅ Generated bio link landing page at: {self.output_file}")
        return self.output_file

if __name__ == '__main__':
    generator = BioLinksGenerator()
    generator.generate_hub()
