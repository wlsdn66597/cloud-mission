# 리소스 정리 체크리스트

기준: 사용자가 제공한 정리 결과 캡처. 리전은 서울이며, 기존 시드니 리소스는 이 실습의 삭제 대상에 포함하지 않는다. 개별 작업 시각은 캡처에 표시되지 않아 기재하지 않았다.

| 상태 | 대상 | ID·이름 | 확인 근거 |
|---|---|---|---|
| 완료 | EC2 | `i-0e9c852cc502e13e8` | [Terminated 상태](screenshots/11-ec2-terminated.png) |
| 완료 | EBS | 서울 리전 볼륨 목록 | [잔여 볼륨 없음](screenshots/12-ebs-empty.png) |
| 할당 없음 | Elastic IP | 별도 할당 없음 | [서울 리전 EIP 목록 없음](screenshots/13-eip-empty.png) |
| 완료 | VPC | `vpc-09e5a60bb41047b15`, `cloud-mission-vpc` | [해당 VPC 및 기타 4개 리소스 삭제 완료 메시지](screenshots/14-vpc-deleted.png) |
| 개별 확인 필요 | IGW | `igw-0c5813beab7d8332e` | VPC 삭제 메시지는 있으나 세부 목록이 접혀 있어 해당 IGW의 개별 삭제는 직접 확인되지 않음 |

- [x] EC2 종료 상태 확인
- [x] EBS 잔여 없음 확인
- [x] Elastic IP 할당 없음 확인
- [x] 실습 VPC 삭제 완료 확인
- [ ] IGW ID로 검색하여 없음 확인 또는 VPC 삭제 세부 정보에서 해당 IGW 삭제 확인

추가 점검(증빙 미첨부): VPC 삭제에 포함된 Subnet·Route Table·Security Group의 최종 상태, AWS 키페어 `cloud-mission-key` 정리, Billing 및 크레딧 잔액 확인. 스냅샷·NAT Gateway·ALB·RDS를 별도로 생성했다면 해당 리소스도 정리한다.

확인하지 못한 항목은 완료로 표시하지 않았다. VPC 콘솔은 연관된 Subnet·Route Table·Security Group·IGW 등을 함께 삭제할 수 있다. 하지만 첨부 캡처만으로 각 ID의 삭제 결과까지 단정하지 않는다.

Billing에는 이전 사용량이 뒤늦게 반영될 수 있으므로, 비용 표시만으로 잔여 리소스 유무를 판단하지 않는다. 유료 플랜 전환이나 고급 기능 활성화는 리소스 삭제로 원복되지 않는다.
