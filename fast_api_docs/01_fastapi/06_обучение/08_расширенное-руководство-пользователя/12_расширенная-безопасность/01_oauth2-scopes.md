---
title: OAuth2 scopes
source: https://fastapi.tiangolo.com/ru/advanced/security/oauth2-scopes/
---

# OAuth2 scopes

🌐 Перевод выполнен с помощью ИИ и людей

Этот перевод был сделан ИИ под руководством людей. 🤝

В нем могут быть ошибки из-за неправильного понимания оригинального смысла или неестественности и т. д. 🤖

Вы можете улучшить этот перевод, [помогая нам лучше направлять ИИ LLM](https://fastapi.tiangolo.com/ru/contributing/#translations) ([local](./../../../11_ресурсы/02_development-contributing.md#translations)).

[Английская версия](https://fastapi.tiangolo.com/advanced/security/oauth2-scopes/)

Вы можете использовать OAuth2 scopes напрямую с **FastAPI** — они интегрированы и работают бесшовно.

Это позволит вам иметь более детальную систему разрешений по стандарту OAuth2, интегрированную в ваше OpenAPI‑приложение (и документацию API).

OAuth2 со scopes — это механизм, который используют многие крупные провайдеры аутентификации: Facebook, Google, GitHub, Microsoft, X (Twitter) и т.д. Они применяют его, чтобы предоставлять конкретные разрешения пользователям и приложениям.

Каждый раз, когда вы «входите через» Facebook, Google, GitHub, Microsoft, X (Twitter), это приложение использует OAuth2 со scopes.

В этом разделе вы увидите, как управлять аутентификацией и авторизацией с теми же OAuth2 scopes в вашем приложении на **FastAPI**.

Предупреждение

Это более-менее продвинутый раздел. Если вы только начинаете, можете пропустить его.

Вам не обязательно нужны OAuth2 scopes — аутентификацию и авторизацию можно реализовать любым нужным вам способом.

Но OAuth2 со scopes можно красиво интегрировать в ваш API (через OpenAPI) и документацию API.

Так или иначе, вы все равно будете применять эти scopes или какие-то другие требования безопасности/авторизации, как вам нужно, в вашем коде.

Во многих случаях OAuth2 со scopes может быть избыточным.

Но если вы знаете, что это нужно, или вам просто интересно — продолжайте чтение.

## OAuth2 scopes и OpenAPI

Спецификация OAuth2 определяет «scopes» как список строк, разделённых пробелами.

Содержимое каждой такой строки может иметь любой формат, но не должно содержать пробелов.

Эти scopes представляют «разрешения».

В OpenAPI (например, в документации API) можно определить «схемы безопасности» (security schemes).

Когда одна из таких схем безопасности использует OAuth2, вы также можете объявлять и использовать scopes.

Каждый «scope» — это просто строка (без пробелов).

Обычно они используются для объявления конкретных разрешений безопасности, например:

  * `users:read` или `users:write` — распространённые примеры.
  * `instagram_basic` используется Facebook / Instagram.
  * `https://www.googleapis.com/auth/drive` используется Google.

Информация

В OAuth2 «scope» — это просто строка, объявляющая требуемое конкретное разрешение.

Неважно, есть ли там другие символы, такие как `:`, или это URL.

Эти детали зависят от реализации.

Для OAuth2 это просто строки.

## Взгляд издалека

Сначала быстро посмотрим, что изменилось по сравнению с примерами из основного раздела **Учебник - Руководство пользователя** — [OAuth2 с паролем (и хешированием), Bearer с JWT-токенами](https://fastapi.tiangolo.com/ru/tutorial/security/oauth2-jwt/) ([local](./../../06_учебник-руководство-пользователя/31_безопасность/04_oauth2-с-паролем-и-хешированием-bearer-с-jwt-токенами.md)). Теперь — с использованием OAuth2 scopes:

Python 3.10+

```
 
    from datetime import datetime, timedelta, timezone
    from typing import Annotated
    
    import jwt
    from fastapi import Depends, FastAPI, HTTPException, Security, status
    from fastapi.security import (
        OAuth2PasswordBearer,
        OAuth2PasswordRequestForm,
        SecurityScopes,
    )
    from jwt.exceptions import InvalidTokenError
    from pwdlib import PasswordHash
    from pydantic import BaseModel, ValidationError
    
    # to get a string like this run:
    # openssl rand -hex 32
    SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    
    
    fake_users_db = {
        "johndoe": {
            "username": "johndoe",
            "full_name": "John Doe",
            "email": "johndoe@example.com",
            "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$wagCPXjifgvUFBzq4hqe3w$CYaIb8sB+wtD+Vu/P4uod1+Qof8h+1g7bbDlBID48Rc",
            "disabled": False,
        },
        "alice": {
            "username": "alice",
            "full_name": "Alice Chains",
            "email": "alicechains@example.com",
            "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$g2/AV1zwopqUntPKJavBFw$BwpRGDCyUHLvHICnwijyX8ROGoiUPwNKZ7915MeYfCE",
            "disabled": True,
        },
    }
    
    
    class Token(BaseModel):
        access_token: str
        token_type: str
    
    
    class TokenData(BaseModel):
        username: str | None = None
        scopes: list[str] = []
    
    
    class User(BaseModel):
        username: str
        email: str | None = None
        full_name: str | None = None
        disabled: bool | None = None
    
    
    class UserInDB(User):
        hashed_password: str
    
    
    password_hash = PasswordHash.recommended()
    
    DUMMY_HASH = password_hash.hash("dummypassword")
    
    oauth2_scheme = OAuth2PasswordBearer(
        tokenUrl="token",
        scopes={"me": "Read information about the current user.", "items": "Read items."},
    )
    
    app = FastAPI()
    
    
    def verify_password(plain_password, hashed_password):
        return password_hash.verify(plain_password, hashed_password)
    
    
    def get_password_hash(password):
        return password_hash.hash(password)
    
    
    def get_user(db, username: str):
        if username in db:
            user_dict = db[username]
            return UserInDB(**user_dict)
    
    
    def authenticate_user(fake_db, username: str, password: str):
        user = get_user(fake_db, username)
        if not user:
            verify_password(password, DUMMY_HASH)
            return False
        if not verify_password(password, user.hashed_password):
            return False
        return user
    
    
    def create_access_token(data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    
    
    async def get_current_user(
        security_scopes: SecurityScopes, token: Annotated[str, Depends(oauth2_scheme)]
    ):
        if security_scopes.scopes:
            authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
        else:
            authenticate_value = "Bearer"
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": authenticate_value},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username = payload.get("sub")
            if username is None:
                raise credentials_exception
            scope: str = payload.get("scope", "")
            token_scopes = scope.split(" ")
            token_data = TokenData(scopes=token_scopes, username=username)
        except (InvalidTokenError, ValidationError):
            raise credentials_exception
        user = get_user(fake_users_db, username=token_data.username)
        if user is None:
            raise credentials_exception
        for scope in security_scopes.scopes:
            if scope not in token_data.scopes:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Not enough permissions",
                    headers={"WWW-Authenticate": authenticate_value},
                )
        return user
    
    
    async def get_current_active_user(
        current_user: Annotated[User, Security(get_current_user, scopes=["me"])],
    ):
        if current_user.disabled:
            raise HTTPException(status_code=400, detail="Inactive user")
        return current_user
    
    
    @app.post("/token")
    async def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    ) -> Token:
        user = authenticate_user(fake_users_db, form_data.username, form_data.password)
        if not user:
            raise HTTPException(status_code=400, detail="Incorrect username or password")
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username, "scope": " ".join(form_data.scopes)},
            expires_delta=access_token_expires,
        )
        return Token(access_token=access_token, token_type="bearer")
    
    
    @app.get("/users/me/")
    async def read_users_me(
        current_user: Annotated[User, Depends(get_current_active_user)],
    ) -> User:
        return current_user
    
    
    @app.get("/users/me/items/")
    async def read_own_items(
        current_user: Annotated[User, Security(get_current_active_user, scopes=["items"])],
    ):
        return [{"item_id": "Foo", "owner": current_user.username}]
    
    
    @app.get("/status/")
    async def read_system_status(current_user: Annotated[User, Depends(get_current_user)]):
        return {"status": "ok"}
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from datetime import datetime, timedelta, timezone
    
    import jwt
    from fastapi import Depends, FastAPI, HTTPException, Security, status
    from fastapi.security import (
        OAuth2PasswordBearer,
        OAuth2PasswordRequestForm,
        SecurityScopes,
    )
    from jwt.exceptions import InvalidTokenError
    from pwdlib import PasswordHash
    from pydantic import BaseModel, ValidationError
    
    # to get a string like this run:
    # openssl rand -hex 32
    SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    
    
    fake_users_db = {
        "johndoe": {
            "username": "johndoe",
            "full_name": "John Doe",
            "email": "johndoe@example.com",
            "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$wagCPXjifgvUFBzq4hqe3w$CYaIb8sB+wtD+Vu/P4uod1+Qof8h+1g7bbDlBID48Rc",
            "disabled": False,
        },
        "alice": {
            "username": "alice",
            "full_name": "Alice Chains",
            "email": "alicechains@example.com",
            "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$g2/AV1zwopqUntPKJavBFw$BwpRGDCyUHLvHICnwijyX8ROGoiUPwNKZ7915MeYfCE",
            "disabled": True,
        },
    }
    
    
    class Token(BaseModel):
        access_token: str
        token_type: str
    
    
    class TokenData(BaseModel):
        username: str | None = None
        scopes: list[str] = []
    
    
    class User(BaseModel):
        username: str
        email: str | None = None
        full_name: str | None = None
        disabled: bool | None = None
    
    
    class UserInDB(User):
        hashed_password: str
    
    
    password_hash = PasswordHash.recommended()
    
    DUMMY_HASH = password_hash.hash("dummypassword")
    
    oauth2_scheme = OAuth2PasswordBearer(
        tokenUrl="token",
        scopes={"me": "Read information about the current user.", "items": "Read items."},
    )
    
    app = FastAPI()
    
    
    def verify_password(plain_password, hashed_password):
        return password_hash.verify(plain_password, hashed_password)
    
    
    def get_password_hash(password):
        return password_hash.hash(password)
    
    
    def get_user(db, username: str):
        if username in db:
            user_dict = db[username]
            return UserInDB(**user_dict)
    
    
    def authenticate_user(fake_db, username: str, password: str):
        user = get_user(fake_db, username)
        if not user:
            verify_password(password, DUMMY_HASH)
            return False
        if not verify_password(password, user.hashed_password):
            return False
        return user
    
    
    def create_access_token(data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    
    
    async def get_current_user(
        security_scopes: SecurityScopes, token: str = Depends(oauth2_scheme)
    ):
        if security_scopes.scopes:
            authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
        else:
            authenticate_value = "Bearer"
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": authenticate_value},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
            scope: str = payload.get("scope", "")
            token_scopes = scope.split(" ")
            token_data = TokenData(scopes=token_scopes, username=username)
        except (InvalidTokenError, ValidationError):
            raise credentials_exception
        user = get_user(fake_users_db, username=token_data.username)
        if user is None:
            raise credentials_exception
        for scope in security_scopes.scopes:
            if scope not in token_data.scopes:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Not enough permissions",
                    headers={"WWW-Authenticate": authenticate_value},
                )
        return user
    
    
    async def get_current_active_user(
        current_user: User = Security(get_current_user, scopes=["me"]),
    ):
        if current_user.disabled:
            raise HTTPException(status_code=400, detail="Inactive user")
        return current_user
    
    
    @app.post("/token")
    async def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
    ) -> Token:
        user = authenticate_user(fake_users_db, form_data.username, form_data.password)
        if not user:
            raise HTTPException(status_code=400, detail="Incorrect username or password")
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username, "scope": " ".join(form_data.scopes)},
            expires_delta=access_token_expires,
        )
        return Token(access_token=access_token, token_type="bearer")
    
    
    @app.get("/users/me/")
    async def read_users_me(current_user: User = Depends(get_current_active_user)) -> User:
        return current_user
    
    
    @app.get("/users/me/items/")
    async def read_own_items(
        current_user: User = Security(get_current_active_user, scopes=["items"]),
    ):
        return [{"item_id": "Foo", "owner": current_user.username}]
    
    
    @app.get("/status/")
    async def read_system_status(current_user: User = Depends(get_current_user)):
        return {"status": "ok"}
    

```

Теперь рассмотрим эти изменения шаг за шагом.

## OAuth2 схема безопасности

Первое изменение — мы объявляем схему безопасности OAuth2 с двумя доступными scopes: `me` и `items`.

Параметр `scopes` получает `dict`, где каждый scope — это ключ, а описание — значение:

Python 3.10+

```
 
    from datetime import datetime, timedelta, timezone
    from typing import Annotated
    
    import jwt
    from fastapi import Depends, FastAPI, HTTPException, Security, status
    from fastapi.security import (
        OAuth2PasswordBearer,
        OAuth2PasswordRequestForm,
        SecurityScopes,
    )
    from jwt.exceptions import InvalidTokenError
    from pwdlib import PasswordHash
    from pydantic import BaseModel, ValidationError
    
    # to get a string like this run:
    # openssl rand -hex 32
    SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    
    
    fake_users_db = {
        "johndoe": {
            "username": "johndoe",
            "full_name": "John Doe",
            "email": "johndoe@example.com",
            "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$wagCPXjifgvUFBzq4hqe3w$CYaIb8sB+wtD+Vu/P4uod1+Qof8h+1g7bbDlBID48Rc",
            "disabled": False,
        },
        "alice": {
            "username": "alice",
            "full_name": "Alice Chains",
            "email": "alicechains@example.com",
            "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$g2/AV1zwopqUntPKJavBFw$BwpRGDCyUHLvHICnwijyX8ROGoiUPwNKZ7915MeYfCE",
            "disabled": True,
        },
    }
    
    
    class Token(BaseModel):
        access_token: str
        token_type: str
    
    
    class TokenData(BaseModel):
        username: str | None = None
        scopes: list[str] = []
    
    
    class User(BaseModel):
        username: str
        email: str | None = None
        full_name: str | None = None
        disabled: bool | None = None
    
    
    class UserInDB(User):
        hashed_password: str
    
    
    password_hash = PasswordHash.recommended()
    
    DUMMY_HASH = password_hash.hash("dummypassword")
    
    oauth2_scheme = OAuth2PasswordBearer(
        tokenUrl="token",
        scopes={"me": "Read information about the current user.", "items": "Read items."},
    )
    
    app = FastAPI()
    
    
    def verify_password(plain_password, hashed_password):
        return password_hash.verify(plain_password, hashed_password)
    
    
    def get_password_hash(password):
        return password_hash.hash(password)
    
    
    def get_user(db, username: str):
        if username in db:
            user_dict = db[username]
            return UserInDB(**user_dict)
    
    
    def authenticate_user(fake_db, username: str, password: str):
        user = get_user(fake_db, username)
        if not user:
            verify_password(password, DUMMY_HASH)
            return False
        if not verify_password(password, user.hashed_password):
            return False
        return user
    
    
    def create_access_token(data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    
    
    async def get_current_user(
        security_scopes: SecurityScopes, token: Annotated[str, Depends(oauth2_scheme)]
    ):
        if security_scopes.scopes:
            authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
        else:
            authenticate_value = "Bearer"
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": authenticate_value},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username = payload.get("sub")
            if username is None:
                raise credentials_exception
            scope: str = payload.get("scope", "")
            token_scopes = scope.split(" ")
            token_data = TokenData(scopes=token_scopes, username=username)
        except (InvalidTokenError, ValidationError):
            raise credentials_exception
        user = get_user(fake_users_db, username=token_data.username)
        if user is None:
            raise credentials_exception
        for scope in security_scopes.scopes:
            if scope not in token_data.scopes:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Not enough permissions",
                    headers={"WWW-Authenticate": authenticate_value},
                )
        return user
    
    
    async def get_current_active_user(
        current_user: Annotated[User, Security(get_current_user, scopes=["me"])],
    ):
        if current_user.disabled:
            raise HTTPException(status_code=400, detail="Inactive user")
        return current_user
    
    
    @app.post("/token")
    async def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    ) -> Token:
        user = authenticate_user(fake_users_db, form_data.username, form_data.password)
        if not user:
            raise HTTPException(status_code=400, detail="Incorrect username or password")
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username, "scope": " ".join(form_data.scopes)},
            expires_delta=access_token_expires,
        )
        return Token(access_token=access_token, token_type="bearer")
    
    
    @app.get("/users/me/")
    async def read_users_me(
        current_user: Annotated[User, Depends(get_current_active_user)],
    ) -> User:
        return current_user
    
    
    @app.get("/users/me/items/")
    async def read_own_items(
        current_user: Annotated[User, Security(get_current_active_user, scopes=["items"])],
    ):
        return [{"item_id": "Foo", "owner": current_user.username}]
    
    
    @app.get("/status/")
    async def read_system_status(current_user: Annotated[User, Depends(get_current_user)]):
        return {"status": "ok"}
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from datetime import datetime, timedelta, timezone
    
    import jwt
    from fastapi import Depends, FastAPI, HTTPException, Security, status
    from fastapi.security import (
        OAuth2PasswordBearer,
        OAuth2PasswordRequestForm,
        SecurityScopes,
    )
    from jwt.exceptions import InvalidTokenError
    from pwdlib import PasswordHash
    from pydantic import BaseModel, ValidationError
    
    # to get a string like this run:
    # openssl rand -hex 32
    SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    
    
    fake_users_db = {
        "johndoe": {
            "username": "johndoe",
            "full_name": "John Doe",
            "email": "johndoe@example.com",
            "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$wagCPXjifgvUFBzq4hqe3w$CYaIb8sB+wtD+Vu/P4uod1+Qof8h+1g7bbDlBID48Rc",
            "disabled": False,
        },
        "alice": {
            "username": "alice",
            "full_name": "Alice Chains",
            "email": "alicechains@example.com",
            "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$g2/AV1zwopqUntPKJavBFw$BwpRGDCyUHLvHICnwijyX8ROGoiUPwNKZ7915MeYfCE",
            "disabled": True,
        },
    }
    
    
    class Token(BaseModel):
        access_token: str
        token_type: str
    
    
    class TokenData(BaseModel):
        username: str | None = None
        scopes: list[str] = []
    
    
    class User(BaseModel):
        username: str
        email: str | None = None
        full_name: str | None = None
        disabled: bool | None = None
    
    
    class UserInDB(User):
        hashed_password: str
    
    
    password_hash = PasswordHash.recommended()
    
    DUMMY_HASH = password_hash.hash("dummypassword")
    
    oauth2_scheme = OAuth2PasswordBearer(
        tokenUrl="token",
        scopes={"me": "Read information about the current user.", "items": "Read items."},
    )
    
    app = FastAPI()
    
    
    def verify_password(plain_password, hashed_password):
        return password_hash.verify(plain_password, hashed_password)
    
    
    def get_password_hash(password):
        return password_hash.hash(password)
    
    
    def get_user(db, username: str):
        if username in db:
            user_dict = db[username]
            return UserInDB(**user_dict)
    
    
    def authenticate_user(fake_db, username: str, password: str):
        user = get_user(fake_db, username)
        if not user:
            verify_password(password, DUMMY_HASH)
            return False
        if not verify_password(password, user.hashed_password):
            return False
        return user
    
    
    def create_access_token(data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    
    
    async def get_current_user(
        security_scopes: SecurityScopes, token: str = Depends(oauth2_scheme)
    ):
        if security_scopes.scopes:
            authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
        else:
            authenticate_value = "Bearer"
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": authenticate_value},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
            scope: str = payload.get("scope", "")
            token_scopes = scope.split(" ")
            token_data = TokenData(scopes=token_scopes, username=username)
        except (InvalidTokenError, ValidationError):
            raise credentials_exception
        user = get_user(fake_users_db, username=token_data.username)
        if user is None:
            raise credentials_exception
        for scope in security_scopes.scopes:
            if scope not in token_data.scopes:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Not enough permissions",
                    headers={"WWW-Authenticate": authenticate_value},
                )
        return user
    
    
    async def get_current_active_user(
        current_user: User = Security(get_current_user, scopes=["me"]),
    ):
        if current_user.disabled:
            raise HTTPException(status_code=400, detail="Inactive user")
        return current_user
    
    
    @app.post("/token")
    async def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
    ) -> Token:
        user = authenticate_user(fake_users_db, form_data.username, form_data.password)
        if not user:
            raise HTTPException(status_code=400, detail="Incorrect username or password")
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username, "scope": " ".join(form_data.scopes)},
            expires_delta=access_token_expires,
        )
        return Token(access_token=access_token, token_type="bearer")
    
    
    @app.get("/users/me/")
    async def read_users_me(current_user: User = Depends(get_current_active_user)) -> User:
        return current_user
    
    
    @app.get("/users/me/items/")
    async def read_own_items(
        current_user: User = Security(get_current_active_user, scopes=["items"]),
    ):
        return [{"item_id": "Foo", "owner": current_user.username}]
    
    
    @app.get("/status/")
    async def read_system_status(current_user: User = Depends(get_current_user)):
        return {"status": "ok"}
    

```

Так как теперь мы объявляем эти scopes, они появятся в документации API при входе/авторизации.

И вы сможете выбрать, какие scopes вы хотите выдать доступ: `me` и `items`.

Это тот же механизм, когда вы даёте разрешения при входе через Facebook, Google, GitHub и т.д.:

![](https://fastapi.tiangolo.com/img/tutorial/security/image11.png)

## JWT-токены со scopes

Теперь измените операцию пути, выдающую токен, чтобы возвращать запрошенные scopes.

Мы всё ещё используем тот же `OAuth2PasswordRequestForm`. Он включает свойство `scopes` с `list` из `str` — каждый scope, полученный в запросе.

И мы возвращаем scopes как часть JWT‑токена.

Опасность

Для простоты здесь мы просто добавляем полученные scopes прямо в токен.

Но в вашем приложении, в целях безопасности, следует убедиться, что вы добавляете только те scopes, которые пользователь действительно может иметь, или те, которые вы заранее определили.

Python 3.10+

```
 
    from datetime import datetime, timedelta, timezone
    from typing import Annotated
    
    import jwt
    from fastapi import Depends, FastAPI, HTTPException, Security, status
    from fastapi.security import (
        OAuth2PasswordBearer,
        OAuth2PasswordRequestForm,
        SecurityScopes,
    )
    from jwt.exceptions import InvalidTokenError
    from pwdlib import PasswordHash
    from pydantic import BaseModel, ValidationError
    
    # to get a string like this run:
    # openssl rand -hex 32
    SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    
    
    fake_users_db = {
        "johndoe": {
            "username": "johndoe",
            "full_name": "John Doe",
            "email": "johndoe@example.com",
            "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$wagCPXjifgvUFBzq4hqe3w$CYaIb8sB+wtD+Vu/P4uod1+Qof8h+1g7bbDlBID48Rc",
            "disabled": False,
        },
        "alice": {
            "username": "alice",
            "full_name": "Alice Chains",
            "email": "alicechains@example.com",
            "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$g2/AV1zwopqUntPKJavBFw$BwpRGDCyUHLvHICnwijyX8ROGoiUPwNKZ7915MeYfCE",
            "disabled": True,
        },
    }
    
    
    class Token(BaseModel):
        access_token: str
        token_type: str
    
    
    class TokenData(BaseModel):
        username: str | None = None
        scopes: list[str] = []
    
    
    class User(BaseModel):
        username: str
        email: str | None = None
        full_name: str | None = None
        disabled: bool | None = None
    
    
    class UserInDB(User):
        hashed_password: str
    
    
    password_hash = PasswordHash.recommended()
    
    DUMMY_HASH = password_hash.hash("dummypassword")
    
    oauth2_scheme = OAuth2PasswordBearer(
        tokenUrl="token",
        scopes={"me": "Read information about the current user.", "items": "Read items."},
    )
    
    app = FastAPI()
    
    
    def verify_password(plain_password, hashed_password):
        return password_hash.verify(plain_password, hashed_password)
    
    
    def get_password_hash(password):
        return password_hash.hash(password)
    
    
    def get_user(db, username: str):
        if username in db:
            user_dict = db[username]
            return UserInDB(**user_dict)
    
    
    def authenticate_user(fake_db, username: str, password: str):
        user = get_user(fake_db, username)
        if not user:
            verify_password(password, DUMMY_HASH)
            return False
        if not verify_password(password, user.hashed_password):
            return False
        return user
    
    
    def create_access_token(data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    
    
    async def get_current_user(
        security_scopes: SecurityScopes, token: Annotated[str, Depends(oauth2_scheme)]
    ):
        if security_scopes.scopes:
            authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
        else:
            authenticate_value = "Bearer"
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": authenticate_value},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username = payload.get("sub")
            if username is None:
                raise credentials_exception
            scope: str = payload.get("scope", "")
            token_scopes = scope.split(" ")
            token_data = TokenData(scopes=token_scopes, username=username)
        except (InvalidTokenError, ValidationError):
            raise credentials_exception
        user = get_user(fake_users_db, username=token_data.username)
        if user is None:
            raise credentials_exception
        for scope in security_scopes.scopes:
            if scope not in token_data.scopes:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Not enough permissions",
                    headers={"WWW-Authenticate": authenticate_value},
                )
        return user
    
    
    async def get_current_active_user(
        current_user: Annotated[User, Security(get_current_user, scopes=["me"])],
    ):
        if current_user.disabled:
            raise HTTPException(status_code=400, detail="Inactive user")
        return current_user
    
    
    @app.post("/token")
    async def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    ) -> Token:
        user = authenticate_user(fake_users_db, form_data.username, form_data.password)
        if not user:
            raise HTTPException(status_code=400, detail="Incorrect username or password")
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username, "scope": " ".join(form_data.scopes)},
            expires_delta=access_token_expires,
        )
        return Token(access_token=access_token, token_type="bearer")
    
    
    @app.get("/users/me/")
    async def read_users_me(
        current_user: Annotated[User, Depends(get_current_active_user)],
    ) -> User:
        return current_user
    
    
    @app.get("/users/me/items/")
    async def read_own_items(
        current_user: Annotated[User, Security(get_current_active_user, scopes=["items"])],
    ):
        return [{"item_id": "Foo", "owner": current_user.username}]
    
    
    @app.get("/status/")
    async def read_system_status(current_user: Annotated[User, Depends(get_current_user)]):
        return {"status": "ok"}
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from datetime import datetime, timedelta, timezone
    
    import jwt
    from fastapi import Depends, FastAPI, HTTPException, Security, status
    from fastapi.security import (
        OAuth2PasswordBearer,
        OAuth2PasswordRequestForm,
        SecurityScopes,
    )
    from jwt.exceptions import InvalidTokenError
    from pwdlib import PasswordHash
    from pydantic import BaseModel, ValidationError
    
    # to get a string like this run:
    # openssl rand -hex 32
    SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    
    
    fake_users_db = {
        "johndoe": {
            "username": "johndoe",
            "full_name": "John Doe",
            "email": "johndoe@example.com",
            "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$wagCPXjifgvUFBzq4hqe3w$CYaIb8sB+wtD+Vu/P4uod1+Qof8h+1g7bbDlBID48Rc",
            "disabled": False,
        },
        "alice": {
            "username": "alice",
            "full_name": "Alice Chains",
            "email": "alicechains@example.com",
            "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$g2/AV1zwopqUntPKJavBFw$BwpRGDCyUHLvHICnwijyX8ROGoiUPwNKZ7915MeYfCE",
            "disabled": True,
        },
    }
    
    
    class Token(BaseModel):
        access_token: str
        token_type: str
    
    
    class TokenData(BaseModel):
        username: str | None = None
        scopes: list[str] = []
    
    
    class User(BaseModel):
        username: str
        email: str | None = None
        full_name: str | None = None
        disabled: bool | None = None
    
    
    class UserInDB(User):
        hashed_password: str
    
    
    password_hash = PasswordHash.recommended()
    
    DUMMY_HASH = password_hash.hash("dummypassword")
    
    oauth2_scheme = OAuth2PasswordBearer(
        tokenUrl="token",
        scopes={"me": "Read information about the current user.", "items": "Read items."},
    )
    
    app = FastAPI()
    
    
    def verify_password(plain_password, hashed_password):
        return password_hash.verify(plain_password, hashed_password)
    
    
    def get_password_hash(password):
        return password_hash.hash(password)
    
    
    def get_user(db, username: str):
        if username in db:
            user_dict = db[username]
            return UserInDB(**user_dict)
    
    
    def authenticate_user(fake_db, username: str, password: str):
        user = get_user(fake_db, username)
        if not user:
            verify_password(password, DUMMY_HASH)
            return False
        if not verify_password(password, user.hashed_password):
            return False
        return user
    
    
    def create_access_token(data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    
    
    async def get_current_user(
        security_scopes: SecurityScopes, token: str = Depends(oauth2_scheme)
    ):
        if security_scopes.scopes:
            authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
        else:
            authenticate_value = "Bearer"
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": authenticate_value},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
            scope: str = payload.get("scope", "")
            token_scopes = scope.split(" ")
            token_data = TokenData(scopes=token_scopes, username=username)
        except (InvalidTokenError, ValidationError):
            raise credentials_exception
        user = get_user(fake_users_db, username=token_data.username)
        if user is None:
            raise credentials_exception
        for scope in security_scopes.scopes:
            if scope not in token_data.scopes:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Not enough permissions",
                    headers={"WWW-Authenticate": authenticate_value},
                )
        return user
    
    
    async def get_current_active_user(
        current_user: User = Security(get_current_user, scopes=["me"]),
    ):
        if current_user.disabled:
            raise HTTPException(status_code=400, detail="Inactive user")
        return current_user
    
    
    @app.post("/token")
    async def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
    ) -> Token:
        user = authenticate_user(fake_users_db, form_data.username, form_data.password)
        if not user:
            raise HTTPException(status_code=400, detail="Incorrect username or password")
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username, "scope": " ".join(form_data.scopes)},
            expires_delta=access_token_expires,
        )
        return Token(access_token=access_token, token_type="bearer")
    
    
    @app.get("/users/me/")
    async def read_users_me(current_user: User = Depends(get_current_active_user)) -> User:
        return current_user
    
    
    @app.get("/users/me/items/")
    async def read_own_items(
        current_user: User = Security(get_current_active_user, scopes=["items"]),
    ):
        return [{"item_id": "Foo", "owner": current_user.username}]
    
    
    @app.get("/status/")
    async def read_system_status(current_user: User = Depends(get_current_user)):
        return {"status": "ok"}
    

```

## Объявление scopes в _обработчиках путей_ и зависимостях

Теперь объявим, что операция пути для `/users/me/items/` требует scope `items`.

Для этого импортируем и используем `Security` из `fastapi`.

Вы можете использовать `Security` для объявления зависимостей (как `Depends`), но `Security` также принимает параметр `scopes` со списком scopes (строк).

В этом случае мы передаём функцию‑зависимость `get_current_active_user` в `Security` (точно так же, как сделали бы с `Depends`).

Но мы также передаём `list` scopes — в данном случае только один scope: `items` (их могло быть больше).

И функция‑зависимость `get_current_active_user` тоже может объявлять подзависимости не только через `Depends`, но и через `Security`, объявляя свою подзависимость (`get_current_user`) и дополнительные требования по scopes.

В данном случае требуется scope `me` (их также могло быть больше одного).

Примечание

Вам не обязательно добавлять разные scopes в разных местах.

Мы делаем это здесь, чтобы показать, как **FastAPI** обрабатывает scopes, объявленные на разных уровнях.

Python 3.10+

```
 
    from datetime import datetime, timedelta, timezone
    from typing import Annotated
    
    import jwt
    from fastapi import Depends, FastAPI, HTTPException, Security, status
    from fastapi.security import (
        OAuth2PasswordBearer,
        OAuth2PasswordRequestForm,
        SecurityScopes,
    )
    from jwt.exceptions import InvalidTokenError
    from pwdlib import PasswordHash
    from pydantic import BaseModel, ValidationError
    
    # to get a string like this run:
    # openssl rand -hex 32
    SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    
    
    fake_users_db = {
        "johndoe": {
            "username": "johndoe",
            "full_name": "John Doe",
            "email": "johndoe@example.com",
            "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$wagCPXjifgvUFBzq4hqe3w$CYaIb8sB+wtD+Vu/P4uod1+Qof8h+1g7bbDlBID48Rc",
            "disabled": False,
        },
        "alice": {
            "username": "alice",
            "full_name": "Alice Chains",
            "email": "alicechains@example.com",
            "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$g2/AV1zwopqUntPKJavBFw$BwpRGDCyUHLvHICnwijyX8ROGoiUPwNKZ7915MeYfCE",
            "disabled": True,
        },
    }
    
    
    class Token(BaseModel):
        access_token: str
        token_type: str
    
    
    class TokenData(BaseModel):
        username: str | None = None
        scopes: list[str] = []
    
    
    class User(BaseModel):
        username: str
        email: str | None = None
        full_name: str | None = None
        disabled: bool | None = None
    
    
    class UserInDB(User):
        hashed_password: str
    
    
    password_hash = PasswordHash.recommended()
    
    DUMMY_HASH = password_hash.hash("dummypassword")
    
    oauth2_scheme = OAuth2PasswordBearer(
        tokenUrl="token",
        scopes={"me": "Read information about the current user.", "items": "Read items."},
    )
    
    app = FastAPI()
    
    
    def verify_password(plain_password, hashed_password):
        return password_hash.verify(plain_password, hashed_password)
    
    
    def get_password_hash(password):
        return password_hash.hash(password)
    
    
    def get_user(db, username: str):
        if username in db:
            user_dict = db[username]
            return UserInDB(**user_dict)
    
    
    def authenticate_user(fake_db, username: str, password: str):
        user = get_user(fake_db, username)
        if not user:
            verify_password(password, DUMMY_HASH)
            return False
        if not verify_password(password, user.hashed_password):
            return False
        return user
    
    
    def create_access_token(data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    
    
    async def get_current_user(
        security_scopes: SecurityScopes, token: Annotated[str, Depends(oauth2_scheme)]
    ):
        if security_scopes.scopes:
            authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
        else:
            authenticate_value = "Bearer"
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": authenticate_value},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username = payload.get("sub")
            if username is None:
                raise credentials_exception
            scope: str = payload.get("scope", "")
            token_scopes = scope.split(" ")
            token_data = TokenData(scopes=token_scopes, username=username)
        except (InvalidTokenError, ValidationError):
            raise credentials_exception
        user = get_user(fake_users_db, username=token_data.username)
        if user is None:
            raise credentials_exception
        for scope in security_scopes.scopes:
            if scope not in token_data.scopes:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Not enough permissions",
                    headers={"WWW-Authenticate": authenticate_value},
                )
        return user
    
    
    async def get_current_active_user(
        current_user: Annotated[User, Security(get_current_user, scopes=["me"])],
    ):
        if current_user.disabled:
            raise HTTPException(status_code=400, detail="Inactive user")
        return current_user
    
    
    @app.post("/token")
    async def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    ) -> Token:
        user = authenticate_user(fake_users_db, form_data.username, form_data.password)
        if not user:
            raise HTTPException(status_code=400, detail="Incorrect username or password")
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username, "scope": " ".join(form_data.scopes)},
            expires_delta=access_token_expires,
        )
        return Token(access_token=access_token, token_type="bearer")
    
    
    @app.get("/users/me/")
    async def read_users_me(
        current_user: Annotated[User, Depends(get_current_active_user)],
    ) -> User:
        return current_user
    
    
    @app.get("/users/me/items/")
    async def read_own_items(
        current_user: Annotated[User, Security(get_current_active_user, scopes=["items"])],
    ):
        return [{"item_id": "Foo", "owner": current_user.username}]
    
    
    @app.get("/status/")
    async def read_system_status(current_user: Annotated[User, Depends(get_current_user)]):
        return {"status": "ok"}
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from datetime import datetime, timedelta, timezone
    
    import jwt
    from fastapi import Depends, FastAPI, HTTPException, Security, status
    from fastapi.security import (
        OAuth2PasswordBearer,
        OAuth2PasswordRequestForm,
        SecurityScopes,
    )
    from jwt.exceptions import InvalidTokenError
    from pwdlib import PasswordHash
    from pydantic import BaseModel, ValidationError
    
    # to get a string like this run:
    # openssl rand -hex 32
    SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    
    
    fake_users_db = {
        "johndoe": {
            "username": "johndoe",
            "full_name": "John Doe",
            "email": "johndoe@example.com",
            "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$wagCPXjifgvUFBzq4hqe3w$CYaIb8sB+wtD+Vu/P4uod1+Qof8h+1g7bbDlBID48Rc",
            "disabled": False,
        },
        "alice": {
            "username": "alice",
            "full_name": "Alice Chains",
            "email": "alicechains@example.com",
            "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$g2/AV1zwopqUntPKJavBFw$BwpRGDCyUHLvHICnwijyX8ROGoiUPwNKZ7915MeYfCE",
            "disabled": True,
        },
    }
    
    
    class Token(BaseModel):
        access_token: str
        token_type: str
    
    
    class TokenData(BaseModel):
        username: str | None = None
        scopes: list[str] = []
    
    
    class User(BaseModel):
        username: str
        email: str | None = None
        full_name: str | None = None
        disabled: bool | None = None
    
    
    class UserInDB(User):
        hashed_password: str
    
    
    password_hash = PasswordHash.recommended()
    
    DUMMY_HASH = password_hash.hash("dummypassword")
    
    oauth2_scheme = OAuth2PasswordBearer(
        tokenUrl="token",
        scopes={"me": "Read information about the current user.", "items": "Read items."},
    )
    
    app = FastAPI()
    
    
    def verify_password(plain_password, hashed_password):
        return password_hash.verify(plain_password, hashed_password)
    
    
    def get_password_hash(password):
        return password_hash.hash(password)
    
    
    def get_user(db, username: str):
        if username in db:
            user_dict = db[username]
            return UserInDB(**user_dict)
    
    
    def authenticate_user(fake_db, username: str, password: str):
        user = get_user(fake_db, username)
        if not user:
            verify_password(password, DUMMY_HASH)
            return False
        if not verify_password(password, user.hashed_password):
            return False
        return user
    
    
    def create_access_token(data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    
    
    async def get_current_user(
        security_scopes: SecurityScopes, token: str = Depends(oauth2_scheme)
    ):
        if security_scopes.scopes:
            authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
        else:
            authenticate_value = "Bearer"
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": authenticate_value},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
            scope: str = payload.get("scope", "")
            token_scopes = scope.split(" ")
            token_data = TokenData(scopes=token_scopes, username=username)
        except (InvalidTokenError, ValidationError):
            raise credentials_exception
        user = get_user(fake_users_db, username=token_data.username)
        if user is None:
            raise credentials_exception
        for scope in security_scopes.scopes:
            if scope not in token_data.scopes:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Not enough permissions",
                    headers={"WWW-Authenticate": authenticate_value},
                )
        return user
    
    
    async def get_current_active_user(
        current_user: User = Security(get_current_user, scopes=["me"]),
    ):
        if current_user.disabled:
            raise HTTPException(status_code=400, detail="Inactive user")
        return current_user
    
    
    @app.post("/token")
    async def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
    ) -> Token:
        user = authenticate_user(fake_users_db, form_data.username, form_data.password)
        if not user:
            raise HTTPException(status_code=400, detail="Incorrect username or password")
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username, "scope": " ".join(form_data.scopes)},
            expires_delta=access_token_expires,
        )
        return Token(access_token=access_token, token_type="bearer")
    
    
    @app.get("/users/me/")
    async def read_users_me(current_user: User = Depends(get_current_active_user)) -> User:
        return current_user
    
    
    @app.get("/users/me/items/")
    async def read_own_items(
        current_user: User = Security(get_current_active_user, scopes=["items"]),
    ):
        return [{"item_id": "Foo", "owner": current_user.username}]
    
    
    @app.get("/status/")
    async def read_system_status(current_user: User = Depends(get_current_user)):
        return {"status": "ok"}
    

```

Технические детали

`Security` на самом деле является подклассом `Depends` и имеет всего один дополнительный параметр, который мы рассмотрим позже.

Но используя `Security` вместо `Depends`, **FastAPI** будет знать, что можно объявлять security scopes, использовать их внутри и документировать API в OpenAPI.

Однако когда вы импортируете `Query`, `Path`, `Depends`, `Security` и другие из `fastapi`, это на самом деле функции, возвращающие специальные классы.

## Использование `SecurityScopes`

Теперь обновим зависимость `get_current_user`.

Именно её используют зависимости выше.

Здесь мы используем ту же схему OAuth2, созданную ранее, объявляя её как зависимость: `oauth2_scheme`.

Поскольку у этой функции‑зависимости нет собственных требований по scopes, мы можем использовать `Depends` с `oauth2_scheme` — нам не нужно использовать `Security`, если не требуется указывать security scopes.

Мы также объявляем специальный параметр типа `SecurityScopes`, импортированный из `fastapi.security`.

Класс `SecurityScopes` похож на `Request` (через `Request` мы получали сам объект запроса).

Python 3.10+

```
 
    from datetime import datetime, timedelta, timezone
    from typing import Annotated
    
    import jwt
    from fastapi import Depends, FastAPI, HTTPException, Security, status
    from fastapi.security import (
        OAuth2PasswordBearer,
        OAuth2PasswordRequestForm,
        SecurityScopes,
    )
    from jwt.exceptions import InvalidTokenError
    from pwdlib import PasswordHash
    from pydantic import BaseModel, ValidationError
    
    # to get a string like this run:
    # openssl rand -hex 32
    SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    
    
    fake_users_db = {
        "johndoe": {
            "username": "johndoe",
            "full_name": "John Doe",
            "email": "johndoe@example.com",
            "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$wagCPXjifgvUFBzq4hqe3w$CYaIb8sB+wtD+Vu/P4uod1+Qof8h+1g7bbDlBID48Rc",
            "disabled": False,
        },
        "alice": {
            "username": "alice",
            "full_name": "Alice Chains",
            "email": "alicechains@example.com",
            "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$g2/AV1zwopqUntPKJavBFw$BwpRGDCyUHLvHICnwijyX8ROGoiUPwNKZ7915MeYfCE",
            "disabled": True,
        },
    }
    
    
    class Token(BaseModel):
        access_token: str
        token_type: str
    
    
    class TokenData(BaseModel):
        username: str | None = None
        scopes: list[str] = []
    
    
    class User(BaseModel):
        username: str
        email: str | None = None
        full_name: str | None = None
        disabled: bool | None = None
    
    
    class UserInDB(User):
        hashed_password: str
    
    
    password_hash = PasswordHash.recommended()
    
    DUMMY_HASH = password_hash.hash("dummypassword")
    
    oauth2_scheme = OAuth2PasswordBearer(
        tokenUrl="token",
        scopes={"me": "Read information about the current user.", "items": "Read items."},
    )
    
    app = FastAPI()
    
    
    def verify_password(plain_password, hashed_password):
        return password_hash.verify(plain_password, hashed_password)
    
    
    def get_password_hash(password):
        return password_hash.hash(password)
    
    
    def get_user(db, username: str):
        if username in db:
            user_dict = db[username]
            return UserInDB(**user_dict)
    
    
    def authenticate_user(fake_db, username: str, password: str):
        user = get_user(fake_db, username)
        if not user:
            verify_password(password, DUMMY_HASH)
            return False
        if not verify_password(password, user.hashed_password):
            return False
        return user
    
    
    def create_access_token(data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    
    
    async def get_current_user(
        security_scopes: SecurityScopes, token: Annotated[str, Depends(oauth2_scheme)]
    ):
        if security_scopes.scopes:
            authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
        else:
            authenticate_value = "Bearer"
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": authenticate_value},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username = payload.get("sub")
            if username is None:
                raise credentials_exception
            scope: str = payload.get("scope", "")
            token_scopes = scope.split(" ")
            token_data = TokenData(scopes=token_scopes, username=username)
        except (InvalidTokenError, ValidationError):
            raise credentials_exception
        user = get_user(fake_users_db, username=token_data.username)
        if user is None:
            raise credentials_exception
        for scope in security_scopes.scopes:
            if scope not in token_data.scopes:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Not enough permissions",
                    headers={"WWW-Authenticate": authenticate_value},
                )
        return user
    
    
    async def get_current_active_user(
        current_user: Annotated[User, Security(get_current_user, scopes=["me"])],
    ):
        if current_user.disabled:
            raise HTTPException(status_code=400, detail="Inactive user")
        return current_user
    
    
    @app.post("/token")
    async def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    ) -> Token:
        user = authenticate_user(fake_users_db, form_data.username, form_data.password)
        if not user:
            raise HTTPException(status_code=400, detail="Incorrect username or password")
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username, "scope": " ".join(form_data.scopes)},
            expires_delta=access_token_expires,
        )
        return Token(access_token=access_token, token_type="bearer")
    
    
    @app.get("/users/me/")
    async def read_users_me(
        current_user: Annotated[User, Depends(get_current_active_user)],
    ) -> User:
        return current_user
    
    
    @app.get("/users/me/items/")
    async def read_own_items(
        current_user: Annotated[User, Security(get_current_active_user, scopes=["items"])],
    ):
        return [{"item_id": "Foo", "owner": current_user.username}]
    
    
    @app.get("/status/")
    async def read_system_status(current_user: Annotated[User, Depends(get_current_user)]):
        return {"status": "ok"}
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from datetime import datetime, timedelta, timezone
    
    import jwt
    from fastapi import Depends, FastAPI, HTTPException, Security, status
    from fastapi.security import (
        OAuth2PasswordBearer,
        OAuth2PasswordRequestForm,
        SecurityScopes,
    )
    from jwt.exceptions import InvalidTokenError
    from pwdlib import PasswordHash
    from pydantic import BaseModel, ValidationError
    
    # to get a string like this run:
    # openssl rand -hex 32
    SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    
    
    fake_users_db = {
        "johndoe": {
            "username": "johndoe",
            "full_name": "John Doe",
            "email": "johndoe@example.com",
            "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$wagCPXjifgvUFBzq4hqe3w$CYaIb8sB+wtD+Vu/P4uod1+Qof8h+1g7bbDlBID48Rc",
            "disabled": False,
        },
        "alice": {
            "username": "alice",
            "full_name": "Alice Chains",
            "email": "alicechains@example.com",
            "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$g2/AV1zwopqUntPKJavBFw$BwpRGDCyUHLvHICnwijyX8ROGoiUPwNKZ7915MeYfCE",
            "disabled": True,
        },
    }
    
    
    class Token(BaseModel):
        access_token: str
        token_type: str
    
    
    class TokenData(BaseModel):
        username: str | None = None
        scopes: list[str] = []
    
    
    class User(BaseModel):
        username: str
        email: str | None = None
        full_name: str | None = None
        disabled: bool | None = None
    
    
    class UserInDB(User):
        hashed_password: str
    
    
    password_hash = PasswordHash.recommended()
    
    DUMMY_HASH = password_hash.hash("dummypassword")
    
    oauth2_scheme = OAuth2PasswordBearer(
        tokenUrl="token",
        scopes={"me": "Read information about the current user.", "items": "Read items."},
    )
    
    app = FastAPI()
    
    
    def verify_password(plain_password, hashed_password):
        return password_hash.verify(plain_password, hashed_password)
    
    
    def get_password_hash(password):
        return password_hash.hash(password)
    
    
    def get_user(db, username: str):
        if username in db:
            user_dict = db[username]
            return UserInDB(**user_dict)
    
    
    def authenticate_user(fake_db, username: str, password: str):
        user = get_user(fake_db, username)
        if not user:
            verify_password(password, DUMMY_HASH)
            return False
        if not verify_password(password, user.hashed_password):
            return False
        return user
    
    
    def create_access_token(data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    
    
    async def get_current_user(
        security_scopes: SecurityScopes, token: str = Depends(oauth2_scheme)
    ):
        if security_scopes.scopes:
            authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
        else:
            authenticate_value = "Bearer"
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": authenticate_value},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
            scope: str = payload.get("scope", "")
            token_scopes = scope.split(" ")
            token_data = TokenData(scopes=token_scopes, username=username)
        except (InvalidTokenError, ValidationError):
            raise credentials_exception
        user = get_user(fake_users_db, username=token_data.username)
        if user is None:
            raise credentials_exception
        for scope in security_scopes.scopes:
            if scope not in token_data.scopes:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Not enough permissions",
                    headers={"WWW-Authenticate": authenticate_value},
                )
        return user
    
    
    async def get_current_active_user(
        current_user: User = Security(get_current_user, scopes=["me"]),
    ):
        if current_user.disabled:
            raise HTTPException(status_code=400, detail="Inactive user")
        return current_user
    
    
    @app.post("/token")
    async def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
    ) -> Token:
        user = authenticate_user(fake_users_db, form_data.username, form_data.password)
        if not user:
            raise HTTPException(status_code=400, detail="Incorrect username or password")
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username, "scope": " ".join(form_data.scopes)},
            expires_delta=access_token_expires,
        )
        return Token(access_token=access_token, token_type="bearer")
    
    
    @app.get("/users/me/")
    async def read_users_me(current_user: User = Depends(get_current_active_user)) -> User:
        return current_user
    
    
    @app.get("/users/me/items/")
    async def read_own_items(
        current_user: User = Security(get_current_active_user, scopes=["items"]),
    ):
        return [{"item_id": "Foo", "owner": current_user.username}]
    
    
    @app.get("/status/")
    async def read_system_status(current_user: User = Depends(get_current_user)):
        return {"status": "ok"}
    

```

## Использование `scopes`

Параметр `security_scopes` будет типа `SecurityScopes`.

У него есть свойство `scopes` со списком, содержащим все scopes, требуемые им самим и всеми зависимостями, использующими его как подзависимость. То есть всеми «зависящими»… это может звучать запутанно, ниже есть дополнительное объяснение.

Объект `security_scopes` (класс `SecurityScopes`) также предоставляет атрибут `scope_str` — это одна строка с этими scopes, разделёнными пробелами (мы будем её использовать).

Мы создаём `HTTPException`, который можем переиспользовать (`raise`) в нескольких местах.

В этом исключении мы включаем требуемые scopes (если есть) в виде строки, разделённой пробелами (используя `scope_str`). Эту строку со scopes мы помещаем в HTTP‑заголовок `WWW-Authenticate` (это часть спецификации).

Python 3.10+

```
 
    from datetime import datetime, timedelta, timezone
    from typing import Annotated
    
    import jwt
    from fastapi import Depends, FastAPI, HTTPException, Security, status
    from fastapi.security import (
        OAuth2PasswordBearer,
        OAuth2PasswordRequestForm,
        SecurityScopes,
    )
    from jwt.exceptions import InvalidTokenError
    from pwdlib import PasswordHash
    from pydantic import BaseModel, ValidationError
    
    # to get a string like this run:
    # openssl rand -hex 32
    SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    
    
    fake_users_db = {
        "johndoe": {
            "username": "johndoe",
            "full_name": "John Doe",
            "email": "johndoe@example.com",
            "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$wagCPXjifgvUFBzq4hqe3w$CYaIb8sB+wtD+Vu/P4uod1+Qof8h+1g7bbDlBID48Rc",
            "disabled": False,
        },
        "alice": {
            "username": "alice",
            "full_name": "Alice Chains",
            "email": "alicechains@example.com",
            "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$g2/AV1zwopqUntPKJavBFw$BwpRGDCyUHLvHICnwijyX8ROGoiUPwNKZ7915MeYfCE",
            "disabled": True,
        },
    }
    
    
    class Token(BaseModel):
        access_token: str
        token_type: str
    
    
    class TokenData(BaseModel):
        username: str | None = None
        scopes: list[str] = []
    
    
    class User(BaseModel):
        username: str
        email: str | None = None
        full_name: str | None = None
        disabled: bool | None = None
    
    
    class UserInDB(User):
        hashed_password: str
    
    
    password_hash = PasswordHash.recommended()
    
    DUMMY_HASH = password_hash.hash("dummypassword")
    
    oauth2_scheme = OAuth2PasswordBearer(
        tokenUrl="token",
        scopes={"me": "Read information about the current user.", "items": "Read items."},
    )
    
    app = FastAPI()
    
    
    def verify_password(plain_password, hashed_password):
        return password_hash.verify(plain_password, hashed_password)
    
    
    def get_password_hash(password):
        return password_hash.hash(password)
    
    
    def get_user(db, username: str):
        if username in db:
            user_dict = db[username]
            return UserInDB(**user_dict)
    
    
    def authenticate_user(fake_db, username: str, password: str):
        user = get_user(fake_db, username)
        if not user:
            verify_password(password, DUMMY_HASH)
            return False
        if not verify_password(password, user.hashed_password):
            return False
        return user
    
    
    def create_access_token(data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    
    
    async def get_current_user(
        security_scopes: SecurityScopes, token: Annotated[str, Depends(oauth2_scheme)]
    ):
        if security_scopes.scopes:
            authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
        else:
            authenticate_value = "Bearer"
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": authenticate_value},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username = payload.get("sub")
            if username is None:
                raise credentials_exception
            scope: str = payload.get("scope", "")
            token_scopes = scope.split(" ")
            token_data = TokenData(scopes=token_scopes, username=username)
        except (InvalidTokenError, ValidationError):
            raise credentials_exception
        user = get_user(fake_users_db, username=token_data.username)
        if user is None:
            raise credentials_exception
        for scope in security_scopes.scopes:
            if scope not in token_data.scopes:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Not enough permissions",
                    headers={"WWW-Authenticate": authenticate_value},
                )
        return user
    
    
    async def get_current_active_user(
        current_user: Annotated[User, Security(get_current_user, scopes=["me"])],
    ):
        if current_user.disabled:
            raise HTTPException(status_code=400, detail="Inactive user")
        return current_user
    
    
    @app.post("/token")
    async def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    ) -> Token:
        user = authenticate_user(fake_users_db, form_data.username, form_data.password)
        if not user:
            raise HTTPException(status_code=400, detail="Incorrect username or password")
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username, "scope": " ".join(form_data.scopes)},
            expires_delta=access_token_expires,
        )
        return Token(access_token=access_token, token_type="bearer")
    
    
    @app.get("/users/me/")
    async def read_users_me(
        current_user: Annotated[User, Depends(get_current_active_user)],
    ) -> User:
        return current_user
    
    
    @app.get("/users/me/items/")
    async def read_own_items(
        current_user: Annotated[User, Security(get_current_active_user, scopes=["items"])],
    ):
        return [{"item_id": "Foo", "owner": current_user.username}]
    
    
    @app.get("/status/")
    async def read_system_status(current_user: Annotated[User, Depends(get_current_user)]):
        return {"status": "ok"}
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from datetime import datetime, timedelta, timezone
    
    import jwt
    from fastapi import Depends, FastAPI, HTTPException, Security, status
    from fastapi.security import (
        OAuth2PasswordBearer,
        OAuth2PasswordRequestForm,
        SecurityScopes,
    )
    from jwt.exceptions import InvalidTokenError
    from pwdlib import PasswordHash
    from pydantic import BaseModel, ValidationError
    
    # to get a string like this run:
    # openssl rand -hex 32
    SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    
    
    fake_users_db = {
        "johndoe": {
            "username": "johndoe",
            "full_name": "John Doe",
            "email": "johndoe@example.com",
            "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$wagCPXjifgvUFBzq4hqe3w$CYaIb8sB+wtD+Vu/P4uod1+Qof8h+1g7bbDlBID48Rc",
            "disabled": False,
        },
        "alice": {
            "username": "alice",
            "full_name": "Alice Chains",
            "email": "alicechains@example.com",
            "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$g2/AV1zwopqUntPKJavBFw$BwpRGDCyUHLvHICnwijyX8ROGoiUPwNKZ7915MeYfCE",
            "disabled": True,
        },
    }
    
    
    class Token(BaseModel):
        access_token: str
        token_type: str
    
    
    class TokenData(BaseModel):
        username: str | None = None
        scopes: list[str] = []
    
    
    class User(BaseModel):
        username: str
        email: str | None = None
        full_name: str | None = None
        disabled: bool | None = None
    
    
    class UserInDB(User):
        hashed_password: str
    
    
    password_hash = PasswordHash.recommended()
    
    DUMMY_HASH = password_hash.hash("dummypassword")
    
    oauth2_scheme = OAuth2PasswordBearer(
        tokenUrl="token",
        scopes={"me": "Read information about the current user.", "items": "Read items."},
    )
    
    app = FastAPI()
    
    
    def verify_password(plain_password, hashed_password):
        return password_hash.verify(plain_password, hashed_password)
    
    
    def get_password_hash(password):
        return password_hash.hash(password)
    
    
    def get_user(db, username: str):
        if username in db:
            user_dict = db[username]
            return UserInDB(**user_dict)
    
    
    def authenticate_user(fake_db, username: str, password: str):
        user = get_user(fake_db, username)
        if not user:
            verify_password(password, DUMMY_HASH)
            return False
        if not verify_password(password, user.hashed_password):
            return False
        return user
    
    
    def create_access_token(data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    
    
    async def get_current_user(
        security_scopes: SecurityScopes, token: str = Depends(oauth2_scheme)
    ):
        if security_scopes.scopes:
            authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
        else:
            authenticate_value = "Bearer"
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": authenticate_value},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
            scope: str = payload.get("scope", "")
            token_scopes = scope.split(" ")
            token_data = TokenData(scopes=token_scopes, username=username)
        except (InvalidTokenError, ValidationError):
            raise credentials_exception
        user = get_user(fake_users_db, username=token_data.username)
        if user is None:
            raise credentials_exception
        for scope in security_scopes.scopes:
            if scope not in token_data.scopes:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Not enough permissions",
                    headers={"WWW-Authenticate": authenticate_value},
                )
        return user
    
    
    async def get_current_active_user(
        current_user: User = Security(get_current_user, scopes=["me"]),
    ):
        if current_user.disabled:
            raise HTTPException(status_code=400, detail="Inactive user")
        return current_user
    
    
    @app.post("/token")
    async def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
    ) -> Token:
        user = authenticate_user(fake_users_db, form_data.username, form_data.password)
        if not user:
            raise HTTPException(status_code=400, detail="Incorrect username or password")
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username, "scope": " ".join(form_data.scopes)},
            expires_delta=access_token_expires,
        )
        return Token(access_token=access_token, token_type="bearer")
    
    
    @app.get("/users/me/")
    async def read_users_me(current_user: User = Depends(get_current_active_user)) -> User:
        return current_user
    
    
    @app.get("/users/me/items/")
    async def read_own_items(
        current_user: User = Security(get_current_active_user, scopes=["items"]),
    ):
        return [{"item_id": "Foo", "owner": current_user.username}]
    
    
    @app.get("/status/")
    async def read_system_status(current_user: User = Depends(get_current_user)):
        return {"status": "ok"}
    

```

## Проверка `username` и формата данных

Мы проверяем, что получили `username`, и извлекаем scopes.

Затем валидируем эти данные с помощью Pydantic‑модели (перехватывая исключение `ValidationError`), и если возникает ошибка при чтении JWT‑токена или при валидации данных с Pydantic, мы вызываем `HTTPException`, созданное ранее.

Для этого мы обновляем Pydantic‑модель `TokenData`, добавляя новое свойство `scopes`.

Валидируя данные с помощью Pydantic, мы можем удостовериться, что у нас, например, именно `list` из `str` со scopes и `str` с `username`.

А не, скажем, `dict` или что‑то ещё — ведь это могло бы где‑то позже сломать приложение и создать риск для безопасности.

Мы также проверяем, что существует пользователь с таким именем, и если нет — вызываем то же исключение, созданное ранее.

Python 3.10+

```
 
    from datetime import datetime, timedelta, timezone
    from typing import Annotated
    
    import jwt
    from fastapi import Depends, FastAPI, HTTPException, Security, status
    from fastapi.security import (
        OAuth2PasswordBearer,
        OAuth2PasswordRequestForm,
        SecurityScopes,
    )
    from jwt.exceptions import InvalidTokenError
    from pwdlib import PasswordHash
    from pydantic import BaseModel, ValidationError
    
    # to get a string like this run:
    # openssl rand -hex 32
    SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    
    
    fake_users_db = {
        "johndoe": {
            "username": "johndoe",
            "full_name": "John Doe",
            "email": "johndoe@example.com",
            "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$wagCPXjifgvUFBzq4hqe3w$CYaIb8sB+wtD+Vu/P4uod1+Qof8h+1g7bbDlBID48Rc",
            "disabled": False,
        },
        "alice": {
            "username": "alice",
            "full_name": "Alice Chains",
            "email": "alicechains@example.com",
            "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$g2/AV1zwopqUntPKJavBFw$BwpRGDCyUHLvHICnwijyX8ROGoiUPwNKZ7915MeYfCE",
            "disabled": True,
        },
    }
    
    
    class Token(BaseModel):
        access_token: str
        token_type: str
    
    
    class TokenData(BaseModel):
        username: str | None = None
        scopes: list[str] = []
    
    
    class User(BaseModel):
        username: str
        email: str | None = None
        full_name: str | None = None
        disabled: bool | None = None
    
    
    class UserInDB(User):
        hashed_password: str
    
    
    password_hash = PasswordHash.recommended()
    
    DUMMY_HASH = password_hash.hash("dummypassword")
    
    oauth2_scheme = OAuth2PasswordBearer(
        tokenUrl="token",
        scopes={"me": "Read information about the current user.", "items": "Read items."},
    )
    
    app = FastAPI()
    
    
    def verify_password(plain_password, hashed_password):
        return password_hash.verify(plain_password, hashed_password)
    
    
    def get_password_hash(password):
        return password_hash.hash(password)
    
    
    def get_user(db, username: str):
        if username in db:
            user_dict = db[username]
            return UserInDB(**user_dict)
    
    
    def authenticate_user(fake_db, username: str, password: str):
        user = get_user(fake_db, username)
        if not user:
            verify_password(password, DUMMY_HASH)
            return False
        if not verify_password(password, user.hashed_password):
            return False
        return user
    
    
    def create_access_token(data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    
    
    async def get_current_user(
        security_scopes: SecurityScopes, token: Annotated[str, Depends(oauth2_scheme)]
    ):
        if security_scopes.scopes:
            authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
        else:
            authenticate_value = "Bearer"
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": authenticate_value},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username = payload.get("sub")
            if username is None:
                raise credentials_exception
            scope: str = payload.get("scope", "")
            token_scopes = scope.split(" ")
            token_data = TokenData(scopes=token_scopes, username=username)
        except (InvalidTokenError, ValidationError):
            raise credentials_exception
        user = get_user(fake_users_db, username=token_data.username)
        if user is None:
            raise credentials_exception
        for scope in security_scopes.scopes:
            if scope not in token_data.scopes:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Not enough permissions",
                    headers={"WWW-Authenticate": authenticate_value},
                )
        return user
    
    
    async def get_current_active_user(
        current_user: Annotated[User, Security(get_current_user, scopes=["me"])],
    ):
        if current_user.disabled:
            raise HTTPException(status_code=400, detail="Inactive user")
        return current_user
    
    
    @app.post("/token")
    async def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    ) -> Token:
        user = authenticate_user(fake_users_db, form_data.username, form_data.password)
        if not user:
            raise HTTPException(status_code=400, detail="Incorrect username or password")
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username, "scope": " ".join(form_data.scopes)},
            expires_delta=access_token_expires,
        )
        return Token(access_token=access_token, token_type="bearer")
    
    
    @app.get("/users/me/")
    async def read_users_me(
        current_user: Annotated[User, Depends(get_current_active_user)],
    ) -> User:
        return current_user
    
    
    @app.get("/users/me/items/")
    async def read_own_items(
        current_user: Annotated[User, Security(get_current_active_user, scopes=["items"])],
    ):
        return [{"item_id": "Foo", "owner": current_user.username}]
    
    
    @app.get("/status/")
    async def read_system_status(current_user: Annotated[User, Depends(get_current_user)]):
        return {"status": "ok"}
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from datetime import datetime, timedelta, timezone
    
    import jwt
    from fastapi import Depends, FastAPI, HTTPException, Security, status
    from fastapi.security import (
        OAuth2PasswordBearer,
        OAuth2PasswordRequestForm,
        SecurityScopes,
    )
    from jwt.exceptions import InvalidTokenError
    from pwdlib import PasswordHash
    from pydantic import BaseModel, ValidationError
    
    # to get a string like this run:
    # openssl rand -hex 32
    SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    
    
    fake_users_db = {
        "johndoe": {
            "username": "johndoe",
            "full_name": "John Doe",
            "email": "johndoe@example.com",
            "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$wagCPXjifgvUFBzq4hqe3w$CYaIb8sB+wtD+Vu/P4uod1+Qof8h+1g7bbDlBID48Rc",
            "disabled": False,
        },
        "alice": {
            "username": "alice",
            "full_name": "Alice Chains",
            "email": "alicechains@example.com",
            "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$g2/AV1zwopqUntPKJavBFw$BwpRGDCyUHLvHICnwijyX8ROGoiUPwNKZ7915MeYfCE",
            "disabled": True,
        },
    }
    
    
    class Token(BaseModel):
        access_token: str
        token_type: str
    
    
    class TokenData(BaseModel):
        username: str | None = None
        scopes: list[str] = []
    
    
    class User(BaseModel):
        username: str
        email: str | None = None
        full_name: str | None = None
        disabled: bool | None = None
    
    
    class UserInDB(User):
        hashed_password: str
    
    
    password_hash = PasswordHash.recommended()
    
    DUMMY_HASH = password_hash.hash("dummypassword")
    
    oauth2_scheme = OAuth2PasswordBearer(
        tokenUrl="token",
        scopes={"me": "Read information about the current user.", "items": "Read items."},
    )
    
    app = FastAPI()
    
    
    def verify_password(plain_password, hashed_password):
        return password_hash.verify(plain_password, hashed_password)
    
    
    def get_password_hash(password):
        return password_hash.hash(password)
    
    
    def get_user(db, username: str):
        if username in db:
            user_dict = db[username]
            return UserInDB(**user_dict)
    
    
    def authenticate_user(fake_db, username: str, password: str):
        user = get_user(fake_db, username)
        if not user:
            verify_password(password, DUMMY_HASH)
            return False
        if not verify_password(password, user.hashed_password):
            return False
        return user
    
    
    def create_access_token(data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    
    
    async def get_current_user(
        security_scopes: SecurityScopes, token: str = Depends(oauth2_scheme)
    ):
        if security_scopes.scopes:
            authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
        else:
            authenticate_value = "Bearer"
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": authenticate_value},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
            scope: str = payload.get("scope", "")
            token_scopes = scope.split(" ")
            token_data = TokenData(scopes=token_scopes, username=username)
        except (InvalidTokenError, ValidationError):
            raise credentials_exception
        user = get_user(fake_users_db, username=token_data.username)
        if user is None:
            raise credentials_exception
        for scope in security_scopes.scopes:
            if scope not in token_data.scopes:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Not enough permissions",
                    headers={"WWW-Authenticate": authenticate_value},
                )
        return user
    
    
    async def get_current_active_user(
        current_user: User = Security(get_current_user, scopes=["me"]),
    ):
        if current_user.disabled:
            raise HTTPException(status_code=400, detail="Inactive user")
        return current_user
    
    
    @app.post("/token")
    async def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
    ) -> Token:
        user = authenticate_user(fake_users_db, form_data.username, form_data.password)
        if not user:
            raise HTTPException(status_code=400, detail="Incorrect username or password")
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username, "scope": " ".join(form_data.scopes)},
            expires_delta=access_token_expires,
        )
        return Token(access_token=access_token, token_type="bearer")
    
    
    @app.get("/users/me/")
    async def read_users_me(current_user: User = Depends(get_current_active_user)) -> User:
        return current_user
    
    
    @app.get("/users/me/items/")
    async def read_own_items(
        current_user: User = Security(get_current_active_user, scopes=["items"]),
    ):
        return [{"item_id": "Foo", "owner": current_user.username}]
    
    
    @app.get("/status/")
    async def read_system_status(current_user: User = Depends(get_current_user)):
        return {"status": "ok"}
    

```

## Проверка `scopes`

Теперь проверяем, что все требуемые scopes — этой зависимостью и всеми зависящими (включая операции пути) — присутствуют среди scopes, предоставленных в полученном токене, иначе вызываем `HTTPException`.

Для этого используем `security_scopes.scopes`, содержащий `list` со всеми этими scopes как `str`.

Python 3.10+

```
 
    from datetime import datetime, timedelta, timezone
    from typing import Annotated
    
    import jwt
    from fastapi import Depends, FastAPI, HTTPException, Security, status
    from fastapi.security import (
        OAuth2PasswordBearer,
        OAuth2PasswordRequestForm,
        SecurityScopes,
    )
    from jwt.exceptions import InvalidTokenError
    from pwdlib import PasswordHash
    from pydantic import BaseModel, ValidationError
    
    # to get a string like this run:
    # openssl rand -hex 32
    SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    
    
    fake_users_db = {
        "johndoe": {
            "username": "johndoe",
            "full_name": "John Doe",
            "email": "johndoe@example.com",
            "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$wagCPXjifgvUFBzq4hqe3w$CYaIb8sB+wtD+Vu/P4uod1+Qof8h+1g7bbDlBID48Rc",
            "disabled": False,
        },
        "alice": {
            "username": "alice",
            "full_name": "Alice Chains",
            "email": "alicechains@example.com",
            "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$g2/AV1zwopqUntPKJavBFw$BwpRGDCyUHLvHICnwijyX8ROGoiUPwNKZ7915MeYfCE",
            "disabled": True,
        },
    }
    
    
    class Token(BaseModel):
        access_token: str
        token_type: str
    
    
    class TokenData(BaseModel):
        username: str | None = None
        scopes: list[str] = []
    
    
    class User(BaseModel):
        username: str
        email: str | None = None
        full_name: str | None = None
        disabled: bool | None = None
    
    
    class UserInDB(User):
        hashed_password: str
    
    
    password_hash = PasswordHash.recommended()
    
    DUMMY_HASH = password_hash.hash("dummypassword")
    
    oauth2_scheme = OAuth2PasswordBearer(
        tokenUrl="token",
        scopes={"me": "Read information about the current user.", "items": "Read items."},
    )
    
    app = FastAPI()
    
    
    def verify_password(plain_password, hashed_password):
        return password_hash.verify(plain_password, hashed_password)
    
    
    def get_password_hash(password):
        return password_hash.hash(password)
    
    
    def get_user(db, username: str):
        if username in db:
            user_dict = db[username]
            return UserInDB(**user_dict)
    
    
    def authenticate_user(fake_db, username: str, password: str):
        user = get_user(fake_db, username)
        if not user:
            verify_password(password, DUMMY_HASH)
            return False
        if not verify_password(password, user.hashed_password):
            return False
        return user
    
    
    def create_access_token(data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    
    
    async def get_current_user(
        security_scopes: SecurityScopes, token: Annotated[str, Depends(oauth2_scheme)]
    ):
        if security_scopes.scopes:
            authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
        else:
            authenticate_value = "Bearer"
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": authenticate_value},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username = payload.get("sub")
            if username is None:
                raise credentials_exception
            scope: str = payload.get("scope", "")
            token_scopes = scope.split(" ")
            token_data = TokenData(scopes=token_scopes, username=username)
        except (InvalidTokenError, ValidationError):
            raise credentials_exception
        user = get_user(fake_users_db, username=token_data.username)
        if user is None:
            raise credentials_exception
        for scope in security_scopes.scopes:
            if scope not in token_data.scopes:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Not enough permissions",
                    headers={"WWW-Authenticate": authenticate_value},
                )
        return user
    
    
    async def get_current_active_user(
        current_user: Annotated[User, Security(get_current_user, scopes=["me"])],
    ):
        if current_user.disabled:
            raise HTTPException(status_code=400, detail="Inactive user")
        return current_user
    
    
    @app.post("/token")
    async def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    ) -> Token:
        user = authenticate_user(fake_users_db, form_data.username, form_data.password)
        if not user:
            raise HTTPException(status_code=400, detail="Incorrect username or password")
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username, "scope": " ".join(form_data.scopes)},
            expires_delta=access_token_expires,
        )
        return Token(access_token=access_token, token_type="bearer")
    
    
    @app.get("/users/me/")
    async def read_users_me(
        current_user: Annotated[User, Depends(get_current_active_user)],
    ) -> User:
        return current_user
    
    
    @app.get("/users/me/items/")
    async def read_own_items(
        current_user: Annotated[User, Security(get_current_active_user, scopes=["items"])],
    ):
        return [{"item_id": "Foo", "owner": current_user.username}]
    
    
    @app.get("/status/")
    async def read_system_status(current_user: Annotated[User, Depends(get_current_user)]):
        return {"status": "ok"}
    

```

🤓 Other versions and variants

Python 3.10+ - non-Annotated

Tip

Prefer to use the `Annotated` version if possible.

```
 
    from datetime import datetime, timedelta, timezone
    
    import jwt
    from fastapi import Depends, FastAPI, HTTPException, Security, status
    from fastapi.security import (
        OAuth2PasswordBearer,
        OAuth2PasswordRequestForm,
        SecurityScopes,
    )
    from jwt.exceptions import InvalidTokenError
    from pwdlib import PasswordHash
    from pydantic import BaseModel, ValidationError
    
    # to get a string like this run:
    # openssl rand -hex 32
    SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    
    
    fake_users_db = {
        "johndoe": {
            "username": "johndoe",
            "full_name": "John Doe",
            "email": "johndoe@example.com",
            "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$wagCPXjifgvUFBzq4hqe3w$CYaIb8sB+wtD+Vu/P4uod1+Qof8h+1g7bbDlBID48Rc",
            "disabled": False,
        },
        "alice": {
            "username": "alice",
            "full_name": "Alice Chains",
            "email": "alicechains@example.com",
            "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$g2/AV1zwopqUntPKJavBFw$BwpRGDCyUHLvHICnwijyX8ROGoiUPwNKZ7915MeYfCE",
            "disabled": True,
        },
    }
    
    
    class Token(BaseModel):
        access_token: str
        token_type: str
    
    
    class TokenData(BaseModel):
        username: str | None = None
        scopes: list[str] = []
    
    
    class User(BaseModel):
        username: str
        email: str | None = None
        full_name: str | None = None
        disabled: bool | None = None
    
    
    class UserInDB(User):
        hashed_password: str
    
    
    password_hash = PasswordHash.recommended()
    
    DUMMY_HASH = password_hash.hash("dummypassword")
    
    oauth2_scheme = OAuth2PasswordBearer(
        tokenUrl="token",
        scopes={"me": "Read information about the current user.", "items": "Read items."},
    )
    
    app = FastAPI()
    
    
    def verify_password(plain_password, hashed_password):
        return password_hash.verify(plain_password, hashed_password)
    
    
    def get_password_hash(password):
        return password_hash.hash(password)
    
    
    def get_user(db, username: str):
        if username in db:
            user_dict = db[username]
            return UserInDB(**user_dict)
    
    
    def authenticate_user(fake_db, username: str, password: str):
        user = get_user(fake_db, username)
        if not user:
            verify_password(password, DUMMY_HASH)
            return False
        if not verify_password(password, user.hashed_password):
            return False
        return user
    
    
    def create_access_token(data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    
    
    async def get_current_user(
        security_scopes: SecurityScopes, token: str = Depends(oauth2_scheme)
    ):
        if security_scopes.scopes:
            authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
        else:
            authenticate_value = "Bearer"
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": authenticate_value},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
            scope: str = payload.get("scope", "")
            token_scopes = scope.split(" ")
            token_data = TokenData(scopes=token_scopes, username=username)
        except (InvalidTokenError, ValidationError):
            raise credentials_exception
        user = get_user(fake_users_db, username=token_data.username)
        if user is None:
            raise credentials_exception
        for scope in security_scopes.scopes:
            if scope not in token_data.scopes:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Not enough permissions",
                    headers={"WWW-Authenticate": authenticate_value},
                )
        return user
    
    
    async def get_current_active_user(
        current_user: User = Security(get_current_user, scopes=["me"]),
    ):
        if current_user.disabled:
            raise HTTPException(status_code=400, detail="Inactive user")
        return current_user
    
    
    @app.post("/token")
    async def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
    ) -> Token:
        user = authenticate_user(fake_users_db, form_data.username, form_data.password)
        if not user:
            raise HTTPException(status_code=400, detail="Incorrect username or password")
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username, "scope": " ".join(form_data.scopes)},
            expires_delta=access_token_expires,
        )
        return Token(access_token=access_token, token_type="bearer")
    
    
    @app.get("/users/me/")
    async def read_users_me(current_user: User = Depends(get_current_active_user)) -> User:
        return current_user
    
    
    @app.get("/users/me/items/")
    async def read_own_items(
        current_user: User = Security(get_current_active_user, scopes=["items"]),
    ):
        return [{"item_id": "Foo", "owner": current_user.username}]
    
    
    @app.get("/status/")
    async def read_system_status(current_user: User = Depends(get_current_user)):
        return {"status": "ok"}
    

```

## Дерево зависимостей и scopes

Ещё раз рассмотрим дерево зависимостей и scopes.

Так как у зависимости `get_current_active_user` есть подзависимость `get_current_user`, scope `"me"`, объявленный в `get_current_active_user`, будет включён в список требуемых scopes в `security_scopes.scopes`, передаваемый в `get_current_user`.

Сама операция пути тоже объявляет scope — `"items"`, поэтому он также будет в списке `security_scopes.scopes`, передаваемом в `get_current_user`.

Иерархия зависимостей и scopes выглядит так:

  * Операция пути `read_own_items`:
  * Запрашивает scopes `["items"]` с зависимостью:
  * `get_current_active_user`:
    * Функция‑зависимость `get_current_active_user`:
    * Запрашивает scopes `["me"]` с зависимостью:
    * `get_current_user`:
      * Функция‑зависимость `get_current_user`:
      * Собственных scopes не запрашивает.
      * Имеет зависимость, использующую `oauth2_scheme`.
      * Имеет параметр `security_scopes` типа `SecurityScopes`:
        * Этот параметр `security_scopes` имеет свойство `scopes` с `list`, содержащим все объявленные выше scopes, то есть:
        * `security_scopes.scopes` будет содержать `["me", "items"]` для операции пути `read_own_items`.
        * `security_scopes.scopes` будет содержать `["me"]` для операции пути `read_users_me`, потому что он объявлен в зависимости `get_current_active_user`.
        * `security_scopes.scopes` будет содержать `[]` (ничего) для операции пути `read_system_status`, потому что там не объявлялся `Security` со `scopes`, и его зависимость `get_current_user` тоже не объявляет `scopes`.

Совет

Важный и «магический» момент здесь в том, что `get_current_user` будет иметь разный список `scopes` для проверки для каждой операции пути.

Всё это зависит от `scopes`, объявленных в каждой операции пути и в каждой зависимости в дереве зависимостей конкретной операции пути.

## Больше деталей о `SecurityScopes`

Вы можете использовать `SecurityScopes` в любой точке и в нескольких местах — необязательно в «корневой» зависимости.

Он всегда будет содержать security scopes, объявленные в текущих зависимостях `Security`, и всеми зависящими — для этой конкретной операции пути и этого конкретного дерева зависимостей.

Поскольку `SecurityScopes` будет содержать все scopes, объявленные зависящими, вы можете использовать его, чтобы централизованно проверять наличие требуемых scopes в токене в одной функции‑зависимости, а затем объявлять разные требования по scopes в разных операциях пути.

Они будут проверяться независимо для каждой операции пути.

## Проверим это

Откройте документацию API — вы сможете аутентифицироваться и указать, какие scopes вы хотите авторизовать.

![](https://fastapi.tiangolo.com/img/tutorial/security/image11.png)

Если вы не выберете ни один scope, вы будете «аутентифицированы», но при попытке доступа к `/users/me/` или `/users/me/items/` получите ошибку о недостаточных разрешениях. При этом доступ к `/status/` будет возможен.

Если вы выберете scope `me`, но не `items`, вы сможете получить доступ к `/users/me/`, но не к `/users/me/items/`.

Так и будет происходить со сторонним приложением, которое попытается обратиться к одной из этих операций пути с токеном, предоставленным пользователем, — в зависимости от того, сколько разрешений пользователь дал приложению.

## О сторонних интеграциях

В этом примере мы используем OAuth2 «password flow» (аутентификация по паролю).

Это уместно, когда мы входим в наше собственное приложение, вероятно, с нашим собственным фронтендом.

Мы можем ему доверять при получении `username` и `password`, потому что он под нашим контролем.

Но если вы создаёте OAuth2‑приложение, к которому будут подключаться другие (т.е. вы строите провайдера аутентификации наподобие Facebook, Google, GitHub и т.п.), вам следует использовать один из других «flows».

Самый распространённый — «implicit flow».

Самый безопасный — «code flow», но он сложнее в реализации, так как требует больше шагов. Из‑за сложности многие провайдеры в итоге рекомендуют «implicit flow».

Примечание

Часто каждый провайдер аутентификации называет свои «flows» по‑разному — как часть бренда.

Но в итоге они реализуют один и тот же стандарт OAuth2.

**FastAPI** включает утилиты для всех этих OAuth2‑flows в `fastapi.security.oauth2`.

## `Security` в параметре `dependencies` декоратора

Точно так же, как вы можете определить `list` из `Depends` в параметре `dependencies` декоратора (см. [Зависимости в декораторах операции пути](https://fastapi.tiangolo.com/ru/tutorial/dependencies/dependencies-in-path-operation-decorators/) ([local](./../../06_учебник-руководство-пользователя/29_зависимости/03_зависимости-в-декораторах-операции-пути.md))), вы можете использовать там и `Security` со `scopes`.
