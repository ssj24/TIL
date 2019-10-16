[TOC]

# SQL과 django ORM

## 기본 준비 사항

```bash
# 폴더구조

TIL
	00_StartCamp
	...
	04_db
		00_sql # only SQL
			hellodb.csv
			tutorial.sqlite3
			users.csv
		01_sql_orm # SQL + ORM
			...
			users.csv # 해당 디렉토리로 다운로드
```

* django app

  * 가상환경 세팅

  * django project : `sql`

  * django app : `users`

  * `django_extensions` 설치 및 등록

  * users.csv 파일에 맞춰 `models.py` 작성 및 migratation

    ```python
    # users/models.py
    
    from django.db import models
    
    class User(models.Model):
        first_name = models.CharField(max_length=10)
        last_name = models.CharField(max_length=10)
        age = models.IntegerField()
        country = models.CharField(max_length=10)
        phone = models.CharField(max_length=15)
        balance = models.IntegerField()
    ```

    ```bash
    $ python manage.py makemigrations
    $ python manage.py migrate 
    ```

    아래의 명령어를 통해서 실제 쿼리문 확인

    ```bash
    $ python manage.py sqlmigrate users 0001
    ```

* `db.sqlite3` 활용

  * `sqlite3`  실행

    ```bash
    $ ls
    db.sqlite3 manage.py ...
    $ sqlite3 db.sqlite3
    ```

  * csv 파일 data 로드

    ```sqlite
    sqlite > .tables
    auth_group                  django_admin_log
    auth_group_permissions      django_content_type
    auth_permission             django_migrations
    auth_user                   django_session
    auth_user_groups            auth_user_user_permissions  
    users_user
    sqlite > .mode csv
    sqlite > .import users.csv users_user
    sqlite > SELECT COUNT(*) FROM user_users;
    100
    ```

* 확인

  * sqlite3에서 스키마 확인

    ```sqlite
    sqlite > .schema users_user
    CREATE TABLE IF NOT EXISTS "users_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "first_name" varchar(10) NOT NULL, "last_name" varchar(10) NOT NULL, "age" integer NOT NULL, "country" varchar(10) NOT NULL, "phone" varchar(15) NOT NULL, "balance" integer NOT NULL);
    ```



---



## 문제

> 아래의 문제들을 보면서 서로 대응되는 ORM문과 SQL문을 작성하시오.
>
> **vscode 터미널을 좌/우로 나누어 진행하시오. (sqlite / shell_plus)**

`.headers on` 을 켜고 작성해주세요.



### 1. 기본 CRUD 로직

1. 모든 user 레코드 조회

   ```python
   # orm
   # 장고 익스텐션 설치한 뒤에 settings.py에 django_extensions추가하고
   # pip install iPython
   # python manage.py shell_plus
   User.objects.all()
   ```

      ```sql
   -- sql
   sqlite> SELECT * FROM users_user;
      ```

