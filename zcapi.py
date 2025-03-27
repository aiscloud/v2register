import requests
import random
import string
import threading
import time
#脚本地址：https://github.com/aiscloud/v2register
# API 地址
REGISTER_URL = "https://xxxxxx/api/v1/passport/auth/register"

# 生成随机邮箱
def random_email():
    domains = ["gmail.com", "outlook.com", "qq.com", "163.com", "yahoo.com"]
    return f"{''.join(random.choices(string.ascii_letters, k=10))}@{random.choice(domains)}"

# 生成随机密码
def random_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=12))

# 生成随机 User-Agent
def random_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    ]
    return random.choice(user_agents)

# 发送注册请求
def register():
    email = random_email()
    password = random_password()

    payload = {
        "email": email,
        "password": password,
        "email_code": 333333,  # 可能需要真实验证码
        "invite_code": "",      # 邀请码（可选）
        "recaptcha_data": ""    # 人机验证数据（可选）
    }

    headers = {
        "Content-Type": "application/json",
        "User-Agent": random_user_agent()
    }

    try:
        response = requests.post(REGISTER_URL, json=payload, headers=headers, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            token = data.get("data", {}).get("token", "No Token")
            auth_data = data.get("data", {}).get("auth_data", "No Auth Data")

            print(f"✅ 账号 {email} 注册成功！Token: {token}")

            # 保存账号信息
            with open("accounts.txt", "a") as file:
                file.write(f"{email} | {password} | {token} | {auth_data}\n")

        else:
            print(f"⚠️ 账号 {email} 注册失败！状态码: {response.status_code}，响应: {response.text}")

    except Exception as e:
        print(f"❌ 账号 {email} 注册异常：{e}")

# 线程任务（每个线程注册 50 个账号）
def thread_task(thread_id):
    print(f"🚀 线程 {thread_id} 开始执行...")

    for i in range(500000):
        print(f"🔄 线程 {thread_id} - 正在注册第 {i+1} 个账号...")
        register()
        time.sleep(random.uniform(1, 3))  # 随机延迟，防止风控

    print(f"✅ 线程 {thread_id} 任务完成！")

# 多线程批量注册（10 线程，每个线程注册 50 账号）
def main():
    threads = []
    num_threads = 50  # 10 个线程

    for i in range(num_threads):
        thread = threading.Thread(target=thread_task, args=(i+1,))
        threads.append(thread)
        thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    print("🎉 所有账号注册完成！")

if __name__ == "__main__":
    main()
