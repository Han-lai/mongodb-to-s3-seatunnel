import os

def create_seatunnel_repo_structure(root_path="."):
    """
    在指定的根路徑下創建 seatunnel-manufacturing-pipelines 的資料夾結構。

    Args:
        root_path (str): 根路徑，預設為目前工作目錄。
    """
    repo_name = "seatunnel-manufacturing-pipelines"
    repo_path = os.path.join(root_path, repo_name)

    # 創建主資料夾
    os.makedirs(repo_path, exist_ok=True)
    print(f"已創建主資料夾: {repo_path}")

    # 創建 config 資料夾及其子資料夾
    config_path = os.path.join(repo_path, "config")
    os.makedirs(os.path.join(config_path, "raw_data_processing"), exist_ok=True)
    os.makedirs(os.path.join(config_path, "aggregated_data"), exist_ok=True)
    print(f"已創建資料夾: {os.path.join(config_path, 'raw_data_processing')}")
    print(f"已創建資料夾: {os.path.join(config_path, 'aggregated_data')}")

    # 創建 scripts 資料夾及其子資料夾
    scripts_path = os.path.join(repo_path, "scripts")
    os.makedirs(os.path.join(scripts_path, "run_pipelines"), exist_ok=True)
    os.makedirs(os.path.join(scripts_path, "utils"), exist_ok=True)
    print(f"已創建資料夾: {os.path.join(scripts_path, 'run_pipelines')}")
    print(f"已創建資料夾: {os.path.join(scripts_path, 'utils')}")

    # 創建 data_samples 資料夾及其子資料夾
    data_samples_path = os.path.join(repo_path, "data_samples")
    os.makedirs(os.path.join(data_samples_path, "raw"), exist_ok=True)
    os.makedirs(os.path.join(data_samples_path, "processed"), exist_ok=True)
    print(f"已創建資料夾: {os.path.join(data_samples_path, 'raw')}")
    print(f"已創建資料夾: {os.path.join(data_samples_path, 'processed')}")

    # 創建 docs 資料夾
    docs_path = os.path.join(repo_path, "docs")
    os.makedirs(docs_path, exist_ok=True)
    print(f"已創建資料夾: {docs_path}")

    # 創建 README.md 和 .gitignore (空檔案)
    with open(os.path.join(repo_path, "README.md"), "w") as f:
        f.write("# Seatunnel Manufacturing Pipelines\n\nThis repository contains the configuration files and scripts for Seatunnel data pipelines related to manufacturing data.")
    print(f"已創建檔案: {os.path.join(repo_path, 'README.md')}")

    with open(os.path.join(repo_path, ".gitignore"), "w") as f:
        f.write("# Add files/directories to ignore here\n")
    print(f"已創建檔案: {os.path.join(repo_path, '.gitignore')}")

if __name__ == "__main__":
    # 預設在目前工作目錄下創建，您可以修改 root_path 指定其他路徑
    create_seatunnel_repo_structure()
    print("\nSeatunnel 資料夾結構已成功建立！")