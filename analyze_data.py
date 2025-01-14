import json
from collections import Counter

# Example function to analyze collected keywords and generate statistics
def analyze_keywords(collected_keywords):
    # Count the occurrences of each keyword
    keyword_counts = Counter(collected_keywords)

    # Convert the Counter object to a dictionary for easy access
    analyzed_data = dict(keyword_counts)

    # Save the analyzed data to a JSON file
    with open('analyzed_data.json', 'w') as outfile:
        json.dump(analyzed_data, outfile)

if __name__ == "__main__":
    analyzed_data = analyze_keywords(collected_keywords)
