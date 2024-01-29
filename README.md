# 项目架构说明

## 项目结构

```
├── backend
│   ├── application
│   │   ├── controllers # 控制器(路由)
│   │   ├── models # 数据模型
│   │   ├── service # 业务逻辑
│   │   ├── static # 静态文件
│   │   ├── utils # 工具类
│   │   ├── config.py # 配置文件
│   │   ├── app.py # 应用创建函数
│   │   └── extensions.py # 扩展
│   ├── manage.py # 启动脚本
│   └── requirements.txt # 依赖
├── frontend
```

## Todo

- [ ] 可视化魔改

## 后端启动说明
需安装python >= 3.9
1. 安装依赖

```bass
pip install -r requirements.txt
```

## 前端启动说明
需安装node.js >= 20.0.0  
每次拉取后建议都使用`npm install`更新依赖
1. 安装依赖

```bass
cd frontend
npm install
```

2. 启动

```bass
npm run dev
```
