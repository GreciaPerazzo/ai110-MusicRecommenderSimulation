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

    def score_song(self, song: Song, user: UserProfile) -> float:
        # Numeric closeness scores (weighted)
        energy_score = 1 - abs(user.preferred_energy - song.energy)
        valence_score = 1 - abs(user.preferred_valence - song.valence)
        danceability_score = 1 - abs(user.preferred_danceability - song.danceability)
        
        # Tempo normalization (assume max meaningful diff is 120 BPM)
        tempo_diff = abs(user.preferred_tempo - song.tempo_bpm)
        tempo_score = 1 - min(tempo_diff / 120, 1)
        
        # Weighted numeric score
        numeric_score = (2 * energy_score + 
                        1.5 * valence_score + 
                        1.2 * danceability_score + 
                        1 * tempo_score)
        
        # Bonus points for matching genre and mood
        genre_bonus = 2 if song.genre == user.preferred_genre else 0
        mood_bonus = 1 if song.mood == user.preferred_mood else 0
        
        return numeric_score + genre_bonus + mood_bonus

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # Score all songs
        scored_songs = [(song, self.score_song(song, user)) for song in self.songs]
        
        # Sort by score descending
        scored_songs.sort(key=lambda x: x[1], reverse=True)
        
        # Return top k songs
        return [song for song, score in scored_songs[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"
