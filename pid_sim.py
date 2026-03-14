import matplotlib.pyplot as plt


class PIDController:
    def __init__(self, Kp, Ki, Kd):
        self.Kp, self.Ki, self.Kd = Kp, Ki, Kd
        self.target = 10.0  # 目标高度：10米
        self.current_val = 0.0  # 起始高度：0米
        self.error_sum = 0.0  # 积分累加
        self.last_error = 0.0  # 上次误差（算微分用）

    def update(self, dt=0.1):
        error = self.target - self.current_val

        # P: 活在当下（误差越大，推力越大）
        p_out = self.Kp * error

        # I: 纠正过去（消除静差）
        self.error_sum += error * dt
        i_out = self.Ki * self.error_sum

        # D: 预测未来（踩刹车，防止冲过头）
        d_out = self.Kd * (error - self.last_error) / dt
        self.last_error = error

        # 总输出
        output = p_out + i_out + d_out
        self.current_val += output * dt  # 模拟无人机位置改变
        return self.current_val


# 尝试不同的参数组合
# 1. 只用 P (Kp=5, Ki=0, Kd=0) -> 会震荡或有静差
# 2. 加入 D (Kp=5, Ki=0, Kd=1) -> 变得平稳
pid = PIDController(Kp=5.0, Ki=1.5, Kd=0.5)

history = []
for _ in range(100):
    history.append(pid.update())

plt.plot(history)
plt.axhline(10, color='r', linestyle='--')  # 画出目标线
plt.title("PID Control Simulation")
plt.show()