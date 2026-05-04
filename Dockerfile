# 로보틱스 및 AI 개발 환경 구성을 위한 Dockerfile
FROM python:3.10-slim

# 시스템 필수 패키지 설치
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

# 로보틱스 핵심 라이브러리 설치 (Polars, PyTorch 등)
RUN pip install --no-cache-dir \
    polars \
    numpy \
    torch \
    matplotlib

COPY . .

CMD ["python", "robot_sensor_processor.py"]