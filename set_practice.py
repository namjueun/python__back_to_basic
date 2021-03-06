# 집합(set): 
# 중복 안됨(중복값 중 하나의 값만 이용가능), 순서 없음

my_set = {1,2,3,3,3} # dict이랑 다르게 value만 씀
#print(my_set) # 1,2,3

java = {"유재석", "김태호", "양세형"}
python = set(["유재석","박명수"])

# 교집합 (java와 python을 모두 할 수 있는 개발자
# print(java & python)
# print(java.intersection(python))

# 합집합 (java 할 수 있거나 python 할 수 있는 개발자)
# print(java | python) # {'박명수', '양세형', '유재석', '김태호'} -> 순서 상관없이 출력됨
# print(java.union(python))

# 차집합 (java 할 수 있지만 python 할 수 없는 개발자)
# print(java-python)
# print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java를 까먹음
java.remove("김태호")
print(java)