# Django Post REST Api 

heroku : https://shoon2430.herokuapp.com/

 * 모델
    * 토큰(token_jwt)
      ```
      token/          토큰 발급
      token/verify/   토큰 갱신
      token/refresh/  토큰 확인
      ``` 
    * 사용자(user)
      * 사용자는 user와 manager권한으로 구분합니다. 
      ```
      registration/      사용자등록(회원가입)
      api/v1/users/      사용자 조회 (토큰인증 + manager권한) 
      api/v1/users/{id}/ 사용자 상세 조회/수정/삭제    (토큰인증 + user권한은 자기자신만, manager는 전부가능)
      api/v1/users/{id}/password/ 사용자 비밀번호 변경 (토큰인증 + user권한은 자기자신만, manager는 전부가능)
      ```

    * 게시물(post)
      ```
      api/v1/posts/     게시물 조회/등록 (조회는 인증 필요없음) (등록은 토큰 인증)
      api/v1/posts/{id} 게시물 상세 조회/수정/삭제 (토큰인증 + user권한은 본인게시물만, manager는 전부가능)
      ```

    * 댓글(comment)
      ```
      api/v1/posts/comments/ 전체 댓글 조회 (인증 필요없음)
      api/v1/posts/{id}/comments/ 해당 게시물의 댓글 조회/등록 (토큰인증 + user권한은 본인댓글만, manager는 전부가능)
      api/v1/posts/{post_id}/comments/{comment_id}/ 게시물 상세 조회/수정/삭제 (토큰인증 + user권한은 본인댓글만, manager는 전부가능)
     
     ```
  * 감사합니다.
    
     
  
      
