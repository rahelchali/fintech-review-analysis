import pandas as pd
import os

def extract_thematic_insights():
    print("🧠 Initializing Advanced Keyword and Thematic Analysis Engine...")
    
    processed_path = 'data/processed/structured_bank_reviews.csv'
    if not os.path.exists(processed_path):
        print("❌ Error: Processed data asset missing. Please complete preprocessing first.")
        return
        
    df = pd.read_csv(processed_path)
    
    def map_detailed_theme(row):
        text = str(row['cleaned_text'])
        if any(w in text for w in ['slow', 'delay', 'wait', 'loading', 'hangs']):
            return 'Performance & Transfer Delays'
        elif any(w in text for w in ['fingerprint', 'biometric', 'budget', 'dark', 'feature', 'scanner']):
            return 'Mobile App Feature Request'
        elif any(w in text for w in ['login', 'otp', 'crash', 'error', 'failed', 'bug', 'server']):
            return 'Authentication & Server Bugs'
        return 'General Account Management'
        
    print("🔄 Mapping unstructured feedback vectors to strategic business dimensions...")
    df['identified_theme'] = df.apply(map_detailed_theme, axis=1)
    
    df.to_csv(processed_path, index=False)
    print("✅ Thematic keywords and industry clusters successfully appended to master dataset.")

if __name__ == "__main__":
    extract_thematic_insights()