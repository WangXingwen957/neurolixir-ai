<div style="position: relative; width:150px; height: 150px;">
    <img src="Icon/icon_run.gif"
         style="position: absolute; top: 0px; left: 0px; width: 150px; height: 150px;"
         alt="neurolixir">
</div>

## 简介
#### 一个Python的AI代码库，能用少量的代码和简洁的语言实现丰富的AI效果

## 快速开始
### 1.安装
#### 在 ```Powershell``` / ```Cmd``` / ```Wt``` 中输入
```bash
pip install neurolixir
```
### 2.基础使用示例
```python
>>> import neurolixir as nr
>>> # 这里的output参数是是否输出的布尔值
>>> # 这里speak参数是是否说出答案的布尔值
>>> print(nr.chat('Hello', output=False, speak=True))
Hi
>>> nr.chat('Good morning', output=True, speak=True)
Good morning
>>> # 也可以用begin和end参数来设置输出的开头和结尾
>>> nr.chat('Hello', output=True, begin='neurolixir >>> ', end='!!')
neurolixir >>> Hi!!
>>> # 你可以用nr.__version__来检查你的neurolixir版本
>>> neurolixir.__version__
'1.0.0'
>>> # 也能用nr.start_chat()直接开始聊天
>>> nr.start_chat()
Start chatting! Type "exit" or "quit" to leave.
You: Hello!
Neurolixir: Hi
You: What's your name?
Neurolixir: I'm Lisa
You: exit
Neurolixir: Chat ended by user.
>>> # 而且，neurolixir也能用来计算时间
>>> # 比如计算一年有几秒，就可以
>>> year = nr.TimeCalculator.Year(1)
>>> print(year.second)
31104000
>>> # 也能等待这个特定时间
>>> year.wait()
>>> # 等待1年...
>>> 
>>> # 当然，还有更多的功能，等你来探索！
```

## 主文件

```file
neurolixir           # 外层目录
|- Icon              # 图标文件夹
|- |- icon_run.gif   # 动态图标(参考最上面图标)
|- |- icon.png       # 静态图标
|- __init__.py       # 初始化
|- api.py            # api请求
|- ctime.py          # 时间计算
|- neurolixir.py     # 主代码
|- gpt.txt           # AI训练文件
|- README.md         # 自述文件
```

## 环境要求
#### -```Python``` >= 3.8, ```opanai``` >= 1.107.0, ```pyttsx3``` >= 2.99
#### -系统: ```Windows```

## 许可证
#### 本项目基于MIT许可证开源, 详见```LICENSE```

## 作者
#### -GitHub: ```WangXingwen957```
#### -备注: 欢迎Star和Fork!