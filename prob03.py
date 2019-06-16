# 문제3.
#
# 1)다음 문자열을 모든 소문자를 대문자로 변환하고, 문자 ',', '.','\n'를 없앤 후에 중복
# 없이 각 단어를 순서대로 출력하세요.
s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""
s = s.upper()
src = s.replace(',', '').replace('.', '').replace('\n', '').split(' ')
src_set = set(src)
src_dic = {}
for i in range(len(src_set)):
    print(src_set.pop())

for i in range(len(src)):
    tmp = src.pop()
    if tmp in src_dic:
        src_dic[tmp] += 1
        continue
    src_dic[tmp] = 1
print(src_dic)
# s.translate({ord('.'): '', ord(','): '', ord('\n'): ''})
# print(s)
# 실행 결과:
# AFTER
# AVAILABLE
# CONTRIBUTE
# CONTRIBUTORS
# .
# TO
# WE
# YOU



