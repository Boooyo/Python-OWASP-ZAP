import time
from zapv2 import ZAPv2

# ZAP 프록시의 주소와 포트 설정
zap = ZAPv2(proxies={'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'})

target_url = 'http://example.com'

# 대상 사이트로 접근
print(f"Accessing target URL {target_url}")
zap.urlopen(target_url)
time.sleep(2)  # 잠시 대기

# 대상 사이트를 스파이더링(크롤링)
print(f"Spidering target URL {target_url}")
scan_id = zap.spider.scan(target_url)
while int(zap.spider.status(scan_id)) < 100:
    print(f"Spider progress: {zap.spider.status(scan_id)}%")
    time.sleep(2)
print("Spider completed")

# 대상 사이트를 활성 스캔
print(f"Scanning target URL {target_url}")
scan_id = zap.ascan.scan(target_url)
while int(zap.ascan.status(scan_id)) < 100:
    print(f"Scan progress: {zap.ascan.status(scan_id)}%")
    time.sleep(5)
print("Active scan completed")

# 취약점 보고서 출력
print("Generating report")
alerts = zap.core.alerts()
for alert in alerts:
    print(f"Alert: {alert['alert']}")
    print(f"Risk: {alert['risk']}")
    print(f"URL: {alert['url']}")
    print(f"Description: {alert['description']}")
    print(f"Solution: {alert['solution']}")
    print()

print("Scan completed")
