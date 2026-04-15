# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name
VibeFinder 1.0

## 2. Goal/Task
Suggests songs that match a user's musical preferences based on genre, mood, and audio features.

## 3. Data Used
Uses 18 songs from a CSV file. Features include title, artist, genre, mood, energy, tempo, valence, danceability, acousticness. Limited by small size and synthetic data.

## 4. Algorithm Summary
Scores songs by closeness to user preferences. Gives points for numeric matches and bonuses for exact genre and mood matches. Weights energy more heavily.

## 5. Observed Behavior/Biases
Prioritizes genre matches, creating filter bubbles. Favors high-energy songs due to weights.

## 6. Evaluation Process
Tested with four user profiles. Ran weight experiments. Compared recommendations across profiles.

## 7. Intended Use and Non-Intended Use
Designed for educational demonstration of content-based recommendations. Should not be used for real music streaming or commercial applications.

## 8. Ideas for Improvement
Add collaborative filtering. Expand dataset. Implement user feedback for adaptive weights.

## Personal Reflection
The biggest learning moment was realizing how easily biases like filter bubbles emerge from simple scoring rules, showing the ethical challenges in real recommendation systems. AI tools helped generate code snippets and explain concepts quickly, but I had to double-check the scoring logic and test outputs manually to ensure accuracy. I was surprised that even basic weighted averages and bonuses could produce recommendations that felt intuitive and personalized, mimicking how platforms like Spotify work. If extending this project, I'd try integrating user feedback loops to adjust weights dynamically and explore hybrid models combining content and collaborative data for better diversity.  
