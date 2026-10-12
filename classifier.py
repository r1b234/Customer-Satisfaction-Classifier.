import re

POSITIVE_WORDS = {"badiya", "awesome", "great", "fantastic", "outstanding", "superb", "excellent", "love", "good", "happy", "smooth", "fast", "best", "mazaa"}
NEGATIVE_WORDS = {"bakwas", "bekar", "terrible", "poor", "worst", "waste", "crash", "disappointed", "slow", "issue", "bug", "fails", "problem"}

def classify_sentiment(comment):
    comment_lower = comment.lower()
    words = re.findall(r'\w+', comment_lower)
    
    pos_count = sum(1 for w in words if w in POSITIVE_WORDS)
    neg_count = sum(1 for w in words if w in NEGATIVE_WORDS)
    
    score = (pos_count - neg_count) / max(1, (pos_count + neg_count))
    
    if pos_count > neg_count or score > 0.05:
        classification = "Satisfied"
    elif neg_count > pos_count or score < -0.05:
        classification = "Dissatisfied"
    else:
        classification = "Neutral"
        
    return float(score), classification
