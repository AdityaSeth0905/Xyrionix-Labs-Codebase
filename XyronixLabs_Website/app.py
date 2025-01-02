from utils.logger import logger

# Example usage
logger.log('User logged in', 'auth')
logger.log('User requested resource', 'request')

# Retrieve logs by category
auth_logs = logger.get_logs_by_category('auth')
print('Auth Logs:', [log.dict() for log in auth_logs])
