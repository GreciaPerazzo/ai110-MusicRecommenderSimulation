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
    
    # Get scored songs
    scored_songs = [(song, rec.score_song(song, user)) for song in songs]
    scored_songs.sort(key=lambda x: x[1], reverse=True)
    
    # Print top 3 recommendations with scores
    print("Top 3 Recommended Songs:")
    for i, (song, score) in enumerate(scored_songs[:3], 1):
        print(f"{i}. {song.title} by {song.artist} - Score: {score:.2f}")

if __name__ == "__main__":
    main()
