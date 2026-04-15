# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

A content-based music recommender system is simulated to recommend songs based on how well they match a user's taste profile. Music is scored by how close the attributes are to matching the user's profile, and then the system outputs a list of songs in order of their score.

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

This music recommendation system operates under the framework of collaborative filtering through use of attributes of songs to determine how similar they are to an individual user's taste profile. Each song receives a "score" based on how closely its attributes (e.g., genre, mood, energy, valence, tempo, danceability) match up to that user's preferences. For categorical attributes (e.g., genre, mood), users receive extra points for being an exact match; for numerical attributes (e.g., energy, valence), the user receives points based on their song preference being in proximity to the user's preference; i.e., the closer the song's value is to that of the user's preference for a particular attribute, the closer it is to receiving maximum scoring. The total scores for all songs are compiled and ranked with higher ranked songs having higher total scores. Then, a specified number of songs are given to the user based on their scores and ultimately provided to them as recommended songs.

**Song attributes:** Song title, artist, genre, mood, energy, tempo_bpm, valence, danceability, acousticness. 
**UserProfile attributes:** Preferred genre, mood, preferred energy, preferred valence, preferred tempo, preferred danceability. 
**Scoring Method:** Categorical attribute weightings + proximity-based numerical scoring. 
**Ranking Method:** Sort songs by total score, returning only the best N song results. 

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

- **Weight Adjustments**: Tested changing the energy weight from 2.0 to 1.0, which reduced the dominance of high-energy songs like "Gym Hero" in recommendations, allowing more balanced matches on other features.
- **User Profile Variations**: Experimented with a "chill" user (lofi genre, chill mood, low energy 0.4), resulting in top recommendations like "Library Rain" and "Focus Flow", confirming the system's ability to adapt to different vibes.
- **Feature Inclusion**: Added tempo normalization (capping diff at 120 BPM), which improved ranking for songs with moderate tempo differences, as seen in the pop user test where "Sunrise City" (118 BPM) scored higher than faster tracks.
- **Dataset Size Impact**: Ran the same pop/happy user on subsets of 5 songs vs. full 10, noting that smaller catalogs led to less diverse but more precise matches, highlighting scalability issues.

---

## Limitations and Risks

- **Small Dataset**: With only 10 songs, the system lacks diversity, potentially leading to repetitive recommendations and inability to handle varied user tastes.
- **Filter Bubbles**: The scoring heavily favors exact genre/mood matches, risking users getting stuck in echo chambers (e.g., always pop/happy songs for pop fans), limiting exposure to new genres.
- **Bias Toward Numeric Features**: High weights on energy/valence can over-prioritize intense or upbeat tracks, underrepresenting calm or melancholic music, and ignoring qualitative aspects like lyrics or cultural context.
- **Cold Start Problems**: New songs or users without established preferences aren't handled, as the system relies solely on content features without collaborative data.
- **Evaluation Gaps**: Manual testing with sample profiles may miss edge cases, and the lack of real user feedback means biases (e.g., toward popular genres) aren't detected.

---

## Reflection

Building VibeFinder 1.0 revealed the trade-offs between simplicity and effectiveness in recommendation systems. The content-based approach excelled at matching "vibes" through weighted features, as evidenced by intuitive top recommendations for the pop/happy user (e.g., "Sunrise City" for its close energy/valence match). However, it underscored real-world challenges like filter bubbles and data limitations, mirroring issues in platforms like Spotify.

Key lessons: Scoring rules need balance to avoid over-favoring certain attributes, and hybrid methods (content + collaborative) are essential for diversity. Future iterations should incorporate user feedback loops and larger datasets to mitigate biases. This project demonstrated how even basic AI can create engaging experiences while highlighting ethical considerations in personalization. For deeper analysis, see `model_card.md`.

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

