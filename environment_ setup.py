import subprocess
import sys

def set_env_var(name, value):
    """Set an environment variable permanently (user-level)."""
    try:
        subprocess.run(
            ["cmd", "/c", "setx", name, value],
            check=True
        )
        print(f"✅ {name} set to: {value}")
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Failed to set {name}: {e}")

# === Paths (update as per your system) ===
java_home = r"C:\Program Files\Java\jdk-11"
spark_home = r"C:\Users\Devak\Softwares\spark"
hadoop_home = r"C:\Users\Devak\Softwares\spark"
python_exe = "python"   # safest option

# === Set Environment Variables ===
set_env_var("JAVA_HOME", java_home)
set_env_var("SPARK_HOME", spark_home)
set_env_var("HADOOP_HOME", hadoop_home)
set_env_var("PYSPARK_PYTHON", python_exe)

# === Update PATH (no failure even if length exceeds limit) ===
try:
    subprocess.run(
        [
            "cmd", "/c",
            f'setx PATH "%PATH%;{java_home}\\bin;{spark_home}\\bin;{hadoop_home}\\bin"'
        ],
        check=False
    )
    print("✅ PATH updated successfully.")
except Exception as e:
    print(f"⚠️ PATH update failed: {e}")

# === Summary ===
print("\n🚀 Setup complete!")
print("⚠️ Restart CMD / PyCharm / System to apply changes\n")

print("🔍 Environment Variables:")
print(f"JAVA_HOME      = {java_home}")
print(f"SPARK_HOME     = {spark_home}")
print(f"HADOOP_HOME    = {hadoop_home}")
print(f"PYSPARK_PYTHON = {python_exe}")

# set | findstr /I "JAVA_HOME SPARK_HOME HADOOP_HOME PYSPARK_PYTHON" => CHECK IN CMD