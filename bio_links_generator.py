import os

def build_links_page():
    links = [
        {"title": "🌐 Official Website", "url": "https://eakv.ebdaey.com/main"},
        {"title": "📺 YouTube Channel", "url": "https://youtube.com/@yourchannel"},
        {"title": "📩 Business Inquiries", "url": "mailto:contact@ebdaey.com"}
    ]

    link_buttons = "\n".join([
        f'    <a href="{link["url"]}" class="link-btn">{link["title"]}</a>'
        for link in links
    ])

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Amr Khedr | Elite AKV</title>
  <style>
    body {{
      background-color: #0d0d0d;
      color: #ffffff;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 40px 20px;
      margin: 0;
      min-height: 100vh;
    }}
    h1 {{ font-size: 1.25rem; margin: 0 0 4px 0; font-weight: 700; }}
    p {{ font-size: 0.9rem; color: #8e8e93; margin: 0 0 24px 0; }}
    .links-container {{ width: 100%; max-width: 400px; display: flex; flex-direction: column; gap: 14px; }}
    .link-btn {{
      background: #1c1c1e;
      color: #ffffff;
      text-decoration: none;
      padding: 16px 20px;
      border-radius: 12px;
      text-align: center;
      font-weight: 600;
      font-size: 0.95rem;
      border: 1px solid #2c2c2e;
      transition: background 0.2s ease, transform 0.1s ease;
    }}
    .link-btn:hover {{ background: #2c2c2e; transform: translateY(-1px); }}
  </style>
</head>
<body>
  <h1>Amr Khedr</h1>
  <p>Elite Performance Content | US · UAE · KSA</p>
  <div class="links-container">
{link_buttons}
  </div>
</body>
</html>"""

    os.makedirs('staged_output', exist_ok=True)
    with open('staged_output/links.html', 'w') as f:
        f.write(html_content)
    print('✅ [Bio Links] Generated fresh links.html in staged_output/')

if __name__ == '__main__':
    build_links_page()
