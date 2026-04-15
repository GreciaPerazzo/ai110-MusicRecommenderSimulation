from typing import List, Dict, Tuple, Optional
from src.song import Song
from src.user_profile import UserProfile

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def score_song(self, song: Song, user: UserProfile) -> Tuple[float, List[str]]:
        """Calculate the recommendation score and reasons for a song based on user preferences."""
        reasons = []
        
        # Numeric closeness scores (weighted)
        energy_score = 1 - abs(user.preferred_energy - song.energy)
        reasons.append(f"energy closeness (+{energy_score:.2f})")
        
        valence_score = 1 - abs(user.preferred_valence - song.valence)
        reasons.append(f"valence closeness (+{valence_score:.2f})")
        
        danceability_score = 1 - abs(user.preferred_danceability - song.danceability)
        reasons.append(f"danceability closeness (+{danceability_score:.2f})")
        
        # Tempo normalization (assume max meaningful diff is 120 BPM)
        tempo_diff = abs(user.preferred_tempo - song.tempo_bpm)
        tempo_score = 1 - min(tempo_diff / 120, 1)
        reasons.append(f"tempo closeness (+{tempo_score:.2f})")
        
        # Weighted numeric score
        numeric_score = (2 * energy_score + 
                        1.5 * valence_score + 
                        1.2 * danceability_score + 
                        1 * tempo_score)
        
        # Bonus points for matching genre and mood
        genre_bonus = 0
        if song.genre == user.preferred_genre:
            genre_bonus = 2.0
            reasons.append("genre match (+2.0)")
        
        mood_bonus = 0
        if song.mood == user.preferred_mood:
            mood_bonus = 1.0
            reasons.append("mood match (+1.0)")
        
        total_score = numeric_score + genre_bonus + mood_bonus
        
        return total_score, reasons

    def recommend(self, user: UserProfile, k: int = 5) -> List[Tuple[Song, float, List[str]]]:
        """Return the top k recommended songs with scores and reasons, sorted by score."""
        # Score all songs
        scored_songs = [(song, score, reasons) for song in self.songs 
                       for score, reasons in [self.score_song(song, user)]]
        
        # Sort by score descending
        scored_songs.sort(key=lambda x: x[1], reverse=True)
        
        # Return top k tuples
        return scored_songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Provide a textual explanation of why a song was recommended."""
        score, reasons = self.score_song(song, user)
        explanation = f"Score: {score:.2f}. Reasons: " + ", ".join(reasons)
        return explanation
