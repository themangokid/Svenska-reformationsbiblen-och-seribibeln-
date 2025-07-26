import re
from pathlib import Path

def clean_text(text):
    # Remove verse numbers (1–3 digits), along with any extra spaces around them
    # This version removes:
    # - space + number + space
    # - punctuation + number + space
    # - avoids touching real numbers like "100 år"
    text = re.sub(r'(?<!\d)(?<!\d[.,])[\s,.!?;:]*\b\d{1,3}\b[\s,.!?;:]*', ' ', text)

    # Remove asterisks (*, **)
    text = re.sub(r'\*+', '', text)

    # Remove double spaces created by removal
    text = re.sub(r'\s{2,}', ' ', text)

    return text.strip()


def clean_all_txt_files_in_folder(folder_path="."):
    folder = Path(folder_path)

    txt_files = list(folder.glob("*.txt"))
    if not txt_files:
        print("⚠️ No .txt files found in the folder.")
        return

    for file_path in txt_files:
        try:
            with file_path.open(encoding="utf-8") as f:
                original_text = f.read()

            cleaned_text = clean_text(original_text)

            # Overwrite the original file
            with file_path.open("w", encoding="utf-8") as f:
                f.write(cleaned_text)

            print(f"✅ Cleaned: {file_path.name}")
        except Exception as e:
            print(f"❌ Failed to process {file_path.name}: {e}")

# 🔧 Run on current directory by default
if __name__ == "__main__":
    clean_all_txt_files_in_folder()
