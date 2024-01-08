from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    songs = defaultdict(list)
    songs_sum = defaultdict(int)
    for idx, song in enumerate(zip(genres, plays)) :
        songs[song[0]].append([idx, song[1]])
        songs_sum[song[0]] += song[1]
        
    songs_sum = sorted(list(songs_sum.items()), key = lambda x:x[1], reverse=True)
    # print(songs_sum)
    
    genres_songs_sum = [s[0] for s in songs_sum]
    
    for k in songs.keys() :
        songs[k].sort(key = lambda x:(x[1], -x[0]), reverse=True)
        
    print(songs)
    for gen in genres_songs_sum :
        if len(songs[gen]) == 1 :
            answer.append(songs[gen][0][0])
        else :
            answer.append(songs[gen][0][0])
            answer.append(songs[gen][1][0])
        
    return answer