# PxollyAPI
Библиотека для взаимодействия с API чат менеджера Pxolly (https://pxolly.ru)

## Использование
Пример получения информации об аккаунте
```python
import asyncio

from pxolly_api import PxollyAPI
from pxolly_api.exceptions import PxollyException


async def main() -> None:
    try:
        api = PxollyAPI(token="access_token")
        result = await api.account.get_info()
        print(result)
    except PxollyException as exc:
        print("Ошибка", exc)
    finally:
        await api.close()

if __name__ == "__main__":
    asyncio.run(main())

```
Также можно использовать клиент через контекстный менеджер

```python
import asyncio

from pxolly_api import PxollyAPI
from pxolly_api.exceptions import PxollyException


async def main() -> None:
    async with PxollyAPI(token="access_token") as api:
        try:
            result = await api.account.get_info()
            print(result)
        except PxollyException as exc:
            print("Ошибка", exc)

if __name__ == "__main__":
    asyncio.run(main())
```

Также вместо готовых методов можно использовать сырые
```python
# Вместо
result = await api.account.get_info()

# Используем 
result = await api.method("account.getInfo")
```

## Доступные категории методов
* Account
* Callback
* Chats
* Database
* Users
* Utils

## Зависимости и инструменты
* Пакетный менеджер: uv
* Линтер: ruff
* HTTP клиент: niquests
* Валидация: pydantic
* Тестирование: pytest, pytest-asyncio

## Благодарность
[Полина Шатохина](https://vk.com/lilchacha)   
Помогла с ошибками и недочётами в методах, а также дала полную документацию ко всем методам.

[Пхолли](https://vk.com/pxolly)
Эпл в мире вк ботов ❤
