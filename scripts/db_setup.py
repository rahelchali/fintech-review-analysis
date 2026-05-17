import pandas as pd
import os
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

# 1. Banks Metadata Table
class Bank(Base):
    __tablename__ = 'banks'
    bank_id = Column(Integer, primary_key=True, autoincrement=True)
    bank_name = Column(String(100), unique=True, nullable=False)
    app_name = Column(String(100), nullable=False)
    reviews = relationship("Review", back_populates="bank")

# 2. Processed Reviews Relational Table
class Review(Base):
    __tablename__ = 'reviews'
    review_id = Column(String(100), primary_key=True)
    bank_id = Column(Integer, ForeignKey('banks.bank_id'), nullable=False)
    review_text = Column(String, nullable=True)
    rating = Column(Integer, nullable=False)
    review_date = Column(Date, nullable=False)
    sentiment_label = Column(String(50), nullable=True)
    sentiment_score = Column(Float, nullable=True)
    identified_theme = Column(String(100), nullable=True)
    source = Column(String(50), default='Google Play')
    bank = relationship("Bank", back_populates="reviews")

def run_database_pipeline():
    print("🗄️ Connecting to local PostgreSQL database cluster...")
    
    # ⚠️ Standard local PostgreSQL URI format. Update with your real password if changed!
    DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/bank_reviews"
    
    try:
        engine = create_engine(DATABASE_URL)
        # Drop old instances and build fresh schema tables
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        
        Session = sessionmaker(bind=engine)
        session = Session()
        
        # Insert Bank Entities Mapping
        banks_metadata = [
            {"bank_name": "CBE", "app_name": "Commercial Bank of Ethiopia Mobile"},
            {"bank_name": "BOA", "app_name": "Bank of Abyssinia Mobile"},
            {"bank_name": "Dashen", "app_name": "Dashen Bank Mobile"}
        ]
        
        for b in banks_metadata:
            session.add(Bank(bank_name=b["bank_name"], app_name=b["app_name"]))
        session.commit()
        
        # Fetch auto-generated primary key IDs
        bank_map = {b.bank_name: b.bank_id for b in session.query(Bank).all()}
        
        # Load processed dataset mapping
        processed_path = 'data/processed/structured_bank_reviews.csv'
        if not os.path.exists(processed_path):
            print("❌ Failure: Processed data asset missing. Run preprocessing first.")
            return
            
        df = pd.read_csv(processed_path)
        
        print(f"🔄 Bulk inserting {len(df)} records into relational schemas...")
        for _, row in df.iterrows():
            review_obj = Review(
                review_id=str(row['reviewId']),
                bank_id=bank_map[row['bank_name']],
                review_text=row['review_text'],
                rating=int(row['rating']),
                review_date=pd.to_datetime(row['date']).date(),
                sentiment_label=row.get('sentiment_label', 'Neutral'),
                sentiment_score=float(row.get('sentiment_score', 0.0)),
                identified_theme=row.get('identified_theme', 'General Account Management'),
                source=row['source']
            )
            session.add(review_obj)
            
        session.commit()
        print(f"✅ Production Database Engineering Complete! Populated tables successfully.")
        session.close()
        
    except Exception as e:
        print(f"❌ Database pipeline aborted. Reason: {str(e)}")
        print("\n💡 Tip: Make sure your local PostgreSQL Server is running and you have created an empty database named 'bank_reviews'!")

if __name__ == "__main__":
    run_database_pipeline()