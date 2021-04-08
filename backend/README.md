# g12_Backend

## Project setup
```
控制台进入虚拟环境
cd virtualenv
cd Scripts
activate
cd..
cd..
(当前目录backend)
下载依赖
(venv) $ pip install -r requirements.txt

```

### Compiles and hot-reloads for development server
```
运行后端
控制台输入(venv)flask run,启动后台
```
### Api API文件
```
进入路径:
backend/src/blueprints/
```

### 数据集和数据库文件
```
进入路径:
dataset\
运行脚本 csv2sql.py
python csv2sqlite CsvFile.csv DATABASE.db TABLENAME(表名)
会在数据库中插入以TABLENAME命名的表

```

###读取数据
