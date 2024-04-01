# sourcery skip: collection-to-bool, de-morgan, equality-identity, remove-redundant-if, use-assigned-variable, dict-assign-update-to-union, while-to-for, for-index-replacement, remove-dict-keys

playlist = {
    "name": "Cry and Feel",
    "author": "Vicente",
    "songs": [
        {
            "name": "Mr. forgettable",
            "authors": ["David Kushner"],
            "album": "Mr. Forgettable",
            "date": "Jan 15, 2024",
            "duration": "3:33",
        },
        {
            "name": "Fire",
            "authors": ["Rafael Witt"],
            "album": "There's nothing wrong with me",
            "date": "Feb 23, 2024",
            "duration": "3:34",
        },
        {
            "name": "Você",
            "authors": ["Tim Maia"],
            "album": "Tim Maia 1971",
            "date": "Mar 15, 2024",
            "duration": "4:04",
        },
        {
            "name": "Beautiful Things",
            "authors": ["Benson Boone"],
            "album": "Beautiful Things",
            "date": "March 5, 2024",
            "duration": "3:00",
        },
        {
            "name": "Vienna",
            "authors": ["Billy Joel"],
            "album": "The Stranger (Legacy Edition)",
            "date": "Feb 23, 2024",
            "duration": "3:34",
        },
        {
            "name": "Prairies",
            "authors": ["BoyWithUke", "mxmtoon"],
            "album": "Serotonin Dreams",
            "date": "May 6, 2022",
            "duration": "3:12",
        },
    ],
}


print("Playlist".upper())
print(playlist["name"])
print(f"Created by: {playlist['author']} º {len(playlist['songs'])} songs")
for song in playlist["songs"]:
    print(
        f"+ {song['name']} by {', '.join(song['authors'])}   -  {song['album']}, {song['date']} - {song['duration']}"
    )
