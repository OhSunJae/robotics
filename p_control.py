import time

def run_robot_p_control(target_pos, current_pos, kP):
    """
    target_pos: 목표 위치 (예: 팔 각도 90도)
    current_pos: 현재 위치
    kP: 제어 상수 (얼마나 강하게 밀어줄 것인가)
    """
    print(f"🎯 목표 설정: {target_pos}도 / 현재 위치: {current_pos}도")
    
    # 로봇이 목표에 도달할 때까지 반복 (실전에서는 무한루프나 타이머 사용)
    for step in range(10):
        # 1. 오차(Error) 계산
        error = target_pos - current_pos
        
        # 2. 제어량(Output) 결정: 오차에 비례해서 힘을 준다!
        # 오차가 크면 세게 밀고, 오차가 작아지면 살살 민다.
        output_power = kP * error
        
        # 3. 로봇 이동 (실제로는 모터에 전압을 보냄)
        current_pos += output_power
        
        print(f"Step {step+1}: 현재 위치 {current_pos:.2f}도 (주는 힘: {output_power:.2f})")
        
        # 목표에 거의 도달하면 정지
        if abs(error) < 0.1:
            print("✨ 목표 도달 완료!")
            break
            
        time.sleep(0.1)

if __name__ == "__main__":
    # kP가 너무 크면 튕겨나가고, 너무 작으면 느리게 움직입니다.
    run_robot_p_control(target_pos=90, current_pos=0, kP=0.5)