2. user 레코드 생성

   ```python
   # orm
   In [3]: user = User(id=101, first_name='수지', last_name='조', age=28, country='한국', phone='123-456-7890')
   
   In [4]: user.full_clean()
   -----------------------------------------------------
   ValidationError     Traceback (most recent call last)
   <ipython-input-4-b0f23f12253c> in <module>
   ----> 1 user.full_clean()
   
   ~\Desktop\push\TIL\04_DB\01_sql_orm\venv\lib\site-packages\django\db\models\base.py in full_clean(self, exclude, validate_unique)
      1201
      1202         if errors:
   -> 1203             raise ValidationError(errors)
      1204
      1205     def clean_fields(self, exclude=None):
   
   ValidationError: {'balance': ['이 필드는 null 값을 사
   용할 수 없습니다. ']}
   
   --------------------------------------------------------------------
   
   In [5]: user = User(id=101, first_name='수지', last_
      ...: name='조', age=28, country='한국', phone='12
      ...: 3-456-7890', balance=1000000)
   
   In [6]: user.full_clean()
   -----------------------------------------------------
   ValidationError     Traceback (most recent call last)
   <ipython-input-6-b0f23f12253c> in <module>
   ----> 1 user.full_clean()
   
   ~\Desktop\push\TIL\04_DB\01_sql_orm\venv\lib\site-packages\django\db\models\base.py in full_clean(self, exclude, validate_unique)
      1201
      1202         if errors:
   -> 1203             raise ValidationError(errors)
      1204
      1205     def clean_fields(self, exclude=None):
   
   ValidationError: {'id': ['User의 ID은/는 이미 존재합
   니다.']}
   
   --------sql에서 101을 미리 생성했기 때문.
                            
                            
   In [7]: user = User(id=102, first_name='수지', last_
      ...: name='조', age=28, country='한국', phone='12
      ...: 3-456-7890', balance=1000000)
   
   In [8]: user.full_clean()
   
   In [9]: user.save() 
   ```

   ```sql
   -- sql
   sqlite> INSERT INTO users_user VALUES(101, '수지', 28, '한국', '123-456-7890');
   Error: table users_user has 7 columns but 5 values were supplied
   
   --------------------------------------------------------------------
   
   sqlite> INSERT INTO users_user VALUES(101,'수지', '조', 28, '한국', '123-456-7890',
    1000000);
   
   ```

   * 하나의 레코드를 빼고 작성 후 `NOT NULL` constraint 오류를 orm과 sql에서 모두 확인 해보세요.

3. 해당 user 레코드 조회

   - `101` 번 id의 전체 레코드 조회

   ```python
   # orm
   In [10]: User.objects.get(id=101)
   Out[10]: <User: User object (101)>
   ```

   ```sql
   -- sql
   sqlite> SELECT * FROM users_user WHERE id=101;
   id,first_name,last_name,age,country,phone,balance
   101,"수지","조",28,"한국",123-456-7890,1000000
   ```

4. 해당 user 레코드 수정

   - ORM: `101` 번 글의 `last_name` 을 '김' 으로 수정
   - SQL: `101` 번 글의 `first_name` 을 '철수' 로 수정

   ```python
   # orm
   In [12]: user = User.objects.get(pk=101)
   
   In [13]: user.last_name='김'
   
   In [14]: user.save()
   
   ```

      ```sql
   -- sql
   sqlite> UPDATE users_user SET first_name='철수';
   sqlite> SELECT * FROM users_user WHERE id=101;
   id,first_name,last_name,age,country,phone,balance
   101,"철수","김",28,"한국",123-456-7890,1000000
      ```

5. 해당 user 레코드 삭제

   - ORM: `101` 번 글 삭제
   - `SQL`:  `101` 번 글 삭제 (ORM에서 삭제가 되었기 때문에 아무런 응답이 없음)

   ```python
   # orm
   In [15]: user = User.objects.get(pk=101)

   In [16]: user.delete()
   Out[16]: (1, {'users.User': 1})
   ```
   
   ```sql
   -- sql
   sqlite> DELETE FROM users_user WHERE id=101;
   sqlite> SELECT * FROM users_user WHERE id=101;
   ```



---



### 2. 조건에 따른 쿼리문

1. 전체 인원 수 

   - `User` 의 전체 인원수

   ```python
   # orm
   In [18]: from django.db.models import Count
   In [20]: User.objects.count()
   Out[20]: 101
   ```

   ```sql
   -- sql
   sqlite> SELECT COUNT(*) FROM users_user;
   COUNT(*)
   101
   -- 아이디 생성 단계에서 orm은 101, sql은 102를 생성한 후 101을 지웠기 때문.
   ```

