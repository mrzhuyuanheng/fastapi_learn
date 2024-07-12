要验证这段代码，可以通过几种方法来上传文件，并查看响应。你可以使用工具如 Postman 或编写 Python 脚本来进行验证。

1. **运行 FastAPI 服务器**：
   首先，将 FastAPI 代码保存到一个文件中，例如 `main.py`。然后在命令行中运行该文件：

   ```sh
   uvicorn main:app --reload
   ```

2. **使用 Postman 验证**：
   - 对于 `/files/` 端点：
     1. 创建一个 POST 请求，URL 设置为 `http://127.0.0.1:8000/files/`。
     2. 在 Body 中选择 `form-data`，并添加一个键名为 `file` 的字段，类型选择 `File`，上传一个文件。

   - 对于 `/uploadfile/` 端点：
     1. 创建一个 POST 请求，URL 设置为 `http://127.0.0.1:8000/uploadfile/`。
     2. 在 Body 中选择 `form-data`，并添加一个键名为 `file` 的字段，类型选择 `File`，上传一个文件。

3. **使用 Python requests 库验证**：
   你也可以编写一个简单的 Python 脚本来验证上传文件的功能：

   ```python
   import requests

   url_files = "http://127.0.0.1:8000/files/"
   url_uploadfile = "http://127.0.0.1:8000/uploadfile/"

   file_path = "path/to/your/file.txt"

   # 对于 /files/ 端点
   with open(file_path, "rb") as file:
       response = requests.post(url_files, files={"file": file})
       print(response.json())

   # 对于 /uploadfile/ 端点
   with open(file_path, "rb") as file:
       response = requests.post(url_uploadfile, files={"file": file})
       print(response.json())
   ```

以下是完整的 FastAPI 代码和验证脚本：

```python
# main.py
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/files/")
async def create_file(file: bytes = File()):
    return {"file_size": len(file)}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}
```

```python
# test.py
import requests

url_files = "http://127.0.0.1:8000/files/"
url_uploadfile = "http://127.0.0.1:8000/uploadfile/"

file_path = "path/to/your/file.txt"

# 对于 /files/ 端点
with open(file_path, "rb") as file:
    response = requests.post(url_files, files={"file": file})
    print(response.json())

# 对于 /uploadfile/ 端点
with open(file_path, "rb") as file:
    response = requests.post(url_uploadfile, files={"file": file})
    print(response.json())
```

运行 FastAPI 服务器和 Python 脚本后，你应该会在控制台中看到返回的 JSON 数据，表示验证成功。

如果你遇到任何问题，请分享错误信息或遇到的具体问题，我会进一步帮助你解决。