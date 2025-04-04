var posts=["article/2025-4-4-第一篇文章/","article/hello-world/","article/2025-4-4-第一篇测试文档/"];function toRandomPost(){
    pjax.loadUrl('/'+posts[Math.floor(Math.random() * posts.length)]);
  };