import os
import re
import json
import zipfile
import shutil
import sys

EXTRACT_DIR = "_extracted_apk"

REGEX_PATTERNS = {
    "Google API Key": r"AIza[0-9A-Za-z\-_]{35}",
    "Firebase Key": r"AAAA[A-Za-z0-9_-]{7}:[A-Za-z0-9_-]{140}",
    "AWS Access Key": r"AKIA[0-9A-Z]{16}",
    "New Relic Key": r"A[A-Za-z0-9]{39}-NRMA",
    "Authorization Bearer": r"Bearer\s+[A-Za-z0-9\-_]+\.[A-Za-z0-9\-_]+\.[A-Za-z0-9\-_]+",
    "JWT Token": r"eyJ[A-Za-z0-9-_]+\.[A-Za-z0-9-_]+\.[A-Za-z0-9-_]+",
    "UUID": r"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}",
    "Hex Secrets": r"\b[a-fA-F0-9]{32,64}\b",
    "Generic Email": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
    "Generic Secret": r"(?i)(secret|token|key|client_id|auth_domain)[\"'=:\s]{1,10}([\w\-\.:@]+)"
}

def extract_apk(apk_path):
    if os.path.exists(EXTRACT_DIR):
        shutil.rmtree(EXTRACT_DIR)
    os.makedirs(EXTRACT_DIR, exist_ok=True)
    with zipfile.ZipFile(apk_path, 'r') as zip_ref:
        zip_ref.extractall(EXTRACT_DIR)

def scan_files():
    findings = []
    for root, _, files in os.walk(EXTRACT_DIR):
        for filename in files:
            filepath = os.path.join(root, filename)
            try:
                with open(filepath, 'rb') as f:
                    content = f.read().decode(errors='ignore')
                    for name, pattern in REGEX_PATTERNS.items():
                        matches = re.findall(pattern, content)
                        if matches:
                            # فلترة وتنسيق النتائج
                            cleaned = set()
                            for m in matches:
                                if isinstance(m, tuple):
                                    cleaned.add(m[1])
                                else:
                                    cleaned.add(m.strip())
                            findings.append({
                                "file": filepath.replace(EXTRACT_DIR + os.sep, ""),
                                "type": name,
                                "matches": sorted(cleaned)
                            })
            except Exception:
                continue
    return findings

def save_report(results):
    with open("report.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4, ensure_ascii=False)

def main():
    if len(sys.argv) != 2:
        print("Usage: python api_extractor.py <path_to_apk>")
        return

    apk_path = sys.argv[1]
    if not os.path.isfile(apk_path):
        print("[!] APK file not found.")
        return

    print("[+] Extracting and scanning APK...")
    extract_apk(apk_path)
    results = scan_files()
    save_report(results)
    print(f"[+] Scan complete. Found {len(results)} files with sensitive data.")
    print("[+] Results saved to report.json")

if __name__ == "__main__":
    main()
