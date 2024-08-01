

# System
import os
from time import sleep
import traceback
import argparse
import subprocess
from pathlib import Path


# ANSI escape codes for colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"

BASE_DIR = Path(__file__).resolve().parent.parent
DOCKER_COMPSE_FILE = "docker-compose.yml"
NEW_SERVICE = "web-green"
NEW_PORT = 8002
OLD_SERVICE = "web-blue"
OLD_PORT = 8001


def parse_args():
    # construct the argument parse and parse the arguments
    argparser = argparse.ArgumentParser()

    argparser.add_argument(
        "-s",
        "--service",
        type=str,
        required=True,
        help="Deploy Service (dev, prod)",
    )

    (args, unknown) = argparser.parse_known_args()

    args = vars(args)

    if len(unknown) > 0:
        argparser.print_help()
        exit(11)

    if args["service"] not in ["dev", "prod"]:
        argparser.print_help()
        exit(12)

    return args


def check_service() -> None:
    """
    현재 실행 중인 서비스가 그린인지 블루인지 확인
    """
    docker_compose_file_path = os.path.join(BASE_DIR, DOCKER_COMPSE_FILE)

    output = subprocess.run(
        f"docker compose -f {docker_compose_file_path} ps | grep web-green | grep Up", shell=True, capture_output=True)

    # 현재 실행 중인 서비스가 green일때
    if output.returncode == 0:
        global NEW_SERVICE
        global NEW_PORT
        global OLD_SERVICE
        global OLD_PORT
        NEW_SERVICE = "web-blue"
        NEW_PORT = 8001
        OLD_SERVICE = "web-green"
        OLD_PORT = 8002

    print(f"{YELLOW}[*] 현재 서비스: [{BLUE}{OLD_SERVICE}{
          YELLOW}], 신규 서비스: [{GREEN}{NEW_SERVICE}{YELLOW}]{RESET}")


def deploy() -> None:
    """
    배포 코드
    """
    print(f"{CYAN}[*] 배포를 진행합니다.{RESET}")

    # 신규 서비스 빌드 및 인스턴스로 배포
    subprocess.run(f"docker compose up -d --build {NEW_SERVICE}", shell=True)

    # 도커 컨테이너가 실행될 때까지 일정시간 기다림
    sleep(15)

    # health Check
    output = subprocess.run(
        f'curl -s -o /dev/null -w "%{{http_code}}" http://127.0.0.1:{NEW_PORT}/health-check', shell=True, capture_output=True)
    new_service_status = output.stdout.decode()

    if new_service_status == "200":
        # 이전 서비스를 중지하고 삭제
        subprocess.run(
            f'docker rm -f {OLD_SERVICE}', shell=True)
        
        print(
            f"{YELLOW}[*] {GREEN}[{NEW_SERVICE}]{YELLOW} 배포 완료 되었습니다.{RESET}")
    else:
        # 배포 실패
        subprocess.run(
            f'docker rm -f {NEW_SERVICE}', shell=True)
        print(
            f"{YELLOW}[*] {GREEN}[{NEW_SERVICE}]{YELLOW} 배포 실패 하였습니다. 배포를 중단합니다.{RESET}")
        exit(1)


def delete_image() -> None:
    print(f"{CYAN}[*] 미사용 도커 이미지를 제거합니다.{RESET}")
    subprocess.run(f"docker container prune -f", shell=True)
    subprocess.run(f"docker image prune -f", shell=True)


def main(service: str) -> None:
    try:
        check_service()
        deploy()
        delete_image()
    except Exception as e:
        # TODO: 오류가 난 상황 정리
        print(traceback.format_exc())


if __name__ == "__main__":
    """
    python deploy/deploy.py --service=dev
    """
    os.chdir(BASE_DIR)
    args = parse_args()
    main(args["service"])
