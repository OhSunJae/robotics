import polars as pl
import numpy as np

def process_robot_telemetry(file_path):
    # Pandas보다 5~10배 빠른 Polars로 로봇 로그 로드
    df = pl.read_csv(file_path)
    
    # 1. 노이즈 제거를 위한 이동평균 (Rolling Mean)
    # 2. 센서 임계치 기반 이상치 필터링
    processed = df.with_columns([
        pl.col("force_z").rolling_mean(window_size=5).alias("smooth_force_z"),
        (pl.col("torque_x") * 0.98).alias("calibrated_torque_x")
    ]).filter(pl.col("is_active") == True)
    
    return processed

# 예시 데이터 생성 및 실행
if __name__ == "__main__":
    print("🚀 Processing Robot Sensor Data with Polars...")
    # 실제 로봇 구동 로그 처리 로직 작성