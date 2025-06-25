import datetime
import os

def should_log():
    try:
        with open('.env', 'r') as f:
            for line in f:
                if line.strip() in ('env=env', 'env=env%'):
                    return True
    except Exception:
        pass
    return False

def log_message(message):
    """
    Appends a log message with a timestamp to testicl.log if .env allows logging.
    Only writes to file, not to console.
    """
    if not should_log():
        return
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('testicl.log', 'a') as f:
        f.write(f"[{timestamp}] {message}\n") 