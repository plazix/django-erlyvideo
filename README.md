*На данный момент это наброски, хотя должны быть работоспособными*

README
======

Загрузите код из git репозитория:
    
    git clone git://github.com/plazix/django-erlyvideo.git django-erlyvideo
    
И добавте папку django-erlyvideo/erlyvideo в ваш PYTHONPATH.

Добавте erlyvideo в INSTALLED_APPS вашего проекта.

Настройки
======

ERLYVIDEO\_PUBLISH\_AUTH\_FUNC - строка с путем к функции проверяющей права пользователя на публикацию потока, по умолчанию - разрешено. 

    def public\_auth\_sample(ip, file, user\_id, session\_id):
        """
        Пример функции проверки разрешено ли пользователю публиковать поток
        
        :param ip: IP адресс пользователя публикующего поток
        :param file: имя потока
        :param user_id: ID пользователя переданного в данных сессии
        :param session_id: ID сессии
        :return: True - разрешено, False - запрещено
        """
        return True
        
ERLYVIDEO\_PLAY\_AUTH\_FUNC - строка с путем к функции проверяющей права пользователя на просмотр потока, по умолчанию - разрешено. 

    def play\_auth\_sample(ip, file, user\_id, session\_id):
        """
        Пример функции проверки разрешено ли пользователю просматривать поток

        :param ip: IP адресс пользователя просматривающего поток
        :param file: имя потока
        :param user_id: ID пользователя переданного в данных сессии
        :param session_id: ID сессии
        :return: True - разрешено, False - запрещено
        """
        return True
    
ERLYVIDEO\_ACCESS\_IPS - список IP с которых разрешен прием запросов на аутентификацию и событий от сервера erlyvideo.

ERLYVIDEO_SECRET_KEY - строка секретный ключ для подписи данных сессии, должна совпадать со строкой secret\_key в секции виртуального хоста в конфиге erlyvideo. По умолчанию равна settings.SECRET\_KEY.

Сигналы
======

server_event - вызывается при приходи события от сервера erlyvideo.

publish_auth - вызывается при успешной аутентификации на публикацию потока.

play_auth - вызывается при успешной аутентификации на просмотр потока.
    
