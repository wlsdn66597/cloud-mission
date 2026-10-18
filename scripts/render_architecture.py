"""Render the architecture from the submitted lab evidence (no cloud access)."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
FONT = Path("C:/Windows/Fonts/malgun.ttf")
BOLD = Path("C:/Windows/Fonts/malgunbd.ttf")
img = Image.new("RGB", (1800, 1000), "white")
d = ImageDraw.Draw(img)
INK, BLUE, PURPLE = "#172b4d", "#2463eb", "#8054c7"


def text(x, y, value, size=28, color=INK, bold=False):
    font = ImageFont.truetype(str(BOLD if bold else FONT), size)
    d.text((x, y), value, fill=color, font=font)


def box(bounds, fill="#ffffff", outline="#c7d4e5", width=3):
    d.rounded_rectangle(bounds, radius=20, fill=fill, outline=outline, width=width)


def arrow(points, color=BLUE, width=5):
    d.line(points, fill=color, width=width, joint="curve")
    x, y = points[-1]
    px, py = points[-2]
    if x > px:
        tri = [(x, y), (x - 17, y - 10), (x - 17, y + 10)]
    elif x < px:
        tri = [(x, y), (x + 17, y - 10), (x + 17, y + 10)]
    elif y > py:
        tri = [(x, y), (x - 10, y - 17), (x + 10, y - 17)]
    else:
        tri = [(x, y), (x - 10, y + 17), (x + 10, y + 17)]
    d.polygon(tri, fill=color)


text(60, 35, "AWS 웹 서버 배포 실습", 48, bold=True)
text(60, 105, "서울 ap-northeast-2  |  검증 당시 구성  |  외부 접속 방식 A", 27, "#526582")

box((700, 170, 1740, 835), "#f8fbff", BLUE)
text(740, 195, "VPC  cloud-mission-vpc  |  10.0.0.0/16", 31, bold=True)

box((750, 270, 1690, 785), "#edf5ff", "#73a4ef")
text(785, 292, "Public Subnet  |  10.0.1.0/24", 30, bold=True)
text(785, 343, "ap-northeast-2c  /  subnet-01a53b4bdf2266a98", 24, "#526582")

box((800, 390, 1640, 690), "white", "#5b8fd9")
text(835, 412, "Security Group  cloud-mission-sg", 28, bold=True)
text(835, 540, "HTTP 80", 27, BLUE, True)
text(835, 580, "0.0.0.0/0 허용", 23)
text(835, 622, "SSH 22: 내 IP /32", 23, PURPLE)

box((1120, 455, 1580, 635), "#e7f8f0", "#38926d")
text(1150, 475, "EC2  /  t3.micro", 31, bold=True)
text(1150, 522, "Ubuntu + Nginx", 27)
text(1150, 565, "Public IPv4: 3.34.44.74", 24)
text(1150, 602, "Private IPv4: 10.0.1.181", 20, "#526582")

box((60, 420, 310, 550), "#f4f7fb")
text(95, 443, "외부 브라우저", 29, bold=True)
text(95, 492, "Internet", 25, "#526582")
box((400, 420, 650, 550), "#fff4de", "#dfac46")
text(425, 442, "Internet Gateway", 25, bold=True)
text(425, 495, "cloud-mission-igw", 21)

arrow([(310, 485), (400, 485)])
arrow([(650, 485), (1120, 485)])
text(70, 376, "HTTP 80 → Nginx", 25, BLUE)

box((60, 215, 310, 345), "#f6f0fd", "#b99add")
text(95, 240, "관리자 PC", 29, bold=True)
text(95, 287, "본인 공인 IP", 24, "#526582")
arrow([(310, 280), (525, 280), (525, 420)], PURPLE, 4)
arrow([(525, 550), (525, 605), (730, 605), (730, 625), (800, 625)], PURPLE, 4)
text(350, 238, "SSH 22 / 개인키 인증", 24, PURPLE)

box((60, 650, 650, 835), "#f5f7fa")
text(90, 675, "Route Table: cloud-mission-public-rt", 26, bold=True)
text(90, 726, "10.0.0.0/16 → local", 26)
text(90, 773, "0.0.0.0/0 → cloud-mission-igw", 26, BLUE)
arrow([(650, 735), (750, 735)], "#8799b1", 3)
text(667, 763, "연결", 21, "#526582")

text(60, 887, "검증: Nginx active · localhost 200 · 인터넷 아웃바운드 200 · 외부 페이지 표시", 28, bold=True)
text(60, 938, "퍼블릭 IPv4는 검증 당시 주소이며, EC2 종료 후에는 이 실습 서비스를 제공하지 않습니다.", 23, "#526582")

target = ROOT / "docs" / "architecture.png"
img.save(target)
print(target)
