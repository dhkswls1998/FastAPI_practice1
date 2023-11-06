# 데이터베이스 연결 엔진
from sqlalchemy import create_engine
# 세션생성기
from sqlalchemy.orm import declarative_base, sessionmaker
# 세션클래스
from sqlalchemy.orm import Session

# 현재 디렉토리에 test.db 생성
DATABASE_URL = "sqlite:///./test.sqlite"

# 데이터베이스 연결 엔진 생성하고 test.sqlite 에 연결
engine = create_engine(DATABASE_URL)

# 세션생성기 정의 : 세션의 자동 커밋 및 자동 플러시 비활성화
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 기본클래스 Base 초기화
Base = declarative_base()

# 데이터베이스 연결 유지
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()