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
  - [x] 内容删除
  - [ ] 内容修改
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
| `.login_get` | `GET` | `/login` | 用户登录 |
|`.login_post`| `POST`|`/login` | 用户登录 |
| `.register_get`| `GET` | `/register`| 用户注册 |
| `.register_post`|`POST`| `/register`| 用户注册 |
| `post.all_posts`| `GET`| `/post/all` | 展示所有短文本 |
| `post.show_post` | `GET`| `/post/<post_id>` | 展示单个短文本及评论 |
|`post.review_post`|`POST` |`/post/<post_id>`|短文本下添加评论|
|`post.delete_post`|`GET` | `/post/<post_id>/del`| 删除短文本 |
| `post.new` | `GET`,`POST` | `/post/new` | 发布短文本（URL和方法待移至post蓝图）|
| `article.all_articles ` | `GET` | `/article/all` | 展示所有短文本 |
| `article.new` |`GET`,`POST`| `/article/new` | 发布长文本（文章）|
| `article.show_article` | `GET`| `/article/<article_id>` | 展示单个长文本及评论 |
|`article.review_article`|`POST`|  `/article/<article_id>` | 长文本下添加评论 |
|`article.delete_article`|`GET` | `/article/<article_id>/del`| 删除长文本 |
| `user.profile` | `GET`,`POST` | `/user/profile` | 个人资料管理 |
| `user.logout` | `GET` | `/user/logout` | 用户登出 |




 

## 待解决问题

1. 文章展示页期望只显示文章内容首行并以省略号结尾，css相关属性 `text-overflow:ellipsis`等可实现只显示首行，但是文本行高不足无法显示100%且没有省略号显示。
2. 数据库隔离（已解决：配置pg数据库）
3. 代码规范与结构改进(文件结构与代码规范均已优化)

