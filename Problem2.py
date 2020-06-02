#피보나치 수열 400만 이하이면서 짝수인 항의 합
# ex)1 2 3 5 8 13 ...
LIMIT_NUMBER = 4000000 
start_num = 1 
temp_num = 2 
before_num = 2 
result = 2 
while start_num <= LIMIT_NUMBER: 
    start_num = start_num + before_num
    before_num = temp_num
    temp_num = start_num
    if start_num%2==0: result = result + start_num
print(result)