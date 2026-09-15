# ipd-test-repo

IPD研发项目管理系统 V0.1。

## V0.1
- Vue 3 + TypeScript + Element Plus 前端骨架
- 登录页、研发项目驾驶舱、项目列表
- IPD 六阶段：概念、计划、开发、验证、发布、生命周期
- FastAPI 后端及项目 API
- PostgreSQL 项目/阶段基础表
- Docker Compose 本地数据库与后端启动配置

## 目录
- frontend/ 前端
- backend/ 后端
- database/ 数据库
- docs/ 架构与 IPD 流程文档

## 启动
后端与数据库：

    docker compose up

前端：

    cd frontend
    npm install
    npm run dev

API 健康检查：GET /health
