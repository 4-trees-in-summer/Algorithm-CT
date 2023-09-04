def solution(files):
    answer = []

    file_name = []
    
    for file in files:
        start_idx = 0  # start_idx를 루프 안에 초기화
        end_idx = len(file)  # end_idx를 파일 길이로 초기화
        first_time = True
        
        for idx, f in enumerate(file):
            if f.isdigit() and first_time:
                start_idx = idx
                first_time = False
            elif not f.isdigit() and not first_time:
                end_idx = idx
                break
        
        file_name.append((file[:start_idx], file[start_idx:end_idx], file[end_idx:]))
    
    file_name.sort(key=lambda x: (x[0].lower(), int(x[1])))

    for name in file_name:
        answer.append(''.join(name))
        
    return answer
