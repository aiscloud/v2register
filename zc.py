import time
import random
import string
import threading
import undetected_chromedriver as uc  # 规避反爬
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#脚本地址：https://github.com/aiscloud/v2register
# 生成随机邮箱
def random_email():
    domains = ["gmail.com", "outlook.com", "qq.com", "163.com", "yahoo.com"]
    return f"{''.join(random.choices(string.ascii_letters, k=10))}@{random.choice(domains)}"

# 生成随机密码
def random_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=12))

# 注册函数
def register(driver):
    email = random_email()
    password = random_password()

    print(f"正在注册账号: {email}")

    try:
        driver.get("https://xxxxxx/#/register")
        
        wait = WebDriverWait(driver, 30)

        # 填写邮箱
        email_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='邮箱']")))
        email_input.send_keys(email)

        # 填写密码
        password_inputs = driver.find_elements(By.XPATH, "//input[@placeholder='密码']")
        if len(password_inputs) >= 2:
            password_inputs[0].send_keys(password)
            password_inputs[1].send_keys(password)
        else:
            print("找不到密码输入框")
            return

        # 等待注册按钮
        register_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button/span[contains(text(),'注册')]")))
        register_button.click()

        print(f"✅ 账号 {email} 注册成功")
        with open("accounts.txt", "a") as file:
            file.write(f"{email} | {password}\n")

    except Exception as e:
        print(f"⚠️ 注册失败: {e}")

# 线程任务
def thread_task(thread_id):
    print(f"🚀 线程 {thread_id} 开始执行...")
    
    # 每个线程创建一个浏览器实例
    driver = uc.Chrome(headless=True)

    for i in range(50):
        print(f"🔄 线程 {thread_id} - 正在注册第 {i+1} 个账号...")
        register(driver)
        time.sleep(random.uniform(2, 5))  # 随机等待，模拟人类操作

    driver.quit()
    print(f"✅ 线程 {thread_id} 任务完成！")

# 多线程批量注册
def main():
    threads = []
    num_threads = 10  # 10个线程，每个线程注册50个账号

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
