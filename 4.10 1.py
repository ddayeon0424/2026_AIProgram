import json
'''
# 주소록 데이터
adressbook = {
    "김영호": "01047278728",
    "이다연": "01094649107"
    }

# 1. 파일로 저장
with open("addressbook.json", "w", encoding="utf-8") as f:
    json.dump(addressbook, f, ensure_ascii=False, indent=4)

print("주소록이 저장되었습니다.")
'''
# 2. 파일에서 다시 불러오기
with open("addressbook.json", "r", encoding="utf-8") as f:
    addressbook = json.load(f)

print("불러온 주소록:",addressbook)
print("김영호 번호:",addressbook["김영호"])
