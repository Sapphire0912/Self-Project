import tkinter as tk
import alg_nAnB as Alg

com_num = Alg.gen_func()
games = Alg.Handle(com_num)


def btw_guess():
    # 遊戲流程
    player_num = _input.get()
    games.guess(player_num)
    _output.set(games.result)

    # 新增猜過紀錄
    his_text.config(state='normal')
    his_text.insert("insert", player_num)
    his_text.insert("insert", " -> " + games.result)
    his_text.insert("insert", '\n')
    his_text.config(state='disable')

    # 遊戲未結束時，猜過一次後就把輸入欄清除
    if games.stop:
        _input.set("")


# 視窗架構
win = tk.Tk()
win.geometry("320x320")
win.title("MynAnB")

# 玩家輸入數字
ft = ("標楷體", 12, "bold")
input_num = tk.Label(win, text='輸入要猜的數字: ', font=ft)
input_num.grid(row=0, column=0, sticky='e')
_input = tk.StringVar()
entry_input = tk.Entry(win, textvariable=_input, font=ft, width=10)
entry_input.grid(row=0, column=1, sticky='w')

# 電腦輸出結果
output_AB = tk.Label(win, text='結果: ', font=ft)
output_AB.grid(row=1, column=0, sticky='e')
_output = tk.StringVar()
entry_AB = tk.Entry(win, textvariable=_output, font=ft, width=10, state='readonly')
entry_AB.grid(row=1, column=1, sticky='w')

# 猜過的紀錄
his_label = tk.Label(win, text="猜過的數字: ", font=ft)
his_label.grid(row=2, column=0, sticky='w')
his_text = tk.Text(win, height=10, width=15, state='disable', font=ft)
his_text.grid(row=3, column=0)

# 猜 按鈕
button_guess = tk.Button(win, text="猜", font=ft, command=btw_guess)
button_guess.grid(row=2, column=1, ipadx=10, ipady=5)

win.mainloop()
