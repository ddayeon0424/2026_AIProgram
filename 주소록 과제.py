import json

# 1. 파일 다시 불러오기 (addressbook 파일이 이미 있을 때?)
with open("addressbook.json", "r", encoding="utf-8") as f:
    addressbook = json.load(f)
    
print("불러온 주소록:",addressbook)
print("김영호 번호:",addressbook["김영호"])

# 2.
while True:
    print("\n--- 주소록 메뉴 ---")
    print("1. 연락처 추가")
    print("2. 연락처 삭제 (새 기능)")
    print("0. 종료")
    
    menu = input("메뉴 번호를 입력하세요: ")

    if menu == "1":
        name = input("이름: ")
        phone = input("전화번호: ")
        addressbook[name] = phone
        
        with open("addressbook.json", "w", encoding="utf-8") as f:
            json.dump(addressbook, f, ensure_ascii=False, indent=4)
        print("저장되었습니다.")

    elif menu == "2":
        # [새로운 기능] 삭제하기
        del_name = input("삭제할 이름을 입력하세요: ")
        if del_name in addressbook:
            del addressbook[del_name] # 딕셔너리에서 삭제
            
            # 삭제된 전체 딕셔너리를 파일에 다시 덮어써서 업데이트
            with open("addressbook.json", "w", encoding="utf-8") as f:
                json.dump(addressbook, f, ensure_ascii=False, indent=4)
            print(f"{del_name}님의 연락처가 삭제되었습니다.")
        else:
            print("주소록에 없는 이름입니다.")

    elif menu == "0":
        print("프로그램을 종료합니다.")
        break
