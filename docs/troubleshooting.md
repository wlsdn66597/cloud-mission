# 트러블슈팅: SSH 개인키 파일 권한

| 단계 | 내용 |
|---|---|
| 증상 | Windows PowerShell에서 EC2 접속 시 `bad permissions`, `This private key will be ignored`, `Permission denied (publickey)` 발생 |
| 가설 | 개인키 파일에 다른 사용자의 접근 권한이 있어 SSH가 키 사용을 거부함 |
| 검증 | 오류 문구에서 키 무시를 확인하고 `icacls`로 파일 ACL 확인 |
| 조치 | 파일 ACL을 초기화하고 현재 Windows 사용자에게 읽기 권한 부여 후 상속 권한 제거 |
| 결과 | 이후 `ubuntu@ip-10-0-1-181` 세션에서 Nginx 실행과 내부 `200 OK` 확인 |
| 재발 방지 | 개인키 저장 후 ACL 확인, 사용자별 보관, 개인키·인증 CSV·토큰 Git 업로드 제외 |

## 조치 명령 — PC의 PowerShell

```powershell
$keyPath = "$env:USERPROFILE\Downloads\cloud-mission-key.pem"
$keyUser = [System.Security.Principal.WindowsIdentity]::GetCurrent().Name
icacls.exe $keyPath /reset
icacls.exe $keyPath /grant:r "${keyUser}:(R)"
icacls.exe $keyPath /inheritance:r
icacls.exe $keyPath
ssh -i "$keyPath" ubuntu@3.34.44.74
```

- [조치 전 오류](screenshots/10-ssh-permissions-error.png)
- [조치 후 SSH 세션 및 Nginx 검증](screenshots/06-service.png)

## 추가 사례: 서울 리전 SCP 거부

- **증상:** 서울에서 `ec2:DescribeVpcs`가 `explicit deny in a service control policy`로 실패했다.
- **가설·검증:** IAM 권한 부족과 조직 정책 제한을 구분했다. 실제 SCP의 `RegionFloor` 리전 목록에 `ap-northeast-2`가 없었다.
- **조치:** 해당 목록에 서울을 추가했다.
- **결과:** 이후 서울 `ap-northeast-2c`에 구성된 VPC·Subnet을 확인했다. [구성 결과](screenshots/03-resource-map.png)
- **재발 방지:** 오류의 실행 주체·작업명·정책 종류를 먼저 확인하고, 필요한 리전만 예외에 추가한다.

SCP 조치 전·후 JSON 캡처는 이 제출 폴더에 포함되지 않는다. SSH 사례를 기본 트러블슈팅 증빙으로 사용한다.
