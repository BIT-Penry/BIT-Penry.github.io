var posts=["article/hello-world/","article/测试文档/","article/第一章-Latex与Vscode的相遇/","article/第一篇-hexo-anzhiyu-配置心得/","article/第三章-biber-VS-bibtex/","article/第二章-Vscode-PK-Overleaf/","article/第三篇-Twikoo评论邮件回复魔改/","article/第二篇-博文写作语法/","article/第四章-Hexo-GitHub-Pages-从零配置自动部署（SSH-版）/"];function toRandomPost(){
    pjax.loadUrl('/'+posts[Math.floor(Math.random() * posts.length)]);
  };