2. 나이가 30인 사람의 이름

   - `ORM` : `.values` 활용
     - 예시: `User.objects.filter(조건).values(컬럼이름)`

   ```python
   # orm
   In [21]: User.objects.filter(age=30).values('first_name')
   Out[21]: <QuerySet [{'first_name': '철수'}, {'first_name': '철수'}, {'first_name': '철수'}]>
   ```

      ```sql
   -- sql
   sqlite> SELECT first_name FROM users_user WHERE age = 30;
   first_name
   "철수"
   "철수"
   "철수"
      ```

3. 나이가 30살 이상인 사람의 인원 수

   -  ORM: `__gte` , `__lte` , `__gt`, `__lt` -> 대소관계 활용

   ```python
   # orm
   In [23]: User.objects.filter(age__gte=30).count()
   Out[23]: 43
   ```

      ```sql
   -- sql
   sqlite> SELECT COUNT(*) FROM users_user WHERE age >= 30;
   COUNT(*)
   43
      ```

4. 나이가 20살 이하인 사람의 인원 수 

   ```python
   # orm
   In [24]: User.objects.filter(age__lte=20).count()
   Out[24]: 23
   ```

   ```sql
   -- sql
   sqlite> SELECT COUNT(*) FROM users_user WHERE age <= 20;
   COUNT(*)
   23
   ```

5. 나이가 30이면서 성이 김씨인 사람의 인원 수

   ```python
   # orm
   In [25]: User.objects.filter(age=30, last_name='김').count()
   Out[25]: 1
   ```

      ```sql
   -- sql
   sqlite> SELECT COUNT(*) FROM users_user WHERE age = 30 and last_name='김';
   COUNT(*)
   1
      ```

6. 나이가 30이거나 성이 김씨인 사람?

   ```python
   # orm
   In [26]: from django.db.models import Q
   
   In [27]: User.objects.filter(Q(age=30) | Q(last_name='김'))
   Out[27]: <QuerySet [<User: User object (5)>, <User: User object (8)>, <User: User object (9)>, <User: User object (11)>, <User: User object (14)>, <User: User
   object (16)>, <User: User object (18)>, <User: User object (19)>, <User: User object (20)>, <User: User object (23)>, <User: User object (32)>, <User: User object (46)>, <User: User object (47)>, <User: User object (57)>, <User: User object (60)>, <User: User object (62)>, <User: User object (70)>, <User: User object (78)>, <User: User object (82)>, <User: User object
   (85)>, '...(remaining elements truncated)...']>
   ```

   ```sql
   -- sql
   sqlite> SELECT * FROM users_user WHERE age = 30 or last_name='김';
   id,first_name,last_name,age,country,phone,balance
   5,"철수","차",30,"충청북도",011-2921-4284,220
   8,"철수","김",33,"충청북도",010-5123-9107,3700
   9,"철수","김",23,"제주특별자치도",016-6839-1106,43000
   11,"철수","김",15,"제주특별자치도",016-3046-9822,640000
   14,"철수","김",35,"전라남도",011-4448-6198,720
   16,"철수","김",19,"경상남도",011-1038-5964,720
   18,"철수","김",17,"충청북도",016-4058-7601,94000
   19,"철수","김",26,"충청남도",011-6897-4723,6100
   20,"철수","김",17,"경기도",016-1159-3227,590
   23,"철수","김",26,"강원도",02-4610-2333,6900
   32,"철수","김",38,"전라북도",016-3075-6557,950000
   46,"철수","김",23,"전라남도",011-3545-5608,330
   47,"철수","김",37,"경상남도",02-3446-1832,920
   57,"철수","안",30,"제주특별자치도",010-6132-4229,68000
   60,"철수","김",30,"경상북도",02-5110-2334,350
   62,"철수","김",31,"충청북도",016-3755-6794,8100
   70,"철수","김",24,"제주특별자치도",016-4846-2896,1000000
   78,"철수","김",37,"경상북도",02-7295-4461,860
   82,"철수","김",39,"충청북도",02-8468-8321,680000
   85,"철수","김",33,"강원도",010-7554-1154,63000
   86,"철수","김",38,"전라남도",016-6487-9185,73000
   87,"철수","김",19,"전라북도",011-4100-7281,89000
   91,"철수","김",39,"경상남도",011-5298-5280,6600
   97,"철수","김",38,"충청남도",016-7677-2212,81000
   100,"철수","김",25,"경상북도",016-1252-2316,210
   ```

