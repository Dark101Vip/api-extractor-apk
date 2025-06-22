# 🔍 API Key & Secret Extractor from APK

Extract sensitive information such as API keys, secrets, and credentials from Android APK files — quickly and efficiently.



## 📦 About

**API Extractor** is a powerful tool designed for **security researchers, bug bounty hunters, mobile security analysts**, and developers who want to scan APKs for **exposed credentials** and **API keys**.

It unpacks `.apk` files and scans for secrets using advanced regex patterns — and classifies findings by **service type**, such as Google, AWS, Firebase, New Relic, etc.

---

## 🚀 Features

✅ Extract API keys and secrets from `.apk` files  
✅ Categorize secrets by **service provider**  
✅ Supports `.env`, `.json`, `.xml`, `.smali`, `.js`, `resources.arsc`, and more  
✅ Generates clean, structured `report.json`  
✅ Detects hardcoded:
- 🔑 Google API keys
- 🔐 Firebase Server Keys
- 🔑 AWS Access Keys
- 🔐 JWTs & Bearer tokens
- 📨 Emails
- 🛠 Generic secrets and tokens
- 📱 New Relic Keys
- 📎 UUIDs, Hex strings, and more...

---

## 📂 Output Example

```json
[
  {
    "file": "assets/flutter_assets/.env/.env.prod",
    "type": "Google API Key",
    "matches": [
      "AIzaSyBvFZf6asffafdfdDzr4mFQqqJEkhgEzcZzU"
    ]
  },
  {
    "file": "resources.arsc",
    "type": "New Key",
    "matches": [
      "AA9088282f705dasfgfgdfa3a1ee07f16a2cae-NRMA"
    ]
  }
]
🛠 Requirements
Install required packages (if not already available):

pip install -r requirements.txt

Note: This script uses only built-in modules — requirements.txt is optional.

🧪 Usage


python api_extractor.py <path_to_apk>
Example:
bash
python api_extractor.py samples/WisdomTreePrime.apk
📝 Output will be saved in report.json.

📁 File Structure
bash

api-extractor-apk/
│
├── api_extractor.py       # Main scanner script
├── report.json            # Output results
└── _extracted_apk/        # Auto-created temp folder (deleted if exists)
⚠️ Disclaimer
This tool is intended for educational and ethical security testing only.
Do not use it on applications without proper authorization.

📬 Contact
Made with 💻 by Abdulrahman Mohamed Gaber (Dark101)
📧 Email: abdogaber690@gmail.com
🌐 GitHub: Dark101Vip

🪪 License
MIT License © 2025 Dark101
