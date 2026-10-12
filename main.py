from crm_database import init_crm_db, fetch_crm_data
from classifier import classify_sentiment

def main():
    print("Initializing CRM Database...")
    init_crm_db()
    df = fetch_crm_data()
    print(f"Loaded {len(df)} customer records from database.")
    
    sample_comment = "Bohot badiya software hai!"
    score, cl = classify_sentiment(sample_comment)
    print(f"Sample Comment: '{sample_comment}' -> Sentiment: {cl} (Score: {score})")

if __name__ == "__main__":
    main()