7. 지역번호가 02인 사람의 인원 수

   - `ORM`: `__startswith` 

   ```python
   # orm
   In [5]: User.objects.filter(phone__startswith='02-').count()
   Out[5]: 24
   ```

      ```sql
   -- sql
   sqlite> SELECT COUNT(*) FROM users_user WHERE phone LIKE '02-%';
   24
      ```

8. 거주 지역이 강원도이면서 성이 황씨인 사람의 이름

   ```python
   # orm
   In [7]: User.objects.filter(country='강원도', last_name='황').values('first_name')
Out[7]: <QuerySet [{'first_name': '철수'}]>
   # values의 괄호 안에서는 ''를 써줘야한다.
   ```
   
      ```sql
   -- sql
   sqlite> SELECT first_name FROM users_user WHERE country='강원도' and last_name='황';
   "철수"
      ```



---



### 3. 정렬 및 LIMIT, OFFSET

1. 나이가 많은 사람순으로 10명

   ```python
   # orm
   In [8]: User.objects.order_by('-age')[:10]
   Out[8]: <QuerySet [<User: User object (1)>, <User: User object (4)>, <User: User object (28)>, <User: User object (53)>, <User: User object (65)>, <User: User object (26)>, <User: User object (55)>, <User: User object (58)>, <User: User object (74)>, <User: User object (82)>]>
   ```

      ```sql
   -- sql
   sqlite> SELECT * FROM users_user ORDER BY age DESC LIMIT 10;
   1,"철수","유",40,"전라북도",016-7280-2855,370
   4,"철수","장",40,"충청남도",011-9079-4419,250000
   28,"철수","박",40,"경상남도",011-2884-6546,580000
   53,"철수","홍",40,"전라북도",016-7698-6684,550
   65,"철수","송",40,"경기도",011-9812-5681,51000
   26,"철수","이",39,"경상북도",016-2645-6128,400000
   55,"철수","이",39,"경기도",02-6697-3997,890000
   58,"철수","배",39,"전라남도",010-3486-8085,280000
   74,"철수","배",39,"강원도",010-4833-9657,840
   82,"철수","김",39,"충청북도",02-8468-8321,680000
      ```

2. 잔액이 적은 사람순으로 10명

   ```python
   # orm
   In [9]: User.objects.order_by('balance')[:10]
   Out[9]: <QuerySet [<User: User object (99)>, <User: User object (48)>, <User: User object (100)>, <User: User object (5)>, <User: User object (24)>, <User: User object (61)>, <User: User object (92)>, <User: User object (46)>, <User: User object (38)>, <User: User object (60)>]>
   ```

      ```sql
   -- sql
   sqlite> SELECT * FROM users_user ORDER BY balance LIMIT 10;
   99,"철수","성",32,"전라북도",010-7636-4368,150
   48,"철수","이",28,"강원도",02-2055-4138,210
   100,"철수","김",25,"경상북도",016-1252-2316,210
   5,"철수","차",30,"충청북도",011-2921-4284,220
   24,"철수","권",33,"경상남도",016-4610-3200,230
   61,"철수","고",15,"경상북도",011-3124-1126,300
   92,"철수","박",35,"경상북도",010-5203-5705,300
   46,"철수","김",23,"전라남도",011-3545-5608,330
   38,"철수","심",28,"충청북도",016-6703-7656,340
   60,"철수","김",30,"경상북도",02-5110-2334,350
      ```

