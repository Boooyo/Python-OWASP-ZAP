import logging
from zap_utils import initialize_zap, access_target, spider_target, scan_target, generate_report, diagnose_vulnerabilities

# 로거 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    # 사용자 입력 받기
    target_url = input("Enter the target URL: ")
    proxy_address = input("Enter the proxy address (default: 127.0.0.1): ") or '127.0.0.1'
    proxy_port = input("Enter the proxy port (default: 8080): ") or 8080

    # ZAP 프록시 초기화
    zap = initialize_zap(proxy_address, proxy_port)

    # 대상 사이트 스캔
    access_target(zap, target_url)
    spider_target(zap, target_url)
    scan_target(zap, target_url)

    # 취약점 보고서 생성
    generate_report(zap)

    # 취약점 진단 및 리팩토링
    diagnose_vulnerabilities(zap, target_url)

if __name__ == "__main__":
    main()


# 2024.05.20.03:10 : 웹 취약점 로그 분석 후, 리펙토링을 자동으로 해주는 모델 생성. (해킹 자동 방지 모델을 만들어보고자함.)