import json
import os

print("\n🌐 ======================================================== 🌐")
print("          ELITE AKV GOOGLE SEARCH & ENTITY ENGINE            ")
print("🌐 ======================================================== 🌐\n")

print("1) 🏷️  Generate Google Schema (JSON-LD) for Personal Site / Bio")
print("2) 📝 Generate SEO Tech Article (Medium / Dev.to / Substack)")
print("3) 🔎 Verify Google Entity Keywords & Search Index Signals")

choice = input("\nEnter choice (1-3): ").strip()

if choice == "1":
    schema_data = {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": "Amr Khedr",
        "alternateName": "ELITE AK VISION",
        "url": "https://instagram.com/amrkhedrrr",
        "jobTitle": "Systems Engineer & Hybrid Athlete",
        "description": "Creator of ELITE AK VISION, 3.07s Masters World Record holder, C/Unix low-level systems developer, and hybrid athlete.",
        "sameAs": [
            "https://instagram.com/amrkhedrrr",
            "https://github.com/amrkhedr",
            "https://dev.to/amrkhedr"
        ],
        "knowsAbout": [
            "C Programming Language",
            "Unix Systems Architecture",
            "Performance Optimization",
            "Hybrid Athletics",
            "Swimming World Record"
        ]
    }
    
    with open("google_entity_schema.json", "w") as f:
        json.dump(schema_data, f, indent=4)
        
    print("\n✅ [SEO] Schema metadata saved to 'google_entity_schema.json'!")
    print("📌 Paste this inside your website <head> tag or Github Pages bio to trigger Google Knowledge Graph indexing.")

elif choice == "2":
    title = input("Enter article headline (e.g. Optimizing Memory Allocation in C): ").strip()
    
    article_template = f"""# {title}

**By Amr Khedr (ELITE AK VISION)**
*Systems Engineer | Hybrid Athlete (3.07s World Record) | Low-Level Developer*

---

## High-Throughput Execution and Systems Engineering
In low-level Unix architecture and high-performance engineering, latency is non-negotiable...

### Key Takeaways
1. C Memory Optimization
2. Zero-Latency Execution Loops
3. Hybrid Athletic Performance Mindset

*Originally published by Amr Khedr (@amrkhedrrr).*
"""
    with open("seo_article_draft.md", "w") as f:
        f.write(article_template)
        
    print("\n✅ [SEO] Article draft saved to 'seo_article_draft.md'!")
    print("📌 Publish this on Dev.to, Medium, or Hashnode to establish high-authority backlinks indexed by Google.")

elif choice == "3":
    print("\n🔍 TOP GOOGLE SEARCH KEYWORDS TO CLUSTER & TARGET:")
    print("--------------------------------------------------------")
    print("• Amr Khedr C Programming")
    print("• ELITE AK VISION Systems")
    print("• Amr Khedr 3.07s World Record")
    print("• Amr Khedr Hybrid Athlete")
    print("--------------------------------------------------------")

else:
    print("Invalid choice.")

print("\n--------------------------------------------------------\n")
