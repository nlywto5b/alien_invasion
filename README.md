# alien_invasion

## 外星人大战

### 简介

这是一个用python写的小游戏——外星人大战，参考了《Python学习 从入门到实践》中的部分代码（包括游戏主体等），并进行了扩展（包括历史最高分、自动备份等），玩家控制飞船发射子弹和移动来攻击外星人，使它们全部死亡

开发语言：python

框架：pygame

启动器GUI框架：tkinter

~尽管python不适合用来做游戏~

### 操作

WASD控制方向

P开始游戏

ESC退出

运行前需要先使用install_module.bat来安装pygame

运行launcher/scripts.py来运行启动器

### 关于DIY

本游戏可以DIY，只要你替换掉对应文件即可

  - images/ship.bmp - 飞船图片
  
  - images/alien.bmp - 外星人图片
  
  - images/welcome.gif - 启动器的欢迎图片(虽然是gif文件，但由于tkinter的问题，无法动起来)
  
  字体类型与大小在settings.py中设置，**此项不建议更改**， 将来可能会在启动器页面自带设置([#5](https://github.com/nlywto5b/alien_invasion/issues/5))。用文本文档打开setting.py,
在第51，62，65，68行
```python
self.button_font = pygame.font.SysFont('Kaiti', 45)
self.scorebaord_font = pygame.font.SysFont('Kaiti', 30)
self.fps_font = pygame.font.SysFont('Kaiti', 30)
self.timer_font = pygame.font.SysFont('Kaiti', 30)
```
  
  四行分别对应开始游戏按钮、计分板、帧数、计时器。`'Kaiti'` 代表楷体，可以替换为字体文件的地址，`45` 代表字体大小。
  
    
  

在DIY前，**记得备份**，以免删除重要文件！

### 其他
任何人都可以随意下载此仓库中的文件，也可以发给其他人，**但必须注明出处，不能从事商业行为**


由于开发者是一个中学生，所以只有周末能处理issue和更新，所以更新速度缓慢，敬请谅解！
