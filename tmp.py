import re

def solution(files):
    
    f = []
    head = ''
    number = ''
    tail = ''
    
    for file in files:
        for i, letter in enumerate(file):
            if re.match('[\d]', letter):
                head = file[:i]
                save = i
                break
        for j, letter2 in enumerate(file[save:]):
            if re.match('[^\d]', letter2):

                number = file[save : save+j]
                tail = file[save+j : ]
                break
        
        f.append([head, number, tail])
        
    f.sort(key = str.lower)
    print(f)
    
    return 0
    
print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
