VERIFY_PROMPT = """
You are an expert fact-checking AI.

Claim:
{claim}

Image Analysis:
{image_analysis}

Evidence from Google Search:
{evidence}

Your tasks:

1. Determine if the claim is TRUE or FALSE.
2. Use the evidence to support reasoning.
3. Consider if the image supports or contradicts the claim.
4. Provide a confidence score between 0 and 1.

Output format:

Prediction: TRUE/FALSE
Confidence: value
Explanation: reasoning
"""