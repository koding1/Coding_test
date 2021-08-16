def solution(record):
    answer = []
    
    action_save = {"Enter" : "님이 들어왔습니다.",
                    "Leave" : "님이 나갔습니다.",
                    "Change" : "표시하지 않음"
    }
    
    user_data = {}
    logs = []
    
    for i in record:
        data = i.split(' ')
        
        # action = data[0]
        # user_id = data[1]
        # nickname = data[2]
        
        if len(data) > 2:
            user_data[data[1]] = data[2]
        
        if data[0] != "Change":
            logs.append([data[1], action_save[data[0]]])

    for index, log in enumerate(logs):
        logs[index] = user_data[log[0]] + log[1] 
    
    return logs
    
    
print(solution(["Enter uid1234 Muzi", 
                "Enter uid4567 Prodo",
                "Leave uid1234",
                "Enter uid1234 Prodo",
                "Change uid4567 Ryan"]))
