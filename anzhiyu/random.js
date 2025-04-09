var posts=["article/hello-world/","article/测试文档/","article/第一章-Latex与Vscode的相遇/","article/第二篇-博文写作语法/","article/第一篇-hexo-anzhiyu-配置心得/"];function toRandomPost(){
    pjax.loadUrl('/'+posts[Math.floor(Math.random() * posts.length)]);
  };