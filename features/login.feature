# Created by ypochien at 2016/12/1
Feature: 連線登入三竹系統
  為了使用三竹觸價系統
  必須先進行連線與登入


  Scenario: 連線三竹主機
    Given We have Mitake Server 220.128.150.80 8800
    When Connect to Server
    And send ALIVE
    Then ALIVE receive


  Scenario: 登入三竹主機
    Given We have Mitake Server 220.128.150.80 8800
    When Connect to Server
    And 送出登入資訊"SNP"和密碼"SNP1234"
    Then 收到登入成功