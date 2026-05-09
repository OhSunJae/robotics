import polars as pl
import matplotlib.pyplot as plt

def visualize_robot_data():
    # 1. 가상의 로봇 센서 데이터 생성 (실제 로그 파일이 있다면 pl.read_csv 사용)
    data = {
        "timestamp": [i for i in range(100)],
        "force_z": [10 + (i * 0.1) for i in range(100)],
        "torque_x": [5 + (i * 0.05) for i in range(100)]
    }
    df = pl.DataFrame(data)

    # 2. 시각화 설정
    plt.figure(figsize=(10, 5))
    
    # Force 데이터 그래프
    plt.subplot(1, 2, 1)
    plt.plot(df["timestamp"], df["force_z"], label="Force Z", color='blue')
    plt.title("Robot Force (Z-axis)")
    plt.xlabel("Time (ms)")
    plt.ylabel("Newton (N)")
    plt.grid(True)

    # Torque 데이터 그래프
    plt.subplot(1, 2, 2)
    plt.plot(df["timestamp"], df["torque_x"], label="Torque X", color='red')
    plt.title("Robot Torque (X-axis)")
    plt.xlabel("Time (ms)")
    plt.ylabel("Nm")
    plt.grid(True)

    plt.tight_layout()
    print("📊 시각화 그래프를 생성합니다. (GUI 환경인 경우 팝업이 뜹니다)")
    # 실제 터미널 환경에서는 아래 줄을 주석 해제하여 이미지로 저장할 수도 있습니다.
    # plt.savefig("sensor_plot.png")
    plt.show()

if __name__ == "__main__":
    visualize_robot_data()