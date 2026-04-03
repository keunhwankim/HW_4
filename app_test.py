from app import validate_username, validate_password

def run_tests():
    print("테스트 시작...")

    # 1. 아이디 테스트
    assert validate_username("tester123") == True, "아이디 유효성 검사 실패!"
    assert validate_username("test") == False, "짧은 아이디 통과 오류!"

    # 2. 비밀번호 테스트
    assert validate_password("pass12345!") == True, "비밀번호 유효성 검사 실패!"
    assert validate_password("pass12345") == False, "숫자 없는 비밀번호 통과 오류!"

    print("✅ 모든 테스트 통과!")

if __name__ == "__main__":
    run_tests()