

def converter(str_):
    rhythm = {'C#' : 'c','D#' : 'd','F#' : 'f','G#' : 'g','A#' : 'a'}
    for k, v in rhythm.items():
        str_ = str_.replace(k, v)
        
    return str_
    
def solution(m, musicinfos):
    m = converter(m)
    answer = '(None)'
    max_pt = 0

    for index, music in enumerate(musicinfos):
        s, e, name, code = music.split(',')
        code = converter(code)
        music_time = len(code)
        
        s = [int(i) for i in s.split(':')]
        e = [int(i) for i in e.split(':')]
        
        s = (s[0] * 60) + s[1]
        e = (e[0] * 60) + e[1]
        play_time = e - s
        
        # tmp에 full code를 열거한다.
        tmp = ""
        while play_time > music_time:
            tmp += code
            play_time -= music_time
        tmp += code[:play_time]
        print(tmp)
        
        # tmp 안에 m 이 있다면
        if m in tmp:
            if max_pt < e - s:
                max_pt = e - s
                answer = name
    
    return answer
    
print(solution("ABCDEFG", ["12:00,13:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
