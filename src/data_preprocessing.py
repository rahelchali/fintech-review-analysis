import pandas as pd
import glob
import os
import re

def clean_and_tag_data():
    print("🧹 Commencing text preprocessing and consulting scenario tagging...")
    
    raw_paths = glob.glob('data/raw/*_raw_reviews.csv')
    if not raw_paths:
        print("⚠️ No raw data assets found in data/raw. Run the scraper script first.")
        return
        
    combined_df = pd.concat([pd.read_csv(p) for p in raw_paths], ignore_index=True)
    
    combined_df['date'] = pd.to_datetime(combined_df['date']).dt.strftime('%Y-%m-%d')
    combined_df['review_text'] = combined_df['review_text'].fillna("")
    
    def normalize_text(text):
        text = text.lower()
        text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        return text.strip()
        
    combined_df['cleaned_text'] = combined_df['review_text'].apply(normalize_text)
    
    combined_df['is_transfer_issue'] = combined_df['cleaned_text'].str.contains('slow|transfer|loading|delay|wait|hangs')
    combined_df['has_feature_request'] = combined_df['cleaned_text'].str.contains('fingerprint|biometric|budget|dark mode|feature|scanner')
    combined_df['is_technical_complaint'] = combined_df['cleaned_text'].str.contains('login|otp|crash|error|failed|bug|server')
    
    os.makedirs('data/processed', exist_ok=True)
    processed_path = 'data/processed/structured_bank_reviews.csv'
    combined_df.to_csv(processed_path, index=False)
    print(f"✅ Preprocessing Complete! {len(combined_df)} records structured at {processed_path}")

if __name__ == "__main__":
    clean_and_tag_data()