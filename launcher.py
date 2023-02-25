# -*- coding:UTF-8 -*-
try:
    import tkinter as tk
    from tkinter import messagebox
    from script import run_game
    import pickle
except ImportError:  # 检测库/文件是否成功调用, 否则显示提示信息
    print('''请确认文件是否缺少! 
请确认Tcl/TK是否在你的电脑上安装! ''')
else:

    def run_game():
        '''运行游戏'''
        global width, height
        # 获取游戏窗口大小
        try:
            if width.get() != '':
                width = int(width.get())  # 获取宽度
            else:
                width = 1200
            if height.get() != '':
                height = int(height.get())  # 获取高度
            else:
                height = 800
        except:
            messagebox.showwarning(title='错误! ', message='请输入正确的数据! ')
        else:
            if width >= 900 and height >= 750 and width < 2000 and height < 2000:  # 是否合理
                window.destroy()
                run_game(difficulty_int, width, height)  # 运行游戏
            else:
                messagebox.showwarning(title='错误! ',
                                        message='请输入合理的窗口大小! ')

    def change_difficulty(difficulty):
        '''切换难度'''
        global difficulty_int
        difficulty_var.set(difficulty_dict[int(difficulty)])
        difficulty_int = int(difficulty)

    # 窗口
    window = tk.Tk()
    window.title('外星人大战启动器')
    window.geometry('600x400')
    '''难度'''
    # 难度变量
    difficulty_dict = {1: '难度: 简单', 2: '难度: 普通', 3: '难度: 困难'}
    difficulty_var = tk.StringVar()
    difficulty_int = 1
    difficulty_var.set('难度: 简单')
    # 难度显示
    difficulty_label = tk.Label(window,
                                width=15,
                                height=2,
                                textvariable=difficulty_var,
                                font=('Minecraft AE Pixel', 22))
    difficulty_label.place(x=150, y=25, anchor='n')
    # 难度选择
    difficulty_scale = tk.Scale(window,
                                from_=1,
                                to=3,
                                orient=tk.HORIZONTAL,
                                length=200,
                                width=25,
                                showvalue=False,
                                tickinterval=None,
                                resolution=1,
                                font=('Minecraft AE Pixel', 22),
                                command=change_difficulty)
    difficulty_scale.place(x=38, y=100, anchor='nw')
    '''游戏窗口大小'''
    width = tk.StringVar()
    width.set('1200')
    height = tk.StringVar()
    height.set('800')
    # 游戏窗口选择
    tk.Label(window,
                width=14,
                height=2,
                text='游戏窗口大小',
                font=('Minecraft AE Pixel', 20)).place(x=432,
                                                    y=25,
                                                    anchor='n')
    width_entry = tk.Entry(window,
                            width=4,
                            show=None,
                            textvariable=width,
                            font=('Minecraft AE Pixel', 22))
    width_entry.place(x=430, y=115, anchor='e')
    height_entry = tk.Entry(window,
                            width=4,
                            show=None,
                            textvariable=height,
                            font=('Minecraft AE Pixel', 22))
    height_entry.place(x=435, y=115, anchor='w')
    '''按钮'''
    # 开始游戏按钮
    start_button = tk.Button(window,
                                text='开始游戏 !',
                                width=20,
                                height=2,
                                font=('Minecraft AE Pixel', 22),
                                command=run_game)
    start_button.place(x=300, y=350, anchor='s')
    # 主循环
    window.mainloop()
