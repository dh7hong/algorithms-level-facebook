def solution(genres, plays):
    # Step 1: Calculate total plays per genre
    genre_total_plays = {}
    # Step 2: Keep track of songs per genre
    genre_songs = {}

    for i in range(len(genres)):
        genre = genres[i]
        play_count = plays[i]

        # Update total plays for each genre
        if genre in genre_total_plays:
            genre_total_plays[genre] += play_count
        else:
            genre_total_plays[genre] = play_count

        # Store songs in a list with their play count and index
        if genre in genre_songs:
            genre_songs[genre].append((play_count, i))
        else:
            genre_songs[genre] = [(play_count, i)]

    # Step 3: Sort genres by total plays in descending order
    sorted_genres = sorted(genre_total_plays.items(), key=lambda x: x[1], reverse=True)

    best_album = []

    # Step 4: Select up to two songs per genre, sorted by play count and index
    for genre, _ in sorted_genres:
        # Sort songs in current genre:
        # First by descending play counts, then by ascending index (if tie)
        songs = sorted(genre_songs[genre], key=lambda x: (-x[0], x[1]))
        
        # Add up to two songs from the sorted list
        best_album.extend([idx for _, idx in songs[:2]])

    return best_album

# Testing the solution:
print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
# Expected Output: [4, 1, 3, 0]
