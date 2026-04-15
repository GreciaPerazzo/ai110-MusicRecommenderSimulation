"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.
"""

import csv
from src.song import Song
from src.user_profile import UserProfile
from src.recommender import Recommender

def load_songs(filepath):
    songs = []
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            song = Song(
                id=int(row['id']),
                title=row['title'],
                artist=row['artist'],
                genre=row['genre'],
                mood=row['mood'],
                energy=float(row['energy']),
                tempo_bpm=float(row['tempo_bpm']),
                valence=float(row['valence']),
                danceability=float(row['danceability']),
                acousticness=float(row['acousticness'])
            )
            songs.append(song)
    return songs

def main() -> None:
    # Load songs from CSV
    songs = load_songs('data/songs.csv')
    
    # Create a sample user profile
    user = UserProfile(
        preferred_genre="pop",
        preferred_mood="happy",
        preferred_energy=0.8,
        preferred_valence=0.8,
        preferred_tempo=120.0,
        preferred_danceability=0.8
    )
    
    # Create recommender
    rec = Recommender(songs)
    
    # Get top 3 recommendations with scores and reasons
    recommendations = rec.recommend(user, 3)
    
    # Print top 3 recommendations with scores
    print("Top 3 Recommended Songs:")
    print("-" * 50)
    for i, (song, score, reasons) in enumerate(recommendations, 1):
        print(f"{i}. {song.title}")
        print(f"   By: {song.artist}")
        print(f"   Score: {score:.2f}")
        print(f"   Reasons: {', '.join(reasons)}")
        print()

if __name__ == "__main__":
    main()
