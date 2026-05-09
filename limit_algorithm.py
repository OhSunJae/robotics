def check_safety_stop(current_distance, safety_limit):
    """
    현재 거리와 안전 제한 거리를 비교하여 정지 여부를 결정합니다.
    """
    if current_distance < safety_limit:
        return "🚨 [DANGER] 거리 너무 가까움! 즉시 정지합니다."
    elif current_distance < safety_limit * 1.5:
        return "⚠️ [WARNING] 주의! 속도를 줄이세요."
    else:
        return "✅ [SAFE] 안전 거리 확보됨. 정상 구동 중."

# 2. 테스트 실행
if __name__ == "__main__":
    # 안전 거리를 20cm로 설정
    limit = 20
    
    # 여러 상황 테스트
    print(f"현재 거리 50cm: {check_safety_stop(50, limit)}")
    print(f"현재 거리 25cm: {check_safety_stop(25, limit)}")
    print(f"현재 거리 15cm: {check_safety_stop(15, limit)}")