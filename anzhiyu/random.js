var posts=["article/hello-world/","article/测试文档/","article/Zotero-1/","article/LaTeX-1/","article/LaTeX-2/","article/Hexo-0/","article/Hexo-2/","article/Hexo-3/","article/Hexo-4/","article/LaTeX-3/","article/Tools-1/","article/Hexo-1/"];function toRandomPost(){
    pjax.loadUrl('/'+posts[Math.floor(Math.random() * posts.length)]);
  };