

# System
import logging

# Project
from core.constants import SERVICE


logger = logging.getLogger("monitor")


class ServerMonitor:
    # 서버 모니터
    @classmethod
    def report_server_error(cls, request, error):
        try:
            if SERVICE.DEBUG:
                slack_channel = "#monitor_debug"
            else:
                slack_channel = "#monitor_server"

            error_detail = f"PATH: {request.path}\nGET: {request.GET}\nPOST: {
                request.POST}\nFILE: {request.FILES}\n{error}"

            logger.error(f"[UNKNOWN_SERVER_ERROR]: {
                         error_detail}")
            # response = slackBot.send_message(slack_channel, "서버 에러가 발생했습니다.")
            # slack_thread_ts = response["ts"]
            # slackBot.send_message(slack_channel, error_detail, thread_ts=slack_thread_ts)
        except Exception as e:
            pass
