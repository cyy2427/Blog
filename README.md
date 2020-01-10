# helloflask

本项目实现了一个简易的web博客应用，实现功能包括：

- [ ] 用户管理 
  - [x] 用户注册
  - [x] 用户登录与登出
  - [ ] 用户个人中心
    - [x] 头像上传和显示
    - [ ] 个人资料设置

- [ ] 内容管理
  - [x] 文章发布（含标题、集成CKEditor富文本编辑）
  - [x] 文章展示
  - [ ] 文章修改和删除
  - [x] 短文本发布
  - [x] 短文本展示（详情+列表）

- [ ] 内容互动与反馈
  - [x] 评论发布与展示（列表）
  - [ ] 评论删除
  - [ ] 点赞

## 部署
使用docker-compose部署
```sh
>  docker-compose up build -d --build
```

## 路由

| 端点 | 方法 | URL | 描述 |
| ---- | --- | --- | --- |
| `.login` | `GET`,`POST` | `/login` | 用户登录 |
| `.register`| `GET`,`POST` | `/logout`| 用户注册 |
| `post.all_posts`| `GET`| `/post/all` | 展示所有短文本 |
| `post.show_post` | `GET`,`POST` | `/post/<post_id>` | 展示单个短文本及评论 |
| `user.newpost` | `GET`,`POST` | `/user/newpost` | 发布短文本（URL和方法待移至post蓝图）|
| `article.all_articles ` | `GET` | `/article/all` | 展示所有短文本 |
| `article.write_article` |`GET`,`POST`| `/article/new` | 发布长文本（文章）|
| `article.show_article` | `GET`,`POST`| `/article/<article_id>` | 展示单个长文本及评论 |
| `user.profile` | `GET`,`POST` | `/user/profile` | 个人资料管理 |
| `user.logout` | `GET` | `/user/logout` | 用户登出 |




 

## 待解决问题

1. 文章展示页期望只显示文章内容首行并以省略号结尾，css相关属性 `text-overflow:ellipsis`等可实现只显示首行，但是文本行高不足无法显示100%且没有省略号显示。
2. 数据库隔离
3. 代码规范与结构改进(PEP8, 工厂函数等)

