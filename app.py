def validate_username(username):
    # 아이디는 5자 이상, 영문 소문자만 허용 (간단한 예시)
    return len(username) >= 5 and username.islower()

def validate_password(password):
    # 비밀번호는 8자 이상, 숫자와 특수문자가 최소 1개 포함되어야 함
    has_digit = any(char.isdigit() for char in password)
    return len(password) >= 8 and has_digit and any(not pw.isalnum() for pw in password)

if __name__ == "__main__":
    user = input("아이디 입력: ")
    pw = input("비밀번호 입력: ")
    
    if validate_username(user) and validate_password(pw):
        print("유효성 검사 통과!")
    else:
        print("유효성 검사 실패 (규칙을 확인하세요)")