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
    
    # Create recommender
    rec = Recommender(songs)
    
    # Define user profiles
    profiles = [
        ("High-Energy Pop", UserProfile(
            preferred_genre="pop",
            preferred_mood="happy",
            preferred_energy=0.9,
            preferred_valence=0.85,
            preferred_tempo=130.0,
            preferred_danceability=0.9
        )),
        ("Chill Lofi", UserProfile(
            preferred_genre="lofi",
            preferred_mood="chill",
            preferred_energy=0.35,
            preferred_valence=0.58,
            preferred_tempo=75.0,
            preferred_danceability=0.6
        )),
        ("Deep Intense Rock", UserProfile(
            preferred_genre="rock",
            preferred_mood="intense",
            preferred_energy=0.92,
            preferred_valence=0.45,
            preferred_tempo=150.0,
            preferred_danceability=0.65
        )),
        ("Conflicted", UserProfile(
            preferred_genre="pop",
            preferred_mood="sad",
            preferred_energy=0.9,
            preferred_valence=0.2,
            preferred_tempo=120.0,
            preferred_danceability=0.8
        )),
    ]
    
    # Run recommender for each profile
    for profile_name, user in profiles:
        recommendations = rec.recommend(user, 5)
        
        print(f"\n=== {profile_name} Profile ===")
        print("-" * 50)
        for i, (song, score, reasons) in enumerate(recommendations, 1):
            print(f"{i}. {song.title}")
            print(f"   By: {song.artist}")
            print(f"   Score: {score:.2f}")
            print(f"   Reasons: {', '.join(reasons)}")
            print()

if __name__ == "__main__":
    main()
