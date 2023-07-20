# Настраиваем сервер

## SSH ключи

Копируем публчиный ключ на сервер:
```
ssh-copy-id server
```

~Добавляем ключ в authorizedkeys, чтобы не вводить пароль:~
```
sudo cat id_rsa.pub > authorized_keys~
```

```
ssh-copy-id adress
```


## Создать юзера

Создаём юзера, хомяка для него и устанавливаем пароль
```
sudo useradd -s /bin/bash user
mkdir /home/user
```
```
sudo passwd user
```
Добавляем юзера в судо
```
sudo usermod -aG sudo user
```

```
sudo chown -R
```


## Python

### Poetry

Установка
```
curl -sSL https://install.python-poetry.org | python3 -
```
