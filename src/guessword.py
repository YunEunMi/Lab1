#importing the time module
import time

name = input("플레이어 이름 입력: ")

print("안녕, " + name, " 단어 맞추기 게임입니다.")

print("")

# 1초 대기
time.sleep(1)

print("게임 시작 ...")
# 0.5초 대기
time.sleep(0.5)

# 정답의 초기값 설성
word = "secret"

# 추측 값 전체를 저장하는 변수 생성
guesses = ""

# 전체 시도 횟수(10회) 설정
turns = 10

# while 반복문으로 구현

# 시도 횟수가 0보다 큰지 체크
while turns > 0:         

    # 실폐 횟수를 위한 변수를 0으로 초기화하여 설정
    failed = 0             

    # 정답의 각 문자를 처리   
    for char in word:      

    # 플레이어가 추측(입력)한 문자가 정답에 있는 문자이면
    # 아니면 '_' 문자 출력예상한 문자
        if char in guesses:    
            # 화면에 해당 문자 출력
            print(char, end=" ")    

        else:
            # 아니면 '_' 문자 출력
            print("_", end=" ")     
       
            # 실폐 횟수를 1 증가시킴
            failed += 1    

    # 실폐횟수가 0이면 "당신이 이겼습니다."라는 문자열 출력
    if failed == 0:        
        print("\n당신이 이겼습니다.")  

        # if문을 빠져나감
        break              

    print()

    # 플레이어가 추측 값 입려
    guess = input("예상 문자를 입력하세요:") 

    # 추측(입력) 값 전체에 추측문자 연결
    guesses += guess                    

    # 추축한 문자가 정답 단어에 없다면i
    if guess not in word:  
 
        # 시도 횟수를 1 감소시킴
        turns -= 1        
 
        # 추측 값이 잘못됐다는 "없음" 문자열 출력
        print("없음")    
 
        # 몇 번의 시도 횟수가 남아있는지 출력
        print("당신은 ", + turns, "번 더 추측할 수 있습니다.") 
 
        # 시도횟수가 0과 같으면
        if turns == 0:           
    
            # 플레이어가 졌다는 의미에서 "당신이 졌습니다." 문자열 출력
            print("당신이 졌습니다.")
