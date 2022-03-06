#DDoS-master

Українська мова
├─▪Вимоги
│ └─▪python 3
│   └─▪pythonping
├─▪Функціонал
│ ├─▪Сканування відкритих портів
│ ├─▪Методи
│ │ ├─▪HTTP(s)
│ │ ├─▪TCP
│ │ └─▪UDP
│ └─▪Особливості
│   ├─▪Оптимізація
│   └─▪HTTP(s) метод через проксі сервер
├─▪Використання
│ └─▪Скрипти
│   ├─▪Windows: py <Ім'я скрипта.py> --help
│   ├─▪Other: python3 <Ім'я скрипта.py> --help  
│   ├─▪http_s.py
│   │ ├─▪-t <Ціль (домейн чи IP адреса)> (обов'язково)
│   │ ├─▪-i <IP адреса проксі сервера> (обов'язково)
│   │ ├─▪-p <Порт проксі сервера> (обов'язково)
│   │ ├─▪-f <Адреса сторінки сайту> (не обов'язково)
│   │ │ ├─▪Якщо не вказувати - кожен запит буде на випадкову сторінку (для більшої ефективності)
│   │ │ └─▪Приклад
│   │ │   ├─▪www.site.com/page
│   │ │   └─▪-f /page (вказувати існуючу та найбільшу сторінку щоб було ефективніше)
│   │ ├─▪-w <Кількість імітованних ботів> (не обов'язково)
│   │ │ ├─▪Якщо не вказувати - автоматично ставиться на 100
│   │ │ └─▪Приклад
│   │ │   └─▪-w 500 (чим більше - тим більша нагрузка на комп'ютер та інтернет)
│   │ ├─▪-s <Швидкість підключення імітованнх ботів до проксі серверу та сайту у мілісекундах> (не обов'язково)
│   │ │ ├─▪Якщо не вказувати - автоматично ставиться на 50
│   │ │ └─▪Приклад
│   │ │   └─▪-s 100 (чим більше - тим більша затримка підключення імітованнх ботів)
│   │ └─▪Приклад використання
│   │   ├─▪Windows
│   │   │ └─▪py http_s.py -t www.site.com -i 123.123.123.123 -p 8080 -f /page -w 250 -s 100
│   │   └─▪Other
│   │     └─▪python3 http_s.py -t www.site.com -i 123.123.123.123 -p 8080 -f /page -w 250 -s 100
│   ├─▪tcp.py
│   │ ├─▪-i <Ціль (домейн чи IP адреса)> (обов'язково)
│   │ ├─▪-p <Порт> (обов'язково)
│   │ ├─▪-w <Кількість імітованних ботів> (не обов'язково)
│   │ │ ├─▪Якщо не вказувати - автоматично ставиться на 100
│   │ │ └─▪Приклад
│   │ │   └─▪-w 500 (чим більше - тим більша нагрузка на комп'ютер та інтернет)
│   │ └─▪Приклад використання
│   │   ├─▪Windows
│   │   │ └─▪py tcp.py -i 123.123.123.123 -p 80 -w 250
│   │   └─▪Other
│   │     └─▪python3 tcp.py -i 123.123.123.123 -p 80 -w 250
│   ├─▪udp.py
│   │ ├─▪-i <Ціль (домейн чи IP адреса)> (обов'язково)
│   │ ├─▪-p <Порт> (не обов'язково)
│   │ │ └─▪Якщо не вказувати - порти будуть перебиратися автоматично (для більшої ефективності)
│   │ ├─▪-w <Кількість імітованних ботів> (не обов'язково)
│   │ │ ├─▪Якщо не вказувати - автоматично ставиться на 100
│   │ │ └─▪Приклад
│   │ │   └─▪-w 500 (чим більше - тим більша нагрузка на комп'ютер та інтернет)
│   │ └─▪Приклад використання
│   │   ├─▪Windows
│   │   │ └─▪py udp.py -i 123.123.123.123 -p 80 -w 250
│   │   └─▪Other
│   │     └─▪python3 udp.py -i 123.123.123.123 -p 80 -w 250
│   └─▪port scanner.py
│     └─▪Приклад використання
│       ├─▪Windows
│       │ └─▪py "port scanner.py"
│       └─▪Other
│         └─▪python3 port\ scanner.py
└─▪Я (RiX), як автор даних скриптів не несу відповідальності за їх використання у тих, чи інших цілях.
