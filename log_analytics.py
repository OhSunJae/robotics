import polars as pl
import numpy as np

def analyze_robot_logs():
    # 1. 가상의 대량 로그 데이터 생성 (10,000개 데이터)
    print("⏳ 데이터 생성 중...")
    data = {
        "timestamp": np.arange(0, 10000),
        "motor_temp": np.random.normal(50, 5, 10000),  # 평균 50도, 표준편차 5
        "torque_val": np.random.normal(15, 2, 10000)   # 평균 15Nm, 표준편차 2
    }
    
    # 의도적으로 이상치(과부하) 주입
    df = pl.DataFrame(data)
    df = df.with_columns([
        pl.when(pl.col("timestamp") == 500).then(80.0).otherwise(pl.col("torque_val")).alias("torque_val")
    ])

    # 2. Polars를 이용한 고속 분석
    print("🚀 분석 시작 (Polars High-Speed Engine)")
    
    # (1) 이상치 감지: 토크 수치가 평균에서 크게 벗어난 지점 찾기 (예: 30Nm 이상)
    overload_incidents = df.filter(pl.col("torque_val") > 30)
    
    # (2) 구간별 요약: 1000개 로우(Row) 단위로 평균 온도와 최대 토크 계산
    summary = df.with_columns(
        (pl.col("timestamp") // 1000).alias("time_group")
    ).group_by("time_group").agg([
        pl.col("motor_temp").mean().alias("avg_temp"),
        pl.col("torque_val").max().alias("max_torque")
    ]).sort("time_group")

    # 3. 결과 출력
    print("\n[🚨 과부하 발생 지점]")
    print(overload_incidents)
    
    print("\n[📊 구간별 데이터 요약]")
    print(summary)

if __name__ == "__main__":
    analyze_robot_logs()