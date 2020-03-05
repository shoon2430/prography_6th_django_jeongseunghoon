# 프로그라피 6기 Django 사전과제


heroku : https://shoon2430.herokuapp.com/

 * 필수 요구사항
   * 게시물 목록을 반환하는 API를 개발 
   * 게시물의 ID, 제목, 내용, 작성날짜 필수
   * 게시물 목록은 게시물 작성 날짜를 기준으로 최신 날짜로 정렬하세요.
   * 게시물 상세 정보를 반환하는 API를 개발
   
 * 선택 요구사항
   * 본인이 작성한 API를 서버에 배포
   * 게시물 목록, 상세, 작성, 수정, 삭제에 사용자 권한을 추가로 적용
   * 실제 필요한 기능이라고 상상하고 필요한 것들은 가정하여 구현
   
* 토큰(token_jwt)
  ```
  token/          토큰 발급
  token/verify/   토큰 갱신
  token/refresh/  토큰 확인
  ```

* 사용자(user)

  ```
  registration/      사용자등록(회원가입)
  api/v1/users/      사용자 조회 
  api/v1/users/{id}/ 사용자 상세 조회/수정/삭제
  api/v1/users/{id}/password/ 사용자 비밀번호 변경
  ```

* 게시물(post)
  ```
  api/v1/posts/     게시물 조회/등록
  api/v1/posts/{id} 게시물 상세 조회/수정/삭제
  ```

* 댓글(comment)
  ```
  api/v1/posts/comments/ 전체 댓글 조회
  api/v1/posts/{id}/comments/ 해당 게시물의 댓글 조회/등록
  api/v1/posts/{post_id}/comments/{comment_id}/ 게시물 상세 조회/수정/삭제
  ```
