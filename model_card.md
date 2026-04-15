# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name
VibeFinder 1.0

## 2. Goal/Task
Suggest songs matching user vibe preferences.

## 3. Data Used
18 songs with features like genre, mood, energy, valence, tempo, danceability. Limited by small size and synthetic nature.

## 4. Algorithm Summary
Scores songs based on how well their attributes match user preferences, using closeness for numbers and bonuses for exact matches.

## 5. Observed Behavior/Biases
Filter bubbles from genre dominance, energy bias favoring high-energy tracks, and conflicted profile showing genre overrides mood.

## 6. Evaluation Process
4 profiles tested, weight experiment conducted, unit tests run.

## 7. Intended Use and Non-Intended Use
Educational only. Not for real products or users.

## 8. Ideas for Improvement
Hybrid filtering, diversity controls, larger dataset.

## Personal Reflection
The biggest learning was how biases emerge from simple rules. AI tools helped with coding and explanations, but logic needed manual checks. I was surprised simple algorithms can feel like real recommendations. Next, I'd add user feedback for adaptive scoring.  
