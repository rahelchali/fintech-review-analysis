import pandas as pd
import os
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

try:
    import matplotlib.pyplot as plt
    import seaborn as sns
    HAS_PLOT = True
except ImportError:
    HAS_PLOT = False

def run_sentiment_pipeline():
    print("🧠 Initializing VADER Sentiment Analysis Engine...")
    nltk.download('vader_lexicon', quiet=True)
    sia = SentimentIntensityAnalyzer()
    
    processed_path = 'data/processed/structured_bank_reviews.csv'
    if not os.path.exists(processed_path):
        print("❌ Error: Processed data asset missing.")
        return
        
    df = pd.read_csv(processed_path)
    print("🔄 Computing continuous polarity scores...")
    df['sentiment_score'] = df['review_text'].apply(lambda x: sia.polarity_scores(str(x))['compound'])
    
    def classify_vader(score):
        if score >= 0.05: return 'Positive'
        elif score <= -0.05: return 'Negative'
        else: return 'Neutral'
        
    df['sentiment_label'] = df['sentiment_score'].apply(classify_vader)
    df.to_csv(processed_path, index=False)
    print("✅ Sentiment attributes appended successfully.")
    
    if HAS_PLOT:
        print("📊 Generating required interim visualization charts...")
        os.makedirs('notebooks/plots', exist_ok=True)
        plt.figure(figsize=(10, 6))
        sns.set_theme(style="whitegrid")
        
        sns.countplot(data=df, x='bank_name', hue='sentiment_label', palette='viridis')
        plt.title('Early Sentiment Findings: CBE vs BOA vs Dashen', fontsize=14, fontweight='bold')
        plt.xlabel('Financial Platform Application', fontsize=12)
        plt.ylabel('User Review Frequency Volume', fontsize=12)
        plt.legend(title='Sentiment Class')
        
        plot_output = 'notebooks/plots/interim_sentiment_distribution.png'
        plt.savefig(plot_output, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"📈 Chart successfully saved to: {plot_output}")
    else:
        print("⚠️ Warning: Plotting libraries missing.")

if __name__ == "__main__":
    run_sentiment_pipeline()