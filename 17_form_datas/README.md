# 怎么验证main.py

要验证下面的 FastAPI 代码，你可以通过使用 Postman 或编写 Python 脚本来发送 POST 请求。以下是详细的验证步骤：

1. **运行 FastAPI 服务器**：
   首先，将 FastAPI 代码保存到一个文件中，例如 `main.py`。然后在命令行中运行该文件：

   ```sh
   uvicorn main:app --reload
   ```

2. **使用 Postman 验证**：
   1. 打开 Postman，创建一个新的 POST 请求。
   2. 设置请求的 URL 为 `http://127.0.0.1:8000/login/`。
   3. 在 Body 选项卡中选择 `x-www-form-urlencoded`。
   4. 添加两个键值对：`username` 和 `password`，并填写相应的值。
   5. 发送请求，查看响应中是否返回了 `username`。

   示例：
   ```plaintext
   POST http://127.0.0.1:8000/login/
   Body:
   username: your_username
   password: your_password
   ```

3. **使用 Python requests 库验证**：
   你也可以编写一个简单的 Python 脚本来验证 POST 请求：

   ```python
   import requests

   url = "http://127.0.0.1:8000/login/"
   payload = {
       "username": "your_username",
       "password": "your_password"
   }

   response = requests.post(url, data=payload)
   print(response.json())
   ```

以下是完整的 FastAPI 代码和验证脚本：

```python
# main.py
from fastapi import FastAPI, Form

app = FastAPI()

@app.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username": username}
```

```python
# test.py
import requests

url = "http://127.0.0.1:8000/login/"
payload = {
    "username": "your_username",
    "password": "your_password"
}

response = requests.post(url, data=payload)
print(response.json())
```

运行 FastAPI 服务器和 Python 脚本后，你应该会在控制台中看到返回的 JSON 数据，表示验证成功。以下是可能的响应：

```json
{
    "username": "your_username"
}
```

### 解释

这个 FastAPI 应用定义了一个 POST 端点 `/login/`，它接受两个表单字段 `username` 和 `password`。验证时，我们发送一个包含这两个字段的表单数据，服务器将返回一个包含用户名的 JSON 响应。这验证了表单数据是否被正确接收和处理。



# 为什么body要选择`x-www-form-urlencoded`

选择 `x-www-form-urlencoded` 是因为 FastAPI 的 `Form` 参数类型是专门用来处理这种类型的表单数据。以下是详细的解释：

### 什么是 `x-www-form-urlencoded`？

`x-www-form-urlencoded` 是一种编码方式，它将表单数据编码为 URL 编码格式。这种格式将表单字段和值转换为 key-value 键值对，并使用 `&` 连接每个字段。在 HTTP 请求中，这种编码方式用于发送简单的表单数据。

### FastAPI `Form` 的作用

在 FastAPI 中，`Form` 是用来处理表单数据的。以下是相关代码：

```python
from fastapi import FastAPI, Form

app = FastAPI()

@app.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username": username}
```

当你使用 `Form` 作为参数时，FastAPI 会期望接收的请求内容类型为 `application/x-www-form-urlencoded` 或 `multipart/form-data`。这两种类型是浏览器在提交表单时最常用的编码方式。

### 如何在 Postman 中选择 `x-www-form-urlencoded`

1. 打开 Postman，创建一个新的 POST 请求。
2. 设置请求的 URL 为 `http://127.0.0.1:8000/login/`。
3. 在 Body 选项卡中选择 `x-www-form-urlencoded`。
4. 添加两个键值对：`username` 和 `password`，并填写相应的值。
5. 发送请求，查看响应中是否返回了 `username`。

示例：

- URL: `http://127.0.0.1:8000/login/`
- Method: POST
- Headers:
  - Content-Type: application/x-www-form-urlencoded
- Body:
  ```plaintext
  username=your_username&password=your_password
  ```

这样，FastAPI 就能正确解析表单数据并返回你期望的结果。

### Python requests 示例

使用 `requests` 库时，默认情况下，数据会以 `application/x-www-form-urlencoded` 编码方式发送：

```python
import requests

url = "http://127.0.0.1:8000/login/"
payload = {
    "username": "your_username",
    "password": "your_password"
}

response = requests.post(url, data=payload)
print(response.json())
```

这个脚本会发送一个 `application/x-www-form-urlencoded` 编码的 POST 请求，FastAPI 能够正确处理并返回响应。

### 总结

选择 `x-www-form-urlencoded` 是因为这种编码方式是浏览器表单的默认提交方式，并且与 FastAPI 的 `Form` 参数类型兼容。这确保了表单数据能够被正确解析并处理。