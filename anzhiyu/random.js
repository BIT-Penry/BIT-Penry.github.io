var posts=["article/hello-world/","article/hexo-anzhiyu-配置心得/","article/测试文档/"];function toRandomPost(){
    pjax.loadUrl('/'+posts[Math.floor(Math.random() * posts.length)]);
  };