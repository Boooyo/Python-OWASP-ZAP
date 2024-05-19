import time
import logging
from zapv2 import ZAPv2

# 로거 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def initialize_zap(proxy_address='127.0.0.1', proxy_port=8080):
    """
    ZAP 프록시 초기화
    """
    logger.info("Initializing ZAP proxy")
    return ZAPv2(proxies={'http': f'http://{proxy_address}:{proxy_port}', 'https': f'http://{proxy_address}:{proxy_port}'})

def access_target(zap, target_url):
    """
    대상 사이트로 접근
    """
    logger.info(f"Accessing target URL: {target_url}")
    zap.urlopen(target_url)
    time.sleep(2)  # 잠시 대기

def spider_target(zap, target_url):
    """
    대상 사이트 스파이더링
    """
    logger.info(f"Spidering target URL: {target_url}")
    scan_id = zap.spider.scan(target_url)
    while int(zap.spider.status(scan_id)) < 100:
        logger.info(f"Spider progress: {zap.spider.status(scan_id)}%")
        time.sleep(2)
    logger.info("Spider completed")

def scan_target(zap, target_url):
    """
    대상 사이트 활성 스캔
    """
    logger.info(f"Scanning target URL: {target_url}")
    scan_id = zap.ascan.scan(target_url)
    while int(zap.ascan.status(scan_id)) < 100:
        logger.info(f"Scan progress: {zap.ascan.status(scan_id)}%")
        time.sleep(5)
    logger.info("Active scan completed")

def generate_report(zap):
    """
    취약점 보고서 출력
    """
    logger.info("Generating report")
    alerts = zap.core.alerts()
    for alert in alerts:
        logger.info(f"Alert: {alert['alert']}")
        logger.info(f"Risk: {alert['risk']}")
        logger.info(f"URL: {alert['url']}")
        logger.info(f"Description: {alert['description']}")
        logger.info(f"Solution: {alert['solution']}")
        logger.info("")

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

if __name__ == "__main__":
    main()
