import tkinter as tk
from tkinter import Canvas, messagebox
import math

class Main:
    def __init__(self):
        self.x = 0
        self.y = 0

        self.window = tk.Tk()
        self.window.title("投射シミュレーション設定")
        self.window.config(bg="#87cefa")
        self.window.geometry("800x750+0+0")
        self.window.protocol("WM_DELETE_WINDOW", self.close_windows)
        self.setup_ui()

        self.simulator = tk.Toplevel(self.window)
        self.simulator.title("投射シミュレーション")
        self.simulator.geometry("640x480+800+0")
        self.simulator.protocol("WM_DELETE_WINDOW", self.close_windows)

        self.cv = Canvas(self.simulator)
        self.cv.pack(fill=tk.BOTH, expand=True)

        self.current_x = None
        self.current_y = None
        self.circle = None  # 現在の円のID
        self.temp_circle = None  # 半透明の円のID
        self.arrow = None  # 赤い矢印のID
        self.temp_arrow = None  # 半透明の矢印のID
        self.simulating = False

        self.apply_settings()  # プログラム開始時に赤い円を表示

    def setup_ui(self):
        TITLE_FONT = ("Helvetica", 28, "bold")
        LABEL_FONT = ("Helvetica", 14)
        BUTTON_FONT = ("Helvetica", 14, "bold")
        MAIN_COLOR = "#4169e1"
        SECONDARY_COLOR = "#7fffd4"
        ACCENT_COLOR = "#ff7f50"

        self.title_label = tk.Label(text="投射シミュレーション", fg=MAIN_COLOR, bg="#87cefa", font=TITLE_FONT)
        self.title_label.pack()

        self.form_frame = tk.Frame(self.window, bg="#87cefa")
        self.form_frame.pack(pady=10, padx=30)

        # 初速度 v_0
        self.v0_label = tk.Label(self.form_frame, text="初速度 v_0:", font=LABEL_FONT, bg="#87cefa")
        self.v0_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.v0_entry = tk.Entry(self.form_frame, font=LABEL_FONT)
        self.v0_entry.grid(row=0, column=1, padx=10, pady=5)
        self.v0_entry.insert(0, "0")  # 初期値
        self.v0_entry.bind("<KeyRelease>", self.on_value_change)

        # 投射角度 θ
        self.angle_label = tk.Label(self.form_frame, text="投射角度 θ (0<=θ<360):", font=LABEL_FONT, bg="#87cefa")
        self.angle_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.angle_entry = tk.Entry(self.form_frame, font=LABEL_FONT)
        self.angle_entry.grid(row=1, column=1, padx=10, pady=5)
        self.angle_entry.insert(0, "0")  # 初期値
        self.angle_entry.bind("<KeyRelease>", self.on_value_change)

        # 反発係数 e
        self.e_label = tk.Label(self.form_frame, text="反発係数 e (0<=e<1):", font=LABEL_FONT, bg="#87cefa")
        self.e_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.e_entry = tk.Entry(self.form_frame, font=LABEL_FONT)
        self.e_entry.grid(row=2, column=1, padx=10, pady=5)
        self.e_entry.insert(0, "0")  # 初期値
        self.e_entry.bind("<KeyRelease>", self.on_value_change)

        # 重力加速度 g
        self.g_label = tk.Label(self.form_frame, text="重力加速度 g:", font=LABEL_FONT, bg="#87cefa")
        self.g_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.g_entry = tk.Entry(self.form_frame, font=LABEL_FONT)
        self.g_entry.grid(row=3, column=1, padx=10, pady=5)
        self.g_entry.insert(0, "9.81")  # 初期値
        self.g_entry.bind("<KeyRelease>", self.on_value_change)

        # 質量 m(kg)
        self.m_label = tk.Label(self.form_frame, text="質量 m(kg):", font=LABEL_FONT, bg="#87cefa")
        self.m_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.m_entry = tk.Entry(self.form_frame, font=LABEL_FONT)
        self.m_entry.grid(row=4, column=1, padx=10, pady=5)
        self.m_entry.insert(0, "1")  # 初期値
        self.m_entry.bind("<KeyRelease>", self.on_value_change)

        # 動摩擦係数 μ'
        self.μ_label = tk.Label(self.form_frame, text="動摩擦係数 μ':", font=LABEL_FONT, bg="#87cefa")
        self.μ_label.grid(row=5, column=0, padx=10, pady=5, sticky="e")
        self.μ_entry = tk.Entry(self.form_frame, font=LABEL_FONT)
        self.μ_entry.grid(row=5, column=1, padx=10, pady=5)
        self.μ_entry.insert(0, "0")  # 初期値
        self.μ_entry.bind("<KeyRelease>", self.on_value_change)

        # 初期 x 座標 (x_0)
        self.x0_label = tk.Label(self.form_frame, text="初期 x 座標 x_0:", font=LABEL_FONT, bg="#87cefa")
        self.x0_label.grid(row=6, column=0, padx=10, pady=5, sticky="e")
        self.x0_entry = tk.Entry(self.form_frame, font=LABEL_FONT)
        self.x0_entry.grid(row=6, column=1, padx=10, pady=5)
        self.x0_entry.insert(0, "15")  # 初期値
        self.x0_entry.bind("<KeyRelease>", self.on_value_change)

        # 初期 y 座標 (y_0)
        self.y0_label = tk.Label(self.form_frame, text="初期 y 座標 y_0:", font=LABEL_FONT, bg="#87cefa")
        self.y0_label.grid(row=7, column=0, padx=10, pady=5, sticky="e")
        self.y0_entry = tk.Entry(self.form_frame, font=LABEL_FONT)
        self.y0_entry.grid(row=7, column=1, padx=10, pady=5)
        self.y0_entry.insert(0, "15")  # 初期値
        self.y0_entry.bind("<KeyRelease>", self.on_value_change)

        # シミュレータ幅
        self.width_label = tk.Label(self.form_frame, text="シミュレータ幅(10pixelで1m):", font=LABEL_FONT, bg="#87cefa")
        self.width_label.grid(row=8, column=0, padx=10, pady=5, sticky="e")
        self.width_entry = tk.Entry(self.form_frame, font=LABEL_FONT)
        self.width_entry.grid(row=8, column=1, padx=10, pady=5)
        self.width_entry.insert(0, "640")  # 初期値
        self.width_entry.bind("<KeyRelease>", self.on_value_change)

        # シミュレータ高さ
        self.height_label = tk.Label(self.form_frame, text="シミュレータ高さ(10pixelで1m):", font=LABEL_FONT, bg="#87cefa")
        self.height_label.grid(row=9, column=0, padx=10, pady=5, sticky="e")
        self.height_entry = tk.Entry(self.form_frame, font=LABEL_FONT)
        self.height_entry.grid(row=9, column=1, padx=10, pady=5)
        self.height_entry.insert(0, "480")  # 初期値
        self.height_entry.bind("<KeyRelease>", self.on_value_change)

        self.button_frame = tk.Frame(self.window, bg="#87cefa")
        self.button_frame.pack()

        self.apply_button = tk.Button(self.button_frame, text="決定", padx=50, pady=10, font=BUTTON_FONT, bg=SECONDARY_COLOR, width=10, command=self.apply_settings, state=tk.DISABLED)
        self.apply_button.pack(side=tk.TOP, padx=5, pady=30)

        self.start_button = tk.Button(self.button_frame, text="シミュレーション開始", padx=50, pady=10, font=BUTTON_FONT, bg=SECONDARY_COLOR, width=10, command=self.simulation, state=tk.NORMAL)
        self.start_button.pack(side=tk.LEFT, padx=5)

        self.stop_button = tk.Button(self.button_frame, text="戻す", padx=50, pady=10, font=BUTTON_FONT, bg=ACCENT_COLOR, width=10, command=self.stop_simulation ,state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=5)

    def on_value_change(self, event=None):
        if self.simulating:
            return
        # フォームの値が変更されたときに「決定」ボタンを有効化
        self.apply_button.config(state=tk.NORMAL)
        self.start_button.config(state=tk.DISABLED)
        self.update_circle()  # 半透明の円と矢印を更新

    def update_circle(self, event=None):
        if self.simulating:
            return
        try:
            x = int(self.x0_entry.get())
            y = int(self.y0_entry.get())
            v0 = float(self.v0_entry.get())*10
            angle = float(self.angle_entry.get())
        except ValueError:
            return  # 無効な値は無視

        # 半透明の円を描画（2倍サイズ）
        if self.temp_circle:
            self.cv.delete(self.temp_circle)
        self.temp_circle = self.cv.create_oval(x - 10, y - 10, x + 10, y + 10, outline="#bc8f8f", fill="#bc8f8f")

        # 半透明の矢印を描画
        if self.temp_arrow:
            self.cv.delete(self.temp_arrow)

        rad = math.radians(angle)
        arrow_x = x + v0 * math.cos(rad)
        arrow_y = y - v0 * math.sin(rad)  # y座標は反転
        self.temp_arrow = self.cv.create_line(x, y, arrow_x, arrow_y, fill="#bc8f8f", arrow=tk.LAST, width=3)

    def get_form(self):
        self.v0 = float(self.v0_entry.get())*10
        self.angle = float(self.angle_entry.get())
        self.x0 = int(self.x0_entry.get())
        self.y0 = int(self.y0_entry.get())
        self.e = float(self.e_entry.get())
        self.g = float(self.g_entry.get())*10
        self.m = float(self.m_entry.get())
        self.μ = float(self.μ_entry.get())
        self.width = int(self.width_entry.get())
        self.height = float(self.height_entry.get())

    
    def apply_settings(self):
        if self.simulating:
            return
        
        try:
            self.get_form()

            if not (0 <= self.angle < 360):
                raise ValueError("角度は0<=θ<360の範囲でなければなりません。")
        
            if not (0 <= self.e < 1):
                raise ValueError("反発係数は0<=e<1の範囲でなければなりません。")

            # 決定ボタンを無効化
            self.apply_button.config(state=tk.DISABLED)

            # 画面クリア
            self.cv.delete('all')

            # 2倍サイズの円を描画
            if self.circle:
                self.cv.delete(self.circle)
            self.circle = self.cv.create_oval(self.x0 - 10, self.y0 - 10, self.x0 + 10, self.y0 + 10, fill="red")

            # 矢印を描画
            if self.arrow:
                self.cv.delete(self.arrow)

            # windowサイズ変更
            self.simulator.geometry(f"{int(self.width)}x{int(self.height)}+800+0")

            rad = math.radians(self.angle)
            arrow_x = self.x0 + self.v0 * math.cos(rad)
            arrow_y = self.y0 - self.v0 * math.sin(rad)  # y座標は反転
            self.arrow = self.cv.create_line(self.x0, self.y0, arrow_x, arrow_y, fill="red", arrow=tk.LAST, width=3)

            self.start_button.config(state=tk.NORMAL)

        except ValueError as e:
            messagebox.showerror("入力エラー", str(e))

    def simulation(self):
        self.simulating = True

        # ボタンを無効化
        self.apply_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        # フォームのエントリーを無効化
        self.v0_entry.config(state=tk.DISABLED)
        self.angle_entry.config(state=tk.DISABLED)
        self.e_entry.config(state=tk.DISABLED)
        self.g_entry.config(state=tk.DISABLED)
        self.m_entry.config(state=tk.DISABLED)
        self.μ_entry.config(state=tk.DISABLED)
        self.x0_entry.config(state=tk.DISABLED)
        self.y0_entry.config(state=tk.DISABLED)
        self.width_entry.config(state=tk.DISABLED)
        self.height_entry.config(state=tk.DISABLED)

        # 初期位置と速度
        self.x = self.x0
        self.y = self.y0
        rad = math.radians(self.angle)

        # 水平と垂直の初速度を計算 (角度に応じてvx, vyを設定)
        self.vx = self.v0 * math.cos(rad)  # 初速度の水平成分
        self.vy = -self.v0 * math.sin(rad)  # 初速度の垂直成分

        # シミュレーションループの開始
        self.simulation_loop()

    def simulation_loop(self):
        if not self.simulating:
            return
        
        dt = 0.01  # シミュレーションの1ステップの時間（秒）

        # 垂直速度に重力加速度を加える
        self.vy += self.g * dt

        # 位置を更新
        self.x += self.vx * dt
        self.y += self.vy * dt

        # 地面に衝突した場合の処理
        ground_level = self.height - 10  # ボールの半径を考慮
        if self.y >= ground_level:
            # 反発係数を用いてバウンド
            self.y = ground_level
            self.vy = -self.vy * self.e

            # バウンドが非常に小さくなったら、転がり始める
            if abs(self.vy) < 1:
                self.vy = 0  # 縦方向の速度を0にして転がる
                # 摩擦による水平方向の減速
                friction_force = self.μ * self.m * self.g  # 摩擦力
                acceleration_friction = friction_force / self.m  # 摩擦による減速
                if self.vx > 0:
                    self.vx -= acceleration_friction * dt
                    if self.vx < 0:
                        self.vx = 0
                elif self.vx < 0:
                    self.vx += acceleration_friction * dt
                    if self.vx > 0:
                        self.vx = 0

        # 左右の壁に衝突した場合の処理
        if self.x <= 15 or self.x >= self.width - 15:  # 壁の判定を修正
            self.vx = -self.vx  # 水平方向の速度を反転

        # 画面クリア
        self.cv.delete('all')

        # 2倍サイズの円を描画
        if self.circle:
            self.cv.delete(self.circle)
        self.circle = self.cv.create_oval(self.x - 10, self.y - 10, self.x + 10, self.y + 10, fill="red")

        # シミュレーションを次のフレームに進める
        self.simulator.after(int(dt * 1000), self.simulation_loop)


    def stop_simulation(self):
        self.simulating = False
        # ボタンを有効化
        self.apply_button.config(state=tk.NORMAL)
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
    
        # フォームのエントリーを有効化
        self.v0_entry.config(state=tk.NORMAL)
        self.angle_entry.config(state=tk.NORMAL)
        self.e_entry.config(state=tk.NORMAL)
        self.g_entry.config(state=tk.NORMAL)
        self.m_entry.config(state=tk.NORMAL)
        self.μ_entry.config(state=tk.NORMAL)
        self.x0_entry.config(state=tk.NORMAL)
        self.y0_entry.config(state=tk.NORMAL)
        self.width_entry.config(state=tk.NORMAL)
        self.height_entry.config(state=tk.NORMAL)

        self.apply_settings()


    def close_windows(self):
        # Close the main window, which will automatically close the child window
        self.window.destroy()

# メインループの開始
if __name__ == "__main__":
    app = Main()
    app.simulation_loop()  # メソッドを正しく呼び出す
    app.window.mainloop()