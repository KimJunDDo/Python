#!/usr/bin/env python
# coding: utf-8

# In[4]:


str1 = input("문자열 1: ")
str2 = input("문자열 2: ")

print(str1, str2)


# In[12]:


km = input("차의 속도를 입력(km) >> ")
mile = int(km) / 1.61

print(km+"(km)은", mile, "마일(miles)이다.")


# In[13]:


americano =  input("아메리카노 몇 개 주문하세요? ")
price = int(americano) * 3500

print("총 가격은", price, "이다.")


# In[5]:


Earth =  input("알려진 지구 둘레: ")
Circumference =  input("지구와 같은 원둘레: ")
dis = float(Earth) - float(Circumference)

print("차이: "+str(dis)+"(km)")


# In[10]:


C = input("온도 입력 >> ")
F = float(C) * 9 / 5 + 32
F2 = float(C) * 2 + 30
dis = F - F2
print("정확 계산: 섭씨:", C, ", 화씨:", F, "\n정확 계산: 섭씨:", C, ", 화씨:", int(F2), "\n차이:", dis)


# In[14]:


Fn = input("Enter First number: ")
Sn = input("Enter First number: ")
Fn = int(Fn)
Sn = int(Sn)

div = Fn / Sn
mod = Fn % Sn
fdiv = Fn // Sn
exp = Fn ** Sn

print(Fn, "/", Sn, "==>", div)
print(Fn, "%", Sn, "==>", mod)
print(Fn, "//", Sn, "==>", fdiv)
print(Fn, "**", Sn, "==>", exp)


# In[19]:


Fn = input("첫 번째 16진수 실수 입력 >> ")
Sn = input("두 번째 16진수 실수 입력 >> ")
Fn2 = float.fromhex(Fn)
Sn2 = float.fromhex(Sn)
print("실수1:", Fn2, "실수2:", Sn2)
print("합:", Fn2+Sn2)
print("차:", Fn2-Sn2)
print("곱하기:", Fn2*Sn2)
print("나누기:", Fn2/Sn2)


# In[21]:


N = input("네 자릿수 정수 입력 >> ")
N= int(N)
ReverseN = (N // 1000) + (((N % 1000) // 100) * 10) + (((N % 100) // 10) * 100) + ((N % 10) * 1000)
print(ReverseN)

