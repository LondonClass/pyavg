import subprocess
import os

def upload_to_pypi(distribution_path, api_token):
    try:
        env = os.environ.copy()
        env["TWINE_PASSWORD"] = api_token
        subprocess.run(['twine', 'upload', distribution_path], check=True, env=env)
        print("上传成功!")
    except subprocess.CalledProcessError as e:
        print("上传失败:", e)

if __name__ == "__main__":
    distribution_path = 'dist/*'  # 指定要上传的软件包路径
    api_token = input("请输入您的API令牌：")
    upload_to_pypi(distribution_path, api_token)
