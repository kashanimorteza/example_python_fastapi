# models/alarm.py

from pydantic import BaseModel

class alarmDetaile(BaseModel):
    enable : bool = False
    count : int = 0
    limit : int = 0

class alarmModel(BaseModel):
    pay : alarmDetaile = None
    validity : alarmDetaile = None
    bandwith : alarmDetaile = None
    create : alarmDetaile = None
    renew : alarmDetaile = None
    validity_near : alarmDetaile = None
    bandwith_near : alarmDetaile = None

# models/config.py

from pydantic import BaseModel

class configModel(BaseModel):
    name : str = None
    panel : str = None
    email : str = None
    web : str = None
    timeZone : str = None
    warp_port : int = 0
    webapi_port : int = 0
    debug : bool = False
    log : bool = False
    verbos : bool = False
    log_lines : int = 0
    cron_daily_time : str = None
    cron_hourly_period : int = 0
    cron_minly_period : int = 0
    cron_delay : int = 0
    config_number : int = 0
    free_group_id : int = 0
    current_user_id : int = 0
    base_group_id : int = 0
    end_group_id : int = 0
    current_group_id : int = 0
    bank_account_name : str = None
    bank_account_card : str = None
    traffic_today : int = 0
    traffic_yesterday : int = 0
    traffic_month : int = 0
    log_folder : str = None
    backup_folder : str = None
    certificate_dir : str = None

# models/display.py

from pydantic import BaseModel

class displayModel(BaseModel):
    config : bool = False
    pay : bool = False
    validity : bool = False
    bandwith : bool = False

# models/domain.py

from pydantic import BaseModel

class domainModel(BaseModel):
    id : int = 0
    enable : bool = False
    name : str = None
    type : str = None 
    provider : str = None
    address : str = None 
    sub : str = None
    zoneid : str = None 
    accountid : str = None 
    token : str = None

# models/group.py

from pydantic import BaseModel
from models.alarm import alarmModel
from models.display import displayModel

class inboundModel(BaseModel):
    id : int = 0
    enable : bool = False
    display : bool = False

class routeModel(BaseModel):
    id : int = 0
    enable : bool = False

class wayModel(BaseModel):
    id : int = 0
    enable : bool = False
    route : list[routeModel] = []

class networkModel(BaseModel):
    id : int = 0
    enable : bool = False
    way : list[wayModel] = []

class serviceV2rayModel(BaseModel):
    enable : bool = False
    inbound : list[inboundModel] = []
    network : list[networkModel] = []

class groupModel(BaseModel):
    id : int = 0
    name : str = None
    type : str = None
    pre : str = None
    enable : bool = False
    serviceV2ray : serviceV2rayModel = None
    alarm : alarmModel = None
    display : displayModel = None

# models/network.py

from pydantic import BaseModel

class networkModel(BaseModel):
    id : int = 0
    enable : bool = False
    name : str = None
    pre : str = None

# models/os.py

from pydantic import BaseModel

class osModel(BaseModel):
    iphone : bool = False
    android : bool = False
    windows : bool = False
    linux : bool = False

# models/plan.py

from pydantic import BaseModel

class planModel(BaseModel):
    id : int = 1
    enable : bool = False
    name : str = None
    period_limit : int = 0
    validity_limit : int = 0
    bandwith_limit : int = 0
    price : int = 0
    period_fix : bool = True
    access_renew : bool = False

# models/domain.py

from pydantic import BaseModel

class serverModel(BaseModel):
    name : str = None
    enable : bool = False

class routeModel(BaseModel):
    id : int = 0
    enable : bool = False
    name : str = None
    type : str = None 
    display : str = None
    select : str = None 
    domain_id : int = 7
    server : list[serverModel] = None

# models/service.py

from pydantic import BaseModel

class serviceV2rayModel(BaseModel):
    id : int = 1
    name : str = "v2ray"
    pre : str = "v"
    plan_id : int = 0
    price : int = 0 
    period_limit : int = 0
    period_used : int = 0
    validity_limit : int = 0
    validity_used : int = 0
    bandwith_limit : int = 0
    bandwith_used : int = 0
    first : str = None
    start : str = None
    last_connection : str = None
    uuid : str = None
    enable : bool = True
    afterStart : bool = False
    period_fix : bool = True
    online : bool = False
    access_renew : bool = False
    reserve_renew : bool = False
    pay : bool = False

# models/telegram.py

from pydantic import BaseModel

class telegramModel(BaseModel):
    id : int = 0
    enable : bool = False
    name : str = None
    support_username : str = None 
    support_channel : str = None
    robot_username : str = None 
    bot_api_id : str = None
    bot_api_hash : str = None 
    bot_token : str = None 
    bot_delay : int = 0
    send_user_telegram : bool = False
    link : str = None

# models/user.py

from pydantic import BaseModel
from models.alarm import alarmModel
from models.display import displayModel
from models.os import osModel

class accountModel(BaseModel):
    register_date : str = None
    id : int = 0
    group : int = 0
    father : int = 0
    username : str = None
    name : str = None
    email : str = None
    phone : str = None
    enable : bool = False
    delete : bool = False
    display : bool = False
    bank_card : list[str] = []

class authenticationModel(BaseModel):
    username : str = None
    password : str = None
    key : str = None

class telegramModel(BaseModel):
    id : str = None
    joinRobot : bool = False
    joinChannel : bool = False
    sumOfMessage : int = 0
    
class userModel(BaseModel):
    account : accountModel = None
    authentication : authenticationModel = None
    telegram : telegramModel = None
    alarm : alarmModel = None
    display : displayModel = None
    os : osModel = None
    service : list = []

# models/way.py

from pydantic import BaseModel

class wayModel(BaseModel):
    id : int = 0
    enable : bool = False
    name : str = None
    pre : str = None