# 점수가 80점 이상이면 함격입니다.를 출력하고 80점 미만이면 아쉽습니다. 다시 도전해주세요를 출력하는 프로그램 if문 두개 사용

score = int(input('점수를 입력하세요 : '))

if score >= 80:
    print('합격입니다.')

if score < 80:

    print('아쉽습니다. 다시 도전해주세요')

# 시나리오는 충족하지만 if~else문을 사용하면 if문의 중복을 보완할 수 있다.