# Настраиваем сервер

## SSH ключи

Копируем публчиный ключ на сервер:
```
ssh-copy-id server
```

Добавляем ключ в authorizedkeys, чтобы не вводить пароль:
```
sudo cat id_rsa.pub > authorized_keys
```

## Добавить юзера в судо

```
sudo usermod -aG sudo user
```


## Python

### Poetry

Установка
```
curl -sSL https://install.python-poetry.org | python3 -
```