3. 잔고는 오름차순, 나이는 내림차순으로 10명?

      ```python
   # orm
   In [10]: User.objects.order_by('balance', '-age')[:10]
Out[10]: <QuerySet [<User: User object (99)>, <User: User object (48)>, <User: User object (100)>, <User: User object (5)>, <User: User object (24)>, <User: User object (92)>, <User: User object (61)>, <User: User object (46)>, <User: User object (38)>, <User: User object (60)>]>
   ```
   
   ```sql
   -- sql
   sqlite> SELECT * FROM users_user ORDER BY balance ASC, age DESC LIMIT 10;
   99,"철수","성",32,"전라북도",010-7636-4368,150
   48,"철수","이",28,"강원도",02-2055-4138,210
   100,"철수","김",25,"경상북도",016-1252-2316,210
   5,"철수","차",30,"충청북도",011-2921-4284,220
   24,"철수","권",33,"경상남도",016-4610-3200,230
   92,"철수","박",35,"경상북도",010-5203-5705,300
   61,"철수","고",15,"경상북도",011-3124-1126,300
   46,"철수","김",23,"전라남도",011-3545-5608,330
   38,"철수","심",28,"충청북도",016-6703-7656,340
   60,"철수","김",30,"경상북도",02-5110-2334,350
   ```
   
4. 성, 이름 내림차순 순으로 5번째 있는 사람

   ```python
   # orm
   In [11]: User.objects.order_by('-last_name', '-first_name')[4]
Out[11]: <User: User object (67)>
   ```
   
      ```sql
   -- sql
   sqlite> SELECT * FROM users_user ORDER BY last_name DESC, first_name DESC LIMIT 1 OFFSET 4;
   67,"철수","허",28,"충청북도",016-4392-9432,82000
      ```



---



### 4. 표현식

> ORM: `aggregate` 사용
>
> https://docs.djangoproject.com/en/2.2/topics/db/aggregation/#aggregation
>
> - '종합', '합계' 등의 사전적 의미
> - 특정 필드 전체의 합, 평균 등을 계산할 때 사용

1. 전체 평균 나이

   ```python
   # orm
   In [12]: from django.db.models import Avg
       
   In [13]: User.objects.all().aggregate(Avg('age'))
   Out[13]: {'age__avg': 28.22772277227723}
   ```

      ```sql
   -- sql
   sqlite> SELECT AVG(age) FROM users_user;
   28.2277227722772
      ```

2. 김씨의 평균 나이

   ```python
   # orm
   In [14]: User.objects.filter(last_name='김').aggregate
       ...: (Avg('age'))
   Out[14]: {'age__avg': 28.782608695652176}
   ```

      ```sql
   -- sql
   sqlite> SELECT AVG(age) FROM users_user WHERE last_name='김';
   28.7826086956522
      ```

3. 강원도에 사는 사람의 평균 계좌 잔고

   ```python
   # orm
   In [15]: User.objects.filter(country='강원도').aggregate(Avg('balance'))
   Out[15]: {'balance__avg': 157895.0}
   ```

   ```sql
   -- sql
   sqlite> SELECT AVG(balance) FROM users_user WHERE country='강원도';
   157895.0
   ```

4. 계좌 잔액 중 가장 높은 값

   ```python
   # orm
   In [16]: from django.db.models import Max
   
   In [17]: User.objects.all().aggregate(Max('balance'))
   Out[17]: {'balance__max': 1000000}
   ```

      ```sql
   -- sql
   sqlite> SELECT MAX(balance) FROM users_user;
   1000000
      ```

5. 계좌 잔액 총액

   ```python
   # orm
   In [18]: from django.db.models import Sum

   In [19]: User.objects.all().aggregate(Sum('balance'))
   Out[19]: {'balance__sum': 15425040}
   ```
   
      ```sql
   -- sql
   sqlite> SELECT SUM(balance) FROM users_user;
   15425040
      ```