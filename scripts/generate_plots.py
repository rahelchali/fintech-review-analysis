import pandas as pd
import os

try:
    import matplotlib.pyplot as plt
    import seaborn as sns
    HAS_PLOT = True
except ImportError:
    HAS_PLOT = False

def build_stakeholder_visuals():
    print("📊 Initializing Omega Consultancy Visualization Engine...")
    processed_path = 'data/processed/structured_bank_reviews.csv'
    
    if not os.path.exists(processed_path):
        print("❌ Error: Missing structured bank data framework.")
        return
        
    df = pd.read_csv(processed_path)
    os.makedirs('notebooks/plots', exist_ok=True)
    
    if HAS_PLOT:
        sns.set_theme(style="whitegrid")
        
        # Plot 1: Rating Benchmarks (Scenario 1 Evidence)
        plt.figure(figsize=(10, 5))
        sns.boxplot(data=df, x='bank_name', y='rating', palette='Set2')
        plt.title('Store Rating Distribution Benchmark: CBE vs BOA vs Dashen', fontsize=12, fontweight='bold')
        plt.xlabel('Financial Institution Application')
        plt.ylabel('User Scores (1-5 Stars)')
        plt.savefig('notebooks/plots/rating_distribution_benchmark.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        # Plot 2: Recurring Core Complaints Count (Scenario 3 Evidence)
        plt.figure(figsize=(11, 5))
        sns.countplot(data=df, x='identified_theme', hue='bank_name', palette='muted')
        plt.title('Thematic Complaint & Request Distribution Across Competitors', fontsize=12, fontweight='bold')
        plt.xlabel('Identified Strategic Theme')
        plt.ylabel('Volume Frequency of Mentions')
        plt.xticks(rotation=15)
        plt.legend(title='Bank')
        plt.savefig('notebooks/plots/thematic_issue_distribution.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        print("✅ Stakeholder-ready visualization suite exported to notebooks/plots/ folder.")
    else:
        print("⚠️ Plotting libraries not available.")

if __name__ == "__main__":
    build_stakeholder_visuals()