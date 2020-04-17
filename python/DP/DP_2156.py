n = int(input())
value = [0] * n
m_value = [0] * n
for i in range(n):
    value[i] = int(input())

if n == 2:
    m_value[0] = value[0]
    m_value[1] = max(value[1], value[0] + value[1])
elif n == 1:
    m_value[0] = value[0]
else:
    m_value[0] = value[0]
    m_value[1] = max(value[1], value[1] + value[0])
    m_value[2] = max(value[0] + value[2], value[1] + value[2])
    m_value[2] = max(m_value[2], m_value[1])

for i in range(3,n):
    m_value[i] = max(m_value[i-3]+value[i-1]+value[i], m_value[i-2]+ value[i])
    m_value[i] = max(m_value[i-1], m_value[i])
print(m_value[n-1])