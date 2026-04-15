# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**VibeFinder 1.0**

---

## 2. Intended Use

VibeFinder 1.0 is a content-based music recommender designed to suggest songs that match a user's preferred musical "vibe" based on genre, mood, and audio features like energy, valence, tempo, and danceability. It assumes users have clear preferences for these attributes and generates personalized recommendations from a song catalog.

This model is intended for educational purposes and classroom exploration, not for production use with real users. It helps demonstrate basic recommendation concepts without relying on large-scale user data.

---

## 3. How the Model Works

VibeFinder scores each song by comparing it to the user's preferences. For numeric features (energy, valence, tempo, danceability), it calculates how close the song's values are to what the user likes—closer values get higher scores. Tempo differences are normalized to handle the wider range of BPM values.

It also gives bonus points if the song's genre and mood exactly match the user's favorites. The total score combines these closeness measures and bonuses, then ranks songs from highest to lowest score to recommend the top matches.

Compared to starter logic, this version uses weighted scoring (heavier on energy and valence) and includes tempo normalization for better accuracy.

---

## 4. Data

The model uses a small dataset of 10 songs from `songs.csv`, including attributes like title, artist, genre, mood, energy, tempo_bpm, valence, danceability, and acousticness. Genres represented include pop, lofi, rock, ambient, jazz, and synthwave. Moods include happy, chill, intense, relaxed, moody, focused.

No data was added or removed; the dataset is synthetic and limited. It misses real-world diversity, such as more artists, languages, or cultural contexts, and doesn't include user interaction data like plays or ratings.

---

## 5. Strengths

VibeFinder works well for users with straightforward preferences, such as those seeking high-energy pop or chill lofi tracks. It effectively captures "vibe" matching by rewarding songs that align closely on multiple features, leading to intuitive recommendations like suggesting upbeat pop songs for users who prefer happy, danceable music.

The scoring feels reasonable for simple cases, and the bonus system helps prioritize exact genre/mood matches without over-relying on numbers alone.

---

## 6. Limitations and Bias

The system can create filter bubbles by reinforcing initial preferences, potentially over-favoring certain genres (e.g., pop if the user starts there) and under-representing others like jazz or rock. It doesn't consider collaborative data (what others like), so it misses serendipitous discoveries.

Bias arises from fixed weights that may favor high-energy or high-valence songs, and the small dataset lacks balance—more pop/happy songs could skew results. It assumes users have precise numeric preferences, which may not reflect real tastes, and ignores factors like lyrics, artist popularity, or context (e.g., time of day).

---

## 7. Evaluation

Evaluation involved testing with a sample user profile (pop genre, happy mood, 0.8 energy/valence, 120 BPM tempo, 0.8 danceability) on the full dataset. Top recommendations were checked for relevance—e.g., pop/happy songs scored highest, as expected.

Surprisingly, some non-matching songs still scored decently due to numeric closeness, highlighting the need for better genre/mood weighting. Basic unit tests verified scoring and ranking logic, but no advanced metrics were used due to the simple setup.

---

## 8. Future Work

Future improvements could include hybrid collaborative filtering to incorporate user behavior data, adding more features like acousticness or artist similarity, and implementing diversity constraints to avoid filter bubbles.

Better explanations (e.g., "Recommended because of high energy match") and adaptive weights based on user feedback would enhance usability. Expanding the dataset and handling complex tastes (e.g., multiple preferred genres) would make it more robust for real applications.  

---

## 9. Personal Reflection  

Building VibeFinder 1.0 taught me that recommenders turn data into predictions by quantifying similarity between user preferences and item attributes, using weighted scores to rank options and surface the best matches. Surprisingly, the scoring system revealed that even songs from mismatched genres could rank highly if their numeric features (like energy or tempo) were close, underscoring the need for balanced weighting to avoid unintended biases. This experience shifted my perspective on apps like Spotify, showing how seemingly simple recommendations involve complex trade-offs between personalization, diversity, and ethical considerations to prevent filter bubbles and ensure fair discovery.  
