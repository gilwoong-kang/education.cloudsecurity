### VM

![IMG_F0E103EA54AA-1](/Users/gilwoongkang/서재/skinfosec-edu/image/IMG_F0E103EA54AA-1.jpeg)

## Linux

### 리눅스 역사

Unix에서 유래. *Linus Torvalds* 가 미닉스 OS를 사용하는 컴퓨터에서 작업하여 만들었다. 미닉스의 불편한 점에 대해 커널에 기능을 추가하고 이것이 새 OS에 가까울 정도로 기능이 늘어났다. 

2000년대 초, 2010년 붐을 겪으며 Unix에서 Linux로의 세대 전환이 이루어졌다. 리눅스는 GPL 정책을 따른다.

> GPL(General public License) : 조건적 무료. 변경 및 재판매가 가능하나 반드시 소스코드를 공개해야 한다. 

### 리눅스 소개

패키지 제어 SW차이에 따라 크게 네가지로 나뉜다.

- RedHat 계열 : fedora, **centOS**
- slackware : 초기 linux, **openSUSE**
- Debian : **ubuntu**, 가장 unix에 가까운 특징.
- mandrake : 현재 mandriva로 변경

#### OS의 주요 구성 요소

- shell : 명령 해석기. Shell 명령을 file로 작성해서 이용한 것을 shell script라고 한다.

- kernal : OS 핵심 기능을 모듈로 프로그래밍 한것.

  > I/O 통신 프로그램을 Driver라고 한다.

- File system : 리눅스는 multi-user system. 디스크를 공유한다. OS와 관련된 Directory는 권한을 제한해 이용한다. 

운영체제 핵심 기능은 커널에 구성. 사용자와 Interactive하게 처리하기 위해 shell이 존재. 사용자는 shell을 통해 시스템을 제어하고 운용한다. 

결과 등 저장단위는 주로 file. 이 file을 관리하기 위해 file System이 필요하다.

### 리눅스 로그인/로그아웃

> Id,pwd,ps,who,finger : 각종 명령어
>
> su - 사용자 ID : 사용자 전환. 

> 리눅스 명령어는 일반적으로 다음 형식을 따른다.
>
> ```shell
> $command options argument
> ```

> exit으로 로그하웃 가능하다. (or Ctrl + D)

### 파일 구성요소

- File name
- inode : 메타 데이터가 저장된다.
- Data block : 실제 데이터로 이루어지며 접근을 위해 주로 메타데이터가 필요하다.

> 파일 네임 규칙은 다음을 따른다. 
>
> - 대,소문자,숫자,#,@,_
> - 그외 메타 캐릭터는 사용 불가.
> - +/-로 시작불가
> - 시스템 명령과 같은 이름으로 사용 불가
> - .으로 시작시 숨겨진 파일 -> ls -a 로 볼 수 있다.
> - 최대 255자 이내

#### 파일 유형

파일 유형은 다음과 같다

- Regular 파일 : -
- Directory : d
- Symbolic link : l
- Device : c | b

> ls -li 와 같은 명령어로 권한을 볼 수 있는데, 맨 앞자리에 나오는 캐릭터의 종류에 따라 파일 유형을 구분 할 수 있다.

#### 디렉토리 관련 명령

ls,find,pwd,mkdir,cp,mv,ln,cd,rm,rmdir

> F 옵션을 넣으면 기호가 추가되어 보인다.
>
> \를 명령어 앞에 넣으면 alias를 무시하고 실행한다. 

#### 상대경로

상대경로란 현재 위치에 기반하여 path를 추적하는 경로. 주로 . 이나 .. 을 이용. 

- . : 현재 디렉토리
- .. : 상위 디렉토리 

#### 절대경로

어디에서나 동일한 절대 경로. 처음부터 끝까지 완전한 path를 입력해야 한다.

#### 파일 관련 명령

Cat, more,string,head,tail,grep,touch,cp,mv,ln,vi,rm

> 파일의 데이터 유형을 모른다면 file명령을 통해 데이터 유형을 파악하는 것을 권장.

cp,rm,mv 등 명령어로 이동 복사 제거 행위가 가능하다.

#### 링크 파일 (a.k.a 바로가기)

- Symbolic link : 파일을 참조함. 링크 파일에 대해 inode가 별도로 생성된다.
- Hard link : inode를 직접 참조한다. inode를 호출해보면 같은것이 나온다.

### Shell

OS와 사용자 사이에서 interface를 제공하는 컴파일 된 프로그램. 명령 해석의 역할 등을 수행한다.

> shell의 parse순서가 있으니 주의

#### 파일 이름 대체 메타문자

- \* : 뭐든으로 앞 또는 뒤에 오며 해당 문자로 시작하거나 끝에 오는 모든 파일을 지칭한다. ex) f*
- ? : 한 캐릭터에 대해 any. Ex) dir?
- [] : 범위를 지정해준다. Ex) [a-f]*

#### Redirect (>,>>,<)

타 지정 출력 등을 위해 리다이렉트. 모니터 출력이 아닌 파일 저장등의 행위를 취할 수 있다.

- 입력 : <
- 출력 : >, >> 

#### Filter(|)

앞에 수행한 명령 기반으로 뒷 명령 수행. 뒤에오는 명령은 표준 입력을 요하는 명령만 가능하다.

