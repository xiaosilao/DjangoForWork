SELECT DATE_SUB(CURDATE(),INTERVAL 1 day) qdate
from 01u_0qudao_url
GROUP BY DATE_SUB(CURDATE(),INTERVAL 1 day)