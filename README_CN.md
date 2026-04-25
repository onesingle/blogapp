# BlogApp

一个简单的基于Flask的博客应用程序，具有用户认证和待办事项管理功能。

## 功能

- 用户登录和登出
- 创建、查看、编辑和删除待办事项
- 使用SQLite进行数据库管理
- CSRF保护
- 使用Bootstrap的响应式UI

## 要求

- Python 3.6+
- Flask
- Flask-SQLAlchemy

## 安装

1. 克隆仓库：
   ```bash
   git clone https://github.com/onesingle/blogapp.git
   cd blogapp
   ```

2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

3. 运行应用程序：
   ```bash
   python3 blogapp.py
   ```

4. 打开浏览器访问 `http://127.0.0.1:5000`

## 配置

编辑 `config.cfg` 来更改设置：

- `SQLALCHEMY_DATABASE_URI`：数据库URI（默认：SQLite）
- `SECRET_KEY`：会话密钥
- `DEBUG`：调试模式（生产环境中设为False）

## 使用

- **登录**：使用用户名 `admin` 和密码 `blog`
- **首页**：查看所有待办事项
- **新建待办**：创建新待办事项
- **查看/编辑**：点击待办ID查看或编辑
- **删除**：在查看页面使用删除按钮

## 项目结构

- `blogapp.py`：主应用程序文件
- `view.py`：路由处理器
- `data.py`：数据库模型（目前为空，模型已移至blogapp.py）
- `config.cfg`：配置文件
- `templates/`：HTML模板
- `static/`：CSS和JS文件
- `requirements.txt`：Python依赖

## 许可证

本项目为开源项